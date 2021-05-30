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

<h2>（2021-05-30更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, '67e2213422e441ac82fba8abceda2ce1')">公司</button>
            <button class="tablinks" onclick="showChart(event, '9a2ce5c49bf0463eaed85934b16b30fe')">城市</button>
            <button class="tablinks" onclick="showChart(event, '9c7d28afc63742328bb0c743b0c12d04')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, '632af9de4e264d82a3e627a780d81d8c')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, 'd18fa9fbb75f4f3188b6921ba8b5cb50')">区域</button>
            <button class="tablinks" onclick="showChart(event, '0bfa33fc349b40df881cfba2c2858f31')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, 'aee8d53067ed49c980c69704988a73e1')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, '993cd615e95542338330bcdd8605ecc4')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, '2aa0bc2e82db41cb9acdbe61ef064bfb')">行业</button>
            <button class="tablinks" onclick="showChart(event, 'cc514c2d85614b70b5b3f1dc4a6b8749')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, 'ed9bab0f4392473095092a343e272434')">公司福利</button>
    </div>

    <div class="box">
                <div id="67e2213422e441ac82fba8abceda2ce1" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_67e2213422e441ac82fba8abceda2ce1 = echarts.init(
            document.getElementById('67e2213422e441ac82fba8abceda2ce1'), 'white', {renderer: 'canvas'});
            
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
    
        var option_67e2213422e441ac82fba8abceda2ce1 = {
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
                45,
                43,
                24,
                20,
                19,
                18,
                16,
                16,
                15,
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
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,43,76)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,113,33)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,147,149)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,80,120)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,123,158)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,122,26)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,137,72)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,57,155)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,43,101)"
                        }
                    }
                },
                {
                    "name": "\u964c\u964c",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,145,10)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,25,120)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u591a\u591a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,28,114)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,43,80)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,153,62)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,40,66)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,155,60)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,0,6)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,97,56)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,122,22)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,18,143)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,78,102)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8054\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,22,13)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,62,112)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,50,112)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,26,31)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,103,138)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,133,32)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,45,62)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,86,105)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,1,105)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,52,56)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u91cf\u5b50",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,99,142)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,120,43)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,48,60)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,61,53)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,25,49)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,51,2)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,43,62)"
                        }
                    }
                },
                {
                    "name": "\u732b\u5c90\u667a\u80fd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,75,125)"
                        }
                    }
                },
                {
                    "name": "\u8363\u8000\u7ec8\u7aef",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,27,76)"
                        }
                    }
                },
                {
                    "name": "\u53c2\u6570",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,5,51)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,27,39)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,55,44)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,31,76)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,36,128)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7814\u7a76\u9662",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,60,44)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,127,12)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,23,130)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,35,103)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,39,85)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,106,97)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,68,90)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u4fe1\u91d1\u79d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,84,51)"
                        }
                    }
                },
                {
                    "name": "\u660e\u7565\u79d1\u6280\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,0,27)"
                        }
                    }
                },
                {
                    "name": "\u827a\u6570\u672a\u6765",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,101,107)"
                        }
                    }
                },
                {
                    "name": "\u6613\u8f66\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,67,159)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,39,68)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,134,48)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,87,18)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5411\u4e7e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,102,97)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,72,127)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,113,20)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u667a\u6167",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,80,155)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,14,72)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,68,129)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,131,125)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5b87\u65e0\u9650",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,11,133)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,110,61)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,32,44)"
                        }
                    }
                },
                {
                    "name": "\u5219\u4e00\u4f9b\u5e94\u94fe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,159,53)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,62,49)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,133,155)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5c1a\u535a\u745e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,102,156)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,58,91)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,149,26)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,81,63)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,89,77)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,105,51)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u89c6\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,1,140)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,157,149)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,67,125)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,126,1)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,145,70)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,122,109)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,133,113)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,110,149)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,75,133)"
                        }
                    }
                },
                {
                    "name": "\u6155\u601d\u5065\u5eb7\u7761\u7720",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,69,31)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,104,45)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,138,106)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,62,78)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,76,149)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,100,140)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,137,156)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,18,9)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,53,152)"
                        }
                    }
                },
                {
                    "name": "\u574e\u5fb7\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,81,0)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,35,158)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,40,109)"
                        }
                    }
                },
                {
                    "name": "NIO\u851a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,108,11)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u676d\u5dde\u7814\u7a76\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,120,131)"
                        }
                    }
                },
                {
                    "name": "\u745e\u9f99\u90a6\u730e\u5934",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,60,138)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,29,150)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,79,39)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,112,28)"
                        }
                    }
                },
                {
                    "name": "Mobvista",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,123,27)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,123,15)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,123,100)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,65,38)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,8,104)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,135,68)"
                        }
                    }
                },
                {
                    "name": "Convert lab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,8,64)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,30,61)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,54,77)"
                        }
                    }
                },
                {
                    "name": "EM3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,0,15)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,132,51)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,13,111)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,160,145)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,148,57)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u5fc3\u97f3\u7b26",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,159,28)"
                        }
                    }
                },
                {
                    "name": "\u597d\u897f\u67da\u6559\u80b2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,19,135)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u7eff\u571f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,75,118)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,14,25)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u805a\u96c6\u56e2\uff08JOYY Inc.\uff09",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,62,93)"
                        }
                    }
                },
                {
                    "name": "\u9053\u9053",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,104,62)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,47,143)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,80,101)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,131,102)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,150,159)"
                        }
                    }
                },
                {
                    "name": "\u641c\u624d\u4eba\u529b\u8d44\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,80,128)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,83,68)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,20,48)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,3,14)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,149,19)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,39,86)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,117,7)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,91,156)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,142,39)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,84,3)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,125,63)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,66,23)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,34,56)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u9014\u8bfe\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,24,68)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,112,109)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,67,43)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,60,105)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,87,109)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e92\u6559\u6559\u80b2\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,34,55)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,1,155)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,60,5)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,152,1)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,47,11)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,20,11)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,9,97)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,122,106)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,86,156)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,11,23)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,88,95)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9c81\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,127,29)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,109,65)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,28,89)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,7,117)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,85,103)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,98,96)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,2,151)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5f18\u548c\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,67,89)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u9536\u5170\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,126,51)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,32,33)"
                        }
                    }
                },
                {
                    "name": "UU\u8dd1\u817f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,69,60)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,103,61)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,132,50)"
                        }
                    }
                },
                {
                    "name": "LinkDoc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,135,33)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e5d\u8857\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,111,59)"
                        }
                    }
                },
                {
                    "name": "\u777f\u755c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,19,55)"
                        }
                    }
                },
                {
                    "name": "\u6570\u6f9c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,151,22)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u878d\u521b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,152,45)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,51,125)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,70,110)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,77,143)"
                        }
                    }
                },
                {
                    "name": "\u572d\u76ee\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,137,57)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,40,94)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,117,80)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,98,41)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,98,72)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,97,36)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u6700\u597d\u7684\u5728\u7ebf\u4eba\u8138\u8bc6\u522b\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,111,83)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u4fe1\u521b\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,104,27)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,80,136)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,147,17)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,34,157)"
                        }
                    }
                },
                {
                    "name": "Veniibot\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,64,83)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,13,123)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77\u4f18\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,94,80)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,75,3)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11\u5065\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,12,94)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,49,101)"
                        }
                    }
                },
                {
                    "name": "\u745e\u591a\u601d\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,76,11)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,73,82)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,29,24)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,139,40)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u601d\u7586",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,68,106)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,53,52)"
                        }
                    }
                },
                {
                    "name": "\u5929\u667a\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,153,12)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u777f\u667a\u836f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,134,160)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u4eab\u5929\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,90,16)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u770b\u6f2b\u753b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,80,23)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,29,151)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u56fe\u817e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,93,112)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,56,14)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,26,84)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u63a2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,138,124)"
                        }
                    }
                },
                {
                    "name": "\u864e\u535a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,5,68)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,93,22)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,111,27)"
                        }
                    }
                },
                {
                    "name": "\u552f\u54c1\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,145,103)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u76db\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,83,117)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,23,132)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,10,152)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u601d\u4fe1\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,110,80)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,9,71)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,138,71)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,153,94)"
                        }
                    }
                },
                {
                    "name": "\u97e9\u521b\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,70,79)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,43,108)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,157,111)"
                        }
                    }
                },
                {
                    "name": "\u5947\u68a6\u8005",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,91,64)"
                        }
                    }
                },
                {
                    "name": "Ximmerse",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,83,48)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7267\u539f\u6570\u5b57\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,35,26)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e91\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,100,134)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,152,137)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,81,115)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ebf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,134,138)"
                        }
                    }
                },
                {
                    "name": "\u5bc4\u4e91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,92,43)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,124,147)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53ca\u96f6\u552e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,0,110)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,98,11)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,152,26)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u4e30\u5de2\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,124,91)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,119,100)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u65b9\u548c\u5317\u4eac",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,5,136)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6d4b\u5bfc\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,103,146)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,85,93)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,7,1)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,48,97)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,1,76)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,81,14)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,134,84)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u9053\u5b87",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,119,100)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,18,107)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80fd\u534e\u667a\u80fd\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,0,136)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,23,17)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,12,4)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\uff08\u5e7f\u4e1c\uff09\u4ea7\u4e1a\u4e92\u8054\u7f51...",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,52,28)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,149,34)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u96f6\u8dc3\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,120,139)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u79d1\u5b66\u9662\u7535\u5b50\u5b66\u7814\u7a76\u6240\u82cf\u5dde\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,116,7)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,28,23)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,24,71)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,102,21)"
                        }
                    }
                },
                {
                    "name": "\u9cb2\u9e4f\u4e91\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,50,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,135,134)"
                        }
                    }
                },
                {
                    "name": "\u6613\u822a\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,20,72)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,121,148)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u60f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,155,51)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,41,8)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u725b\u7535\u52a8\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,89,20)"
                        }
                    }
                },
                {
                    "name": "\u901f\u611f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,132,52)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f71APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,17,117)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,95,113)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,131,94)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,129,74)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,18,69)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u91ce\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,146,56)"
                        }
                    }
                },
                {
                    "name": "\u667a\u52a0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,130,90)"
                        }
                    }
                },
                {
                    "name": "\u6781\u89c6\u89d2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,155,49)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,88,24)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,78,85)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,154,124)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,38,20)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,15,5)"
                        }
                    }
                },
                {
                    "name": "\u767d\u7280\u725b\u667a\u8fbe\uff08\u5317\u4eac\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,132,3)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,115,111)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,80,12)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,119,67)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\uff08\u4e2d\u56fd\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,38,16)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,61,152)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7075\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,151,59)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,97,78)"
                        }
                    }
                },
                {
                    "name": "\u601d\u56fe\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,160,153)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u5570\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,52,109)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u89c2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,117,86)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,135,132)"
                        }
                    }
                },
                {
                    "name": "eBrain",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,87,71)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,37,0)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,53,155)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,128,92)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,15,130)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u56fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,132,19)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u7279\u7eb3\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,38,61)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,77,145)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,34,112)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,135,76)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,92,115)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,14,75)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,41,59)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,101,121)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,16,129)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,131,70)"
                        }
                    }
                },
                {
                    "name": "\u6765\u56de\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,53,138)"
                        }
                    }
                },
                {
                    "name": "\u73cd\u7231\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,65,89)"
                        }
                    }
                },
                {
                    "name": "Rokid",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,24,58)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,98,50)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u7535\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,52,91)"
                        }
                    }
                },
                {
                    "name": "\u888b\u9f20\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,47,148)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9a6c\u4f01\u670d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,65,56)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,1,149)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,149,6)"
                        }
                    }
                },
                {
                    "name": "\u6653\u6a3e\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,98,82)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,146,53)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,6,157)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u7280\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,74,16)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,43,25)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6469\u8c61\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,26,124)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u4ee3\u62d3\u7075",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,118,130)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,32,30)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,43,9)"
                        }
                    }
                },
                {
                    "name": "WeLab\u536b\u76c8\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,11,45)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u7279\u7f8e\u8fea",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,125,111)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,133,92)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9Dmall",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,88,154)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,2,29)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u70b9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,106,154)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,80,7)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,36,113)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,123,85)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u540d\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,134,34)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,159,149)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,27,38)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,148,3)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u4ee5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,25,152)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,55,18)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,22,104)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u7f8e\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,29,144)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79fb\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,69,40)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u4f17\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,117,142)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u8fbe\u6570\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,131,153)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4ea7\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,101,26)"
                        }
                    }
                },
                {
                    "name": "\u886b\u6570\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,123,133)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8702\u7a9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,104,107)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,132,46)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,6,128)"
                        }
                    }
                },
                {
                    "name": "BaseBit AI \u7ffc\u65b9\u5065\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,87)"
                        }
                    }
                },
                {
                    "name": "\u5b97\u7533\u521b\u65b0\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,117,6)"
                        }
                    }
                },
                {
                    "name": "\u9756\u6208\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,156,13)"
                        }
                    }
                },
                {
                    "name": "\u5531\u5427-\u73a9\u97f3\u4e50\uff0c\u5c31\u4e0a\u5531\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,46,127)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u4e70\u53cb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,12,69)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,25,67)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e09\u77f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,83,11)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9ad8\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,55,114)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7b97\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,148,117)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5219\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,67,9)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,58,71)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,150,21)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,110,49)"
                        }
                    }
                },
                {
                    "name": "\u591a\u725b\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,21,65)"
                        }
                    }
                },
                {
                    "name": "\u6c90\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,16,39)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,68,64)"
                        }
                    }
                },
                {
                    "name": "\u6469\u822a\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,154,7)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,28,43)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u770b\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,130,74)"
                        }
                    }
                },
                {
                    "name": "\u534e\u665f\u660e\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,87,51)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,81,1)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u52bf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,142,143)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u6e38\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,64,115)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d28\u6570\u65af\u8fbe\u514b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,142,72)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5bb6\u7f51\u7edc\u6280\u672f\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,99,75)"
                        }
                    }
                },
                {
                    "name": "\u5916\u7814\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,17,87)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,6,92)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,138,65)"
                        }
                    }
                },
                {
                    "name": "\u987a\u7f51\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,68,143)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,20,27)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u6bd4\u7279\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,128,102)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,25,123)"
                        }
                    }
                },
                {
                    "name": "AfterShip",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,20,69)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8c19\u65af\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,18,5)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,110,147)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,36,47)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,82,57)"
                        }
                    }
                },
                {
                    "name": "\u5c0fi\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,4,57)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,93,154)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,59,19)"
                        }
                    }
                },
                {
                    "name": "\u81f3\u771f\u4e92\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,4,33)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u51cc\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,126,135)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,114,7)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,41,41)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,19,112)"
                        }
                    }
                },
                {
                    "name": "\u76db\u4e16\u9e92\u9e9f\u519c\u4e1a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,49,150)"
                        }
                    }
                },
                {
                    "name": "\u8054\u6613\u878dlinklogis",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,21,52)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,2,56)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,153,17)"
                        }
                    }
                },
                {
                    "name": "\u79cd\u68a6\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,89,66)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,66,158)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,96,88)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u667a\u80fd\u5236\u9020\u8f6f\u4ef6\u5f00\u53d1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,136,74)"
                        }
                    }
                },
                {
                    "name": "\u65af\u683c\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,133,63)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u6c7d\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,63,111)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u62c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,120,22)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,60,71)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,2,131)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,45,46)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8f85\u7279\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,40,78)"
                        }
                    }
                },
                {
                    "name": "\u7231\u8bed\u5427",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,124,89)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,16,27)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,31,76)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,29,12)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,145,92)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5fc5\u80dc\u4e92\u5a31\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,59,23)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7fcc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,77,68)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,135,69)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u4e16\u7eaa\u4e1c\u65b9\u901a\u8baf\u8bbe\u5907\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,2,159)"
                        }
                    }
                },
                {
                    "name": "\u8109\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,50,64)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u79d1\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,45,66)"
                        }
                    }
                },
                {
                    "name": "\u94a2\u94c1\u4fa0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,111,137)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,32,96)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,61,73)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,31,111)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,3,58)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u661f\u63a2\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,10,20)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,10,65)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,46,58)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7279\u66fc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,45,21)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,21,153)"
                        }
                    }
                },
                {
                    "name": "\u771f\u6e90\u6865\u4f01\u4e1a\u54a8\u8be2\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,112,146)"
                        }
                    }
                },
                {
                    "name": "\u8d28\u5b50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,156,115)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,153,34)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,149,148)"
                        }
                    }
                },
                {
                    "name": "Nox\u591c\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,18,112)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5927\u8baf\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,147,148)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,72,134)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,30,158)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,118,106)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u7ff0\u683c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,136,137)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,35,39)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,39,120)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,96,65)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,39,148)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,36,82)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,86,8)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,69,88)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,146,48)"
                        }
                    }
                },
                {
                    "name": "\u8c46\u679c\u7f8e\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,50,35)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,25,155)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,99,5)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,132)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,48,103)"
                        }
                    }
                },
                {
                    "name": "\u4e3d\u7acb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,98,123)"
                        }
                    }
                },
                {
                    "name": "\u745e\u5a01\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,123,85)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,46,133)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5370\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,25,56)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u8dc3\u6609\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,111,61)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,68,159)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,130,74)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,87,36)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u96c6\u8054\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,29,150)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u666e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,2,38)"
                        }
                    }
                },
                {
                    "name": "\u5965\u6bd4\u4e2d\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,69,64)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,154,13)"
                        }
                    }
                },
                {
                    "name": "Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,77,45)"
                        }
                    }
                },
                {
                    "name": "\u667a\u878d\u4fe1\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,51,110)"
                        }
                    }
                },
                {
                    "name": "\u957f\u4ead\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,58,102)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u80fd\u8fbe\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,30,148)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6167\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,23,82)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,19,53)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u7ae0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,85,57)"
                        }
                    }
                },
                {
                    "name": "\u5373\u6784\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,143,43)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,89,109)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,73,79)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,6,66)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,16,47)"
                        }
                    }
                },
                {
                    "name": "\u4e98\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,80,139)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,33,115)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,19,132)"
                        }
                    }
                },
                {
                    "name": "\u5149\u9274\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,68,140)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,16,31)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,133,151)"
                        }
                    }
                },
                {
                    "name": "\u9014\u5bb6\u6c11\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,156,147)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,105,126)"
                        }
                    }
                },
                {
                    "name": "\u5353\u8f69\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,64,104)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,10)"
                        }
                    }
                },
                {
                    "name": "\u70ed\u4e91\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,21,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,95,154)"
                        }
                    }
                },
                {
                    "name": "\u6c57\u9a6c\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,122,43)"
                        }
                    }
                },
                {
                    "name": "FreeWheel",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,47,45)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u98de\u7f51\u7edc-\u8f66\u8f7d\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,69,129)"
                        }
                    }
                },
                {
                    "name": "\u5bd3\u8a00\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,138,72)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,59,14)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u6570\u79d1\u96c6\u56e2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,81,100)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,125,134)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,82,77)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,74,140)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5353\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,1,114)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u76f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,108,28)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,31,121)"
                        }
                    }
                },
                {
                    "name": "Udesk\uff0d\u4f01\u4e1a\u7ea7\u667a\u80fd\u5ba2\u670d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,39,40)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,88,41)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u91d1\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,125,73)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u7403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,69,150)"
                        }
                    }
                },
                {
                    "name": "\u9038\u4eab\u7535\u5b50\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,1,116)"
                        }
                    }
                },
                {
                    "name": "\u503c\u5f97\u4e70\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,92,112)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,58,76)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,31,159)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,159,4)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,56,30)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,125,107)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,36,145)"
                        }
                    }
                },
                {
                    "name": "\u83ab\u6bd4\u55e8\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,12,63)"
                        }
                    }
                },
                {
                    "name": "DataEye",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,88,55)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4e13\u5bb6.COM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,60,22)"
                        }
                    }
                },
                {
                    "name": "\u53cb\u5854\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,92,96)"
                        }
                    }
                },
                {
                    "name": "Fordeal",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,70,144)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,44,105)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,102,9)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,150,111)"
                        }
                    }
                },
                {
                    "name": "\u592a\u521d\u5f08\u5baa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,125,14)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,65,111)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,11,127)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,102,127)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,114,33)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5f84\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,100,96)"
                        }
                    }
                },
                {
                    "name": "\u68a6\u9977\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,82,138)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,20,144)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,30,55)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,67,4)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u7f51\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,60,57)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,38,16)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u89c8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,20,149)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,153,116)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u7ef4\u667a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,74,79)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,66,24)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,11,16)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,11,107)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6728\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,131,93)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,59,146)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,83,76)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6df1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,102,103)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,144,66)"
                        }
                    }
                },
                {
                    "name": "UMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,138,146)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,103,132)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u91cd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,145,77)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u91d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,21,116)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u89c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,133,73)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,55,137)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4ec1\u5065\u5eb7\u533b\u7597\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,142,63)"
                        }
                    }
                },
                {
                    "name": "\u67d2\u96f6\u58f9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,107,134)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,98,116)"
                        }
                    }
                },
                {
                    "name": "\u6700\u53f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,12,36)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,19,140)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,77,74)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,132,33)"
                        }
                    }
                },
                {
                    "name": "\u98de\u5e38\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,147,0)"
                        }
                    }
                },
                {
                    "name": "\u7425\u73c0\u521b\u60f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,135,0)"
                        }
                    }
                },
                {
                    "name": "\u822a\u5929\u7231\u9510",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,9,5)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u77e5\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,4,114)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,69,158)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,42,31)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u627f\u6cf0\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,25,28)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u5b9a\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,53,17)"
                        }
                    }
                },
                {
                    "name": "\u8d22\u76c8\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,127,52)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98ce\u7231\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,90,119)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5fc5\u9009\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,1,135)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u4f4e\u78b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,112,109)"
                        }
                    }
                },
                {
                    "name": "\u5154\u73a9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,28,57)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,106,24)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,78,39)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d0\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,111,75)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,47,145)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,87,151)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,157,89)"
                        }
                    }
                },
                {
                    "name": "\u9091\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,95,58)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,83,37)"
                        }
                    }
                },
                {
                    "name": "\u9636\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,6,14)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9488\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,30,50)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,17,62)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6781\u777f\u79d1\u6280\u6709\u9650\u8d23\u4efb\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,22,118)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,140,21)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5b8f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,13,77)"
                        }
                    }
                },
                {
                    "name": "\u9e70\u4e4b\u773c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,143,91)"
                        }
                    }
                },
                {
                    "name": "\u6c85\u9038\u65b9\u8fbe\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,61,19)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,15,24)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,150,98)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,6,126)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,117,109)"
                        }
                    }
                },
                {
                    "name": "spring professional",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,149,122)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,116,15)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u4ed5\u8fbe\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,59,10)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u70b9\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,134,62)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u95fb\u6b4c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,46,30)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6d1b\u514b\u822a\u7a7a\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,126,86)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u653f\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,18,89)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,9,95)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,127,160)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,56,71)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u5fc3\u529b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,76,88)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,26,63)"
                        }
                    }
                },
                {
                    "name": "InMobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,47,3)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,157,134)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,45,91)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,133,146)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,101,62)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,102,34)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u5fc3\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,62,2)"
                        }
                    }
                },
                {
                    "name": "IntraMirror",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,7,53)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,86,158)"
                        }
                    }
                },
                {
                    "name": "\u516d\u4e00\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,96,7)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,137,60)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,122,108)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,27,31)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,32,129)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,97,4)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,139,53)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u4e91\u6749",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,154,135)"
                        }
                    }
                },
                {
                    "name": "\u548c\u7f8e\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,60,111)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,119,90)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u987f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,137,4)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u90a6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,60,89)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u9f13\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,42,46)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6b21\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,17,27)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,138,42)"
                        }
                    }
                },
                {
                    "name": "\u660e\u671d\u4e07\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,131,19)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5bb6\u5065\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,62,95)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,30,118)"
                        }
                    }
                },
                {
                    "name": "\u4ee5\u89c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,18,58)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u679c\u6bd4\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,147,26)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,133,4)"
                        }
                    }
                },
                {
                    "name": "Sleepace \u4eab\u7761",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,14,75)"
                        }
                    }
                },
                {
                    "name": "\u9e3f\u6cf0\u9f0e\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,109,132)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,39,159)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8fea\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,146,71)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,117,100)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,38,115)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6f14\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,60,40)"
                        }
                    }
                },
                {
                    "name": "\u76ca\u76df\u64cd\u76d8\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,49,17)"
                        }
                    }
                },
                {
                    "name": "\u8d62\u706b\u866b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,83,121)"
                        }
                    }
                },
                {
                    "name": "\u660e\u6e90\u4e91\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,49,140)"
                        }
                    }
                },
                {
                    "name": "OPENAILAB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,135,147)"
                        }
                    }
                },
                {
                    "name": "\u8354\u679d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,146,57)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,82,149)"
                        }
                    }
                },
                {
                    "name": "\u8baf\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,159,126)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,147,103)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,11,110)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,25,10)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u7f19\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,142,126)"
                        }
                    }
                },
                {
                    "name": "\u6f2b\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,75,41)"
                        }
                    }
                },
                {
                    "name": "\u9541\u4fe1\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,113,118)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,27,76)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5bb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,46,33)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,41,37)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,40,109)"
                        }
                    }
                },
                {
                    "name": "OSR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,62,2)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,73,21)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u57ce\u601d\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,19,107)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,11,19)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u5ba2\u6615\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,75,56)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u798f\u7984\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,141,115)"
                        }
                    }
                },
                {
                    "name": "\u53eb\u53eb\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,117,13)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6570\u667a\u82af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,72,75)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u521b\u66e6\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,111,129)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5fae\u5149\u96c6\u7535\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,69,124)"
                        }
                    }
                },
                {
                    "name": "\u67ab\u53f6\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,156,54)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,18,0)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,159,97)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,159,87)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99\u7adf\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,54,131)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8c61\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,91,120)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,9,100)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,25,94)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,108,8)"
                        }
                    }
                },
                {
                    "name": "\u667a\u4e91\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,71,92)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,113,15)"
                        }
                    }
                },
                {
                    "name": "\u5341\u624d\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,40,55)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u5c0f\u6ee1\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,7,68)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f26\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,36,131)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u5929\u5fae\u661f\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,85,88)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e2d\u8f6f\u534e\u817e\u8f6f\u4ef6\u7cfb\u7edf\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,158,97)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,122,90)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,97,57)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,84,112)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,18,53)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,121,87)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u6f2b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,115,74)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,151,21)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u9886\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,80,159)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,144,92)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,91,53)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,38,39)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u4f17\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,31,140)"
                        }
                    }
                },
                {
                    "name": "\u533b\u51c6\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,23,89)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u8302\u5929\u521d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,92,67)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,70,141)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,72,71)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,18,67)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,29,122)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u667a\u52a0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,2,1)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u8346\u6843\u674e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,26,67)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5de5\u540c\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,22,50)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,117,141)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,132,43)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5e2e\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,144,117)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,23,53)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,60,107)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u67da\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,99,108)"
                        }
                    }
                },
                {
                    "name": "\u4e01\u9999\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,125,128)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,89,116)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,115,160)"
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
                "\u5b57\u8282\u8df3\u52a8",
                "\u7f8e\u56e2",
                "\u5e73\u5b89\u79d1\u6280",
                "Insta360\u5f71\u77f3",
                "\u4eac\u4e1c\u96c6\u56e2",
                "\u6ef4\u6ef4",
                "\u9177\u5bb6\u4e50",
                "OPPO",
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
        chart_67e2213422e441ac82fba8abceda2ce1.setOption(option_67e2213422e441ac82fba8abceda2ce1);
    </script>
                <div id="9a2ce5c49bf0463eaed85934b16b30fe" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_9a2ce5c49bf0463eaed85934b16b30fe = echarts.init(
            document.getElementById('9a2ce5c49bf0463eaed85934b16b30fe'), 'white', {renderer: 'canvas'});
        var option_9a2ce5c49bf0463eaed85934b16b30fe = {
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
                637,
                309,
                309,
                171,
                71,
                61,
                29,
                15,
                11,
                8
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
                    "value": 637,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,116,142)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 309,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,136,121)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 309,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,44,145)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 171,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,111,45)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,82,20)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,124,116)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,140,27)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,82,35)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,151,34)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,63,102)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,9,109)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,52,139)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,137,146)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,151,96)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,18,58)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,20,124)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,121,68)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,47,112)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,4,6)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,84,142)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6d25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,82,103)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,30,145)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,7,75)"
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
                "\u6df1\u5733",
                "\u4e0a\u6d77",
                "\u676d\u5dde",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u6b66\u6c49",
                "\u82cf\u5dde",
                "\u4f5b\u5c71",
                "\u53a6\u95e8"
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
        chart_9a2ce5c49bf0463eaed85934b16b30fe.setOption(option_9a2ce5c49bf0463eaed85934b16b30fe);
    </script>
                <div id="9c7d28afc63742328bb0c743b0c12d04" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9c7d28afc63742328bb0c743b0c12d04 = echarts.init(
            document.getElementById('9c7d28afc63742328bb0c743b0c12d04'), 'white', {renderer: 'canvas'});
        var option_9c7d28afc63742328bb0c743b0c12d04 = {
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
                    "value": 637,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 309,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 309,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 171,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 71,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 61,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 29,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 15,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 11,
                    "name": "\u4f5b\u5c71"
                },
                {
                    "value": 8,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 7,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 7,
                    "name": "\u957f\u6c99"
                },
                {
                    "value": 6,
                    "name": "\u897f\u5b89"
                },
                {
                    "value": 5,
                    "name": "\u91cd\u5e86"
                },
                {
                    "value": 4,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u9521"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u5408\u80a5"
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
                    "value": 1,
                    "name": "\u5929\u6d25"
                },
                {
                    "value": 1,
                    "name": "\u798f\u5dde"
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
        chart_9c7d28afc63742328bb0c743b0c12d04.setOption(option_9c7d28afc63742328bb0c743b0c12d04);
    </script>
                <div id="632af9de4e264d82a3e627a780d81d8c" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_632af9de4e264d82a3e627a780d81d8c = echarts.init(
            document.getElementById('632af9de4e264d82a3e627a780d81d8c'), 'white', {renderer: 'canvas'});
            
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
    
        var option_632af9de4e264d82a3e627a780d81d8c = {
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
                        637
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        309
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        309
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        171
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        71
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        61
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        29
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        15
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
                        8
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        7
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
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
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        5
                    ]
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        4
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
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
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
                    "name": "\u5929\u6d25",
                    "value": [
                        117.200983,
                        39.084158,
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
        chart_632af9de4e264d82a3e627a780d81d8c.setOption(option_632af9de4e264d82a3e627a780d81d8c);
    </script>
                <div id="d18fa9fbb75f4f3188b6921ba8b5cb50" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_d18fa9fbb75f4f3188b6921ba8b5cb50 = echarts.init(
            document.getElementById('d18fa9fbb75f4f3188b6921ba8b5cb50'), 'white', {renderer: 'canvas'});
        var option_d18fa9fbb75f4f3188b6921ba8b5cb50 = {
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
                172,
                134,
                131,
                42,
                41,
                40,
                38,
                36,
                35,
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
                    "value": 172,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,4,102)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 134,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,53,122)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 131,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,108,41)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,158,148)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,127,60)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,99,147)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,150,21)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,24,48)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,131,102)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,134,11)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,115,159)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,94,90)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,37,9)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,81,28)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,11,72)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,152,42)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,143,43)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,49,153)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,121,104)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,4,58)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,43,99)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,146,51)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,155,97)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,86,10)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,126,117)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,121,71)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,94,64)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,20,78)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,110,155)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,146,117)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,70,22)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,5,58)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,86,20)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,46,6)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,72,93)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,124,68)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,67,60)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,146,39)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,119,125)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,43,20)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,4,124)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,88,152)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,60,42)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,112,129)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,80,121)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,142,113)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,81,105)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,152,113)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,27,49)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,39,30)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,1,99)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,134,15)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,120,149)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,97,8)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,121,4)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,78,105)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,130,17)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,52,61)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,150,70)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,55,157)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,148,55)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,115,101)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,58,91)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,2,59)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,103,6)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,125,137)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,12,64)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,23,52)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,23,5)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,79,77)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,136,71)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,138,102)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,78,12)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,89,131)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,135,82)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,23,140)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,102,36)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,121,9)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,84,71)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,47,47)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,45,120)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,130,87)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,41,108)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,61,85)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,21,50)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,132,95)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,51,87)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,63,130)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,94,54)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,59,79)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,160,110)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,7,113)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,153,49)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8425",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,153,33)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9a\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,41,2)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,94,130)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,22,86)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,15,30)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,126,72)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,122,26)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,84,24)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,85,34)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,76,76)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,14,48)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,52,50)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,104,44)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,29,91)"
                        }
                    }
                },
                {
                    "name": "\u65e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,68,98)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,107,128)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,142,95)"
                        }
                    }
                },
                {
                    "name": "\u673a\u6295\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,121,129)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,105,100)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,21,160)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,11,29)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,120,31)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6c34\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,140,41)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,51,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,81,48)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,25,86)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,3,128)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9f99\u5761\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,13,135)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,153,94)"
                        }
                    }
                },
                {
                    "name": "\u5929\u76ee\u5c71\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,50,11)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,21,8)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,127,47)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,83,148)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,108,116)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,78,118)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,39,36)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u8def",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,52,155)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u5858\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,90,89)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,40,0)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,35,95)"
                        }
                    }
                },
                {
                    "name": "\u76d0\u7530\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,118,63)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6d77\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,3,47)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5885\u6e56",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,137,123)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,91,63)"
                        }
                    }
                },
                {
                    "name": "\u6885\u9647",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,28,61)"
                        }
                    }
                },
                {
                    "name": "\u5b98\u6d32",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,154,140)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,65,157)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,145,37)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,139,141)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,3,111)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6cc9\u9a7f\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,0,108)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,91,78)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5858",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,92,101)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,48,36)"
                        }
                    }
                },
                {
                    "name": "\u80dc\u6d66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,114,30)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,101,34)"
                        }
                    }
                },
                {
                    "name": "\u671d\u5916",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,160,48)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,36,152)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,69,153)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,81,14)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,79,12)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,75,121)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u5143\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,57,38)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,39,39)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,120,6)"
                        }
                    }
                },
                {
                    "name": "\u5149\u660e\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,142,53)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f\u4e1c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,62,113)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,132,133)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,0,21)"
                        }
                    }
                },
                {
                    "name": "\u6ca3\u6e2d\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,117,88)"
                        }
                    }
                },
                {
                    "name": "\u9b4f\u516c\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,85,33)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,91,131)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,7,14)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u5c9b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,143,99)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,158,85)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,46,50)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,29,42)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,159,63)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,125,25)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,140,49)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,24,71)"
                        }
                    }
                },
                {
                    "name": "\u6f58\u5bb6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,0,105)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,10,54)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,93,46)"
                        }
                    }
                },
                {
                    "name": "\u5434\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,48,85)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e00\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,129,19)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,123,99)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,139,59)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6ca7\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,31,114)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,6,0)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,65,101)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,51,143)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,132,158)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,29,138)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8fde\u6d3c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,11,44)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,96,48)"
                        }
                    }
                },
                {
                    "name": "\u5927\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,60,86)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,76,128)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99\u53bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,76,5)"
                        }
                    }
                },
                {
                    "name": "\u8700\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,61,6)"
                        }
                    }
                },
                {
                    "name": "\u51bc\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,66,135)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6d77\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,9,111)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,62,14)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,135,136)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,157,0)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6c5f\u6e7e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,39,27)"
                        }
                    }
                },
                {
                    "name": "\u78a7\u4e91\u793e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,151,42)"
                        }
                    }
                },
                {
                    "name": "\u5510\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,47,57)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,27,78)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,29,126)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,53,106)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,82,108)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,39,80)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,43,41)"
                        }
                    }
                },
                {
                    "name": "\u6797\u6821\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,142,78)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,51,2)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,100,98)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,23,119)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,127,150)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,24,73)"
                        }
                    }
                },
                {
                    "name": "\u911e\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,142,13)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e49\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,5,119)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,132,113)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u534e\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,150,1)"
                        }
                    }
                },
                {
                    "name": "\u5ba3\u6b66\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,148,159)"
                        }
                    }
                },
                {
                    "name": "\u8700\u6c49\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,32,114)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,28,0)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,47,62)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,90,129)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,137,61)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u5e7f\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,15,58)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,146,6)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u798f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,155,71)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,66,35)"
                        }
                    }
                },
                {
                    "name": "\u7fe0\u82d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,149,52)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,77,81)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,28,134)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,115,84)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,158,49)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,17,35)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,3,147)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,77,9)"
                        }
                    }
                },
                {
                    "name": "\u7436\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,41,44)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5bff\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,107,27)"
                        }
                    }
                },
                {
                    "name": "\u5858\u8fb9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,66,8)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,33,158)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5fb7\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,127,60)"
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
                "\u79d1\u6280\u56ed",
                "\u4f59\u676d\u533a",
                "\u897f\u5317\u65fa",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u5b9d\u5b89\u533a",
                "\u671b\u4eac",
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
        chart_d18fa9fbb75f4f3188b6921ba8b5cb50.setOption(option_d18fa9fbb75f4f3188b6921ba8b5cb50);
    </script>
                <div id="0bfa33fc349b40df881cfba2c2858f31" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0bfa33fc349b40df881cfba2c2858f31 = echarts.init(
            document.getElementById('0bfa33fc349b40df881cfba2c2858f31'), 'white', {renderer: 'canvas'});
        var option_0bfa33fc349b40df881cfba2c2858f31 = {
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
                    "value": 172,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 134,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 131,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 42,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 41,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 40,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 38,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 36,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 35,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 34,
                    "name": "\u4e2d\u5173\u6751"
                },
                {
                    "value": 33,
                    "name": "\u95f5\u884c\u533a"
                },
                {
                    "value": 30,
                    "name": "\u5f90\u6c47\u533a"
                },
                {
                    "value": 28,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 26,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 26,
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 26,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 25,
                    "name": "\u897f\u6e56\u533a"
                },
                {
                    "value": 22,
                    "name": "\u6b66\u4faf\u533a"
                },
                {
                    "value": 20,
                    "name": "\u8679\u53e3\u533a"
                },
                {
                    "value": 19,
                    "name": "\u897f\u6eaa"
                },
                {
                    "value": 16,
                    "name": "\u957f\u5b81\u533a"
                },
                {
                    "value": 15,
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 14,
                    "name": "\u6ee8\u6c5f\u533a"
                },
                {
                    "value": 14,
                    "name": "\u77e5\u6625\u8def"
                },
                {
                    "value": 13,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 13,
                    "name": "\u6768\u6d66\u533a"
                },
                {
                    "value": 13,
                    "name": "\u5927\u51b2"
                },
                {
                    "value": 12,
                    "name": "\u62f1\u5885\u533a"
                },
                {
                    "value": 12,
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 11,
                    "name": "\u897f\u4e8c\u65d7"
                },
                {
                    "value": 11,
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 11,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
                },
                {
                    "value": 10,
                    "name": "\u9f99\u534e\u65b0\u2026"
                },
                {
                    "value": 9,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 9,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 9,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 9,
                    "name": "\u5de5\u4e1a\u56ed\u2026"
                },
                {
                    "value": 9,
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 8,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 8,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 8,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 8,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 8,
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 8,
                    "name": "\u77f3\u666f\u5c71\u2026"
                },
                {
                    "value": 8,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 8,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 7,
                    "name": "\u5357\u6c99\u533a"
                },
                {
                    "value": 7,
                    "name": "\u897f\u4e09\u65d7"
                },
                {
                    "value": 7,
                    "name": "\u6d77\u73e0\u533a"
                },
                {
                    "value": 7,
                    "name": "\u6d2a\u5c71\u533a"
                },
                {
                    "value": 7,
                    "name": "\u5f90\u5bb6\u6c47"
                },
                {
                    "value": 7,
                    "name": "\u9ec4\u6d66\u533a"
                },
                {
                    "value": 6,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 6,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 6,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 6,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 6,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 6,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 5,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 5,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 5,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 5,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 5,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 5,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 5,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 5,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 5,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 4,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 4,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 4,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 4,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 4,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 4,
                    "name": "\u6587\u4e09\u8def"
                },
                {
                    "value": 4,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 4,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5f90\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u9759\u5b89\u533a"
                },
                {
                    "value": 3,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 3,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 3,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 3,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 3,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 3,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u8425"
                },
                {
                    "value": 3,
                    "name": "\u5609\u5b9a\u533a"
                },
                {
                    "value": 3,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 3,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 3,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 2,
                    "name": "\u65e0"
                },
                {
                    "value": 2,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 2,
                    "name": "\u673a\u6295\u6865"
                },
                {
                    "value": 2,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 2,
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u6c34\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 2,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 2,
                    "name": "\u4e5d\u9f99\u5761\u2026"
                },
                {
                    "value": 2,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u5929\u76ee\u5c71\u2026"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 2,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 2,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u6e05\u6cb3"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u8def"
                },
                {
                    "value": 2,
                    "name": "\u94b1\u5858\u533a"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u76d0\u7530\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5357\u6d77\u533a"
                },
                {
                    "value": 2,
                    "name": "\u72ec\u5885\u6e56"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u6885\u9647"
                },
                {
                    "value": 2,
                    "name": "\u5b98\u6d32"
                },
                {
                    "value": 2,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5357\u5934"
                },
                {
                    "value": 2,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u6cc9\u9a7f\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5858"
                },
                {
                    "value": 2,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 2,
                    "name": "\u80dc\u6d66"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 2,
                    "name": "\u671d\u5916"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 2,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u5143\u6865"
                },
                {
                    "value": 2,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u6d41\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5149\u660e\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6e2f\u4e1c"
                },
                {
                    "value": 1,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u6ca3\u6e2d\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u9b4f\u516c\u6751"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u5c9b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u884c"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u5dde\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6f58\u5bb6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u56ed\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5434\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u6587\u4e00\u8def"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u6ca7\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u8fde\u6d3c"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u5927\u77f3"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6865"
                },
                {
                    "value": 1,
                    "name": "\u957f\u6c99\u53bf"
                },
                {
                    "value": 1,
                    "name": "\u8700\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u51bc\u6751"
                },
                {
                    "value": 1,
                    "name": "\u6ee8\u6d77\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 1,
                    "name": "\u9f99\u6eaa"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6c5f\u6e7e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u78a7\u4e91\u793e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5510\u9547"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 1,
                    "name": "\u5e73\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6797\u6821\u8def"
                },
                {
                    "value": 1,
                    "name": "\u4e03\u5b9d"
                },
                {
                    "value": 1,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5c71\u533b\u2026"
                },
                {
                    "value": 1,
                    "name": "\u911e\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u987a\u4e49\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u534e\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5ba3\u6b66\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u8700\u6c49\u8def"
                },
                {
                    "value": 1,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u8679\u6865"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u4eac\u5e7f\u6865"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u798f\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u7fe0\u82d1"
                },
                {
                    "value": 1,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1\u533a"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6865"
                },
                {
                    "value": 1,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 1,
                    "name": "\u5317\u5927\u5730"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u7436\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5bff\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5858\u8fb9"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
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
        chart_0bfa33fc349b40df881cfba2c2858f31.setOption(option_0bfa33fc349b40df881cfba2c2858f31);
    </script>
                <div id="aee8d53067ed49c980c69704988a73e1" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_aee8d53067ed49c980c69704988a73e1 = echarts.init(
            document.getElementById('aee8d53067ed49c980c69704988a73e1'), 'white', {renderer: 'canvas'});
        var option_aee8d53067ed49c980c69704988a73e1 = {
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
                426,
                337,
                210,
                190,
                171,
                133,
                112,
                87
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
                    "value": 426
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 337
                },
                {
                    "name": "A\u8f6e",
                    "value": 210
                },
                {
                    "name": "B\u8f6e",
                    "value": 190
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 171
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 133
                },
                {
                    "name": "C\u8f6e",
                    "value": 112
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 87
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
                    "value": 426
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 337
                },
                {
                    "name": "A\u8f6e",
                    "value": 210
                },
                {
                    "name": "B\u8f6e",
                    "value": 190
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 171
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 133
                },
                {
                    "name": "C\u8f6e",
                    "value": 112
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 87
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
        chart_aee8d53067ed49c980c69704988a73e1.setOption(option_aee8d53067ed49c980c69704988a73e1);
    </script>
                <div id="993cd615e95542338330bcdd8605ecc4" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_993cd615e95542338330bcdd8605ecc4 = echarts.init(
            document.getElementById('993cd615e95542338330bcdd8605ecc4'), 'white', {renderer: 'canvas'});
        var option_993cd615e95542338330bcdd8605ecc4 = {
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
                344,
                325,
                305,
                171,
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
                    "value": 501
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 344
                },
                {
                    "name": "50-150\u4eba",
                    "value": 325
                },
                {
                    "name": "150-500\u4eba",
                    "value": 305
                },
                {
                    "name": "15-50\u4eba",
                    "value": 171
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
                    "value": 501
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 344
                },
                {
                    "name": "50-150\u4eba",
                    "value": 325
                },
                {
                    "name": "150-500\u4eba",
                    "value": 305
                },
                {
                    "name": "15-50\u4eba",
                    "value": 171
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
                "500-2000\u4eba",
                "50-150\u4eba",
                "150-500\u4eba",
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
                "50-150\u4eba",
                "150-500\u4eba",
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
        chart_993cd615e95542338330bcdd8605ecc4.setOption(option_993cd615e95542338330bcdd8605ecc4);
    </script>
                <div id="2aa0bc2e82db41cb9acdbe61ef064bfb" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_2aa0bc2e82db41cb9acdbe61ef064bfb = echarts.init(
            document.getElementById('2aa0bc2e82db41cb9acdbe61ef064bfb'), 'white', {renderer: 'canvas'});
        var option_2aa0bc2e82db41cb9acdbe61ef064bfb = {
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
                545,
                284,
                199,
                195,
                169,
                126,
                97
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
                    "value": 545,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,78,70)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 284,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,31,109)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 199,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,21,127)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 195,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,61,62)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 169,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,156,35)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 126,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,14,30)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,47,36)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,30,106)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,97,8)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,98,150)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,111,109)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,50,110)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,63,6)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,97,69)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,157,108)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,1,16)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,52,2)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,134,140)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,50,150)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,48,59)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,47,139)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,116,105)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,14,103)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,98,45)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,126,87)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,160,130)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,120,10)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,119,61)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,137,122)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,17,122)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,83,80)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,121,30)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,91,97)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,12,72)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,46,60)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,108,43)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,84,73)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,35,11)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,130,154)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,106,134)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,113,106)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,0,97)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,101,62)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,129,7)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,56,72)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,133,115)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,42,24)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,47,58)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,80,54)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,131,8)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,29,104)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,88,58)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,25,120)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,142,95)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,56,91)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,124,118)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,50,128)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,140,131)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,83,85)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,69,136)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,9,30)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,41,88)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,64,75)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,45,64)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,13,90)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,41,50)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,68,149)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,91,126)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,72,8)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,93,36)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,111,160)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,28,65)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,8,120)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,112,92)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,39,2)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,105,59)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1\u3001\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,127,45)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,28,66)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,134,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,24,118)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,132,22)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,40,112)"
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
        chart_2aa0bc2e82db41cb9acdbe61ef064bfb.setOption(option_2aa0bc2e82db41cb9acdbe61ef064bfb);
    </script>
                <div id="cc514c2d85614b70b5b3f1dc4a6b8749" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_cc514c2d85614b70b5b3f1dc4a6b8749 = echarts.init(
            document.getElementById('cc514c2d85614b70b5b3f1dc4a6b8749'), 'white', {renderer: 'canvas'});
        var option_cc514c2d85614b70b5b3f1dc4a6b8749 = {
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
                471,
                101,
                87,
                52,
                48,
                32,
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
                    "value": 471,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,148,70)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 101,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,140,58)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,147,127)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,140,41)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,126,113)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,159,159)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,150,59)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,73,98)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,130,19)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,152,61)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,39,107)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,19,21)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,5,100)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,143,116)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,26,77)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,158,130)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,115,4)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,25,132)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,12,123)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,116,105)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,147,84)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,136,139)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,59,115)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,133,47)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,126,55)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,82,32)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,42,78)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,104,111)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,90,116)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,146,28)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,88,101)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,8,149)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,8,100)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,30,16)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,142,138)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,16,65)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,110,53)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,155,24)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,29,94)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,11,57)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,107,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,47,75)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,81,86)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,121,60)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,157,160)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,43,75)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,7,8)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,116,57)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,116,89)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,62,63)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,30,155)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,149,140)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,112,39)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,153,13)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,48,151)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,148,78)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,46,23)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,150,47)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,145,37)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,93,120)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,54,7)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,72,133)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,160,146)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,70,61)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,6,145)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,4,2)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,142,160)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,132,77)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6691\u5047\u5b9e\u4e60\u751f\u3011\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,113,60)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,13,26)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,149,139)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,102,137)"
                        }
                    }
                },
                {
                    "name": "DSP\u5e7f\u544a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,8,6)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,37,44)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u9891/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,54,19)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,24,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,27,119)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,104,104)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,76,160)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,31,7)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,139,151)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u5e08\\\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,153,102)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,31,16)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,110,18)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,53,99)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,106,66)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,120,154)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5546\u54c1\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,20,87)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,50,63)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,43,101)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,21,105)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,60,81)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,2,59)"
                        }
                    }
                },
                {
                    "name": "GNSS\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,78,82)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,33,10)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,144,157)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,59,155)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,19,106)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,86,122)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,0,35)"
                        }
                    }
                },
                {
                    "name": "\u7ec4\u5408\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,52,153)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,24,121)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u7814\u7a76\u5458/\u4e34\u5e8a\u7814\u7a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,95,138)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6027\u80fd\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,28,12)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,103,141)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,116,59)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,25,11)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,140,158)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7d27\u6025\u5c97\u4f4d\u3011\u301095\u5206\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,49,124)"
                        }
                    }
                },
                {
                    "name": "1121PC-LT-354-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,146,159)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,54,69)"
                        }
                    }
                },
                {
                    "name": "00233-\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,55,149)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u4eba\u4f53/\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,48,62)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,100,64)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,149,49)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,84,75)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,138,40)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,13,95)"
                        }
                    }
                },
                {
                    "name": "024254-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,77,62)"
                        }
                    }
                },
                {
                    "name": "02416A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,151,72)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u5185\u63a8 - \u5f00\u53d1/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,47,62)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,122,121)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u914d\u51c6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,32,16)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,21,97)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,137,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,97,63)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,11,8)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,69,140)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,81,60)"
                        }
                    }
                },
                {
                    "name": "Camera\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,146,159)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,154,153)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7ade\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,11,76)"
                        }
                    }
                },
                {
                    "name": "11122M-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,1,89)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,78,47)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u6d4f\u89c8\u5668\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,4,9)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,98,35)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,52,8)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u5f00\u53d1\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,65,97)"
                        }
                    }
                },
                {
                    "name": "11416Z-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,113,42)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,98,140)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,71,128)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,15,0)"
                        }
                    }
                },
                {
                    "name": "11413B-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,57,143)"
                        }
                    }
                },
                {
                    "name": "PCG09-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,46,97)"
                        }
                    }
                },
                {
                    "name": "55414C-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,58,29)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,12,55)"
                        }
                    }
                },
                {
                    "name": "Algorithm Engineer \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,73,153)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,6,115)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,90,83)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08-\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,121,150)"
                        }
                    }
                },
                {
                    "name": "ARVR/\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,123,120)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,36,23)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,37,18)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,149,75)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,150,46)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,142,2)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u548c\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,154,76)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,103,45)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,82,87)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,52,140)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,151,156)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,44,103)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,112,13)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,135,50)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u770b\u70b9\u5546\u4e1a\u5316\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,141,78)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u533a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,124,110)"
                        }
                    }
                },
                {
                    "name": "npu\u67b6\u6784\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,91,47)"
                        }
                    }
                },
                {
                    "name": "\u8def\u7f51\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,155,33)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,53,122)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,58,119)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,135,68)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,29,160)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,79,146)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,46,109)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,132,105)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,89,7)"
                        }
                    }
                },
                {
                    "name": "11417L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,33,65)"
                        }
                    }
                },
                {
                    "name": "11312H-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,36,122)"
                        }
                    }
                },
                {
                    "name": "11413S-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,33,78)"
                        }
                    }
                },
                {
                    "name": "nlp/cv \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,132,31)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,49,133)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,21,158)"
                        }
                    }
                },
                {
                    "name": "SW-\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,42,76)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,88,106)"
                        }
                    }
                },
                {
                    "name": "11122K-LT-310-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,106,74)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,11,80)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,113,32)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,27,32)"
                        }
                    }
                },
                {
                    "name": "02426A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,57,54)"
                        }
                    }
                },
                {
                    "name": "\u63a5\u7ba1\u9884\u8b66\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,132,116)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\uff083D\u65b9\u5411\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,17,58)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,113,137)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,66,124)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,113,109)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,56,55)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,27,145)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,118,33)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,15,98)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,52,9)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,73,74)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76\u5b9a\u4f4d\u4e0e\u5730\u56fe\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,102,158)"
                        }
                    }
                },
                {
                    "name": "00239-\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,55,100)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,8,105)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,144,2)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,65,126)"
                        }
                    }
                },
                {
                    "name": "113195-\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,105,132)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,36,135)"
                        }
                    }
                },
                {
                    "name": "YAI-\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,6,96)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,42,49)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,101,111)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,158,29)"
                        }
                    }
                },
                {
                    "name": "KHQ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,35,56)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,90,140)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,4,104)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u4f53\u9a8c\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,126,141)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,60,139)"
                        }
                    }
                },
                {
                    "name": "05412O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,68,145)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,127,29)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,116,25)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,111,65)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,155,22)"
                        }
                    }
                },
                {
                    "name": "25317O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,32,30)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,37,110)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,124,36)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,105,48)"
                        }
                    }
                },
                {
                    "name": "AIOPS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,157,31)"
                        }
                    }
                },
                {
                    "name": "114114-\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,25,138)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,55,23)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,70,11)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u56fe\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,117,0)"
                        }
                    }
                },
                {
                    "name": "29912-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,55,71)"
                        }
                    }
                },
                {
                    "name": "AI\u8bad\u7ec3/\u63a8\u7406\u52a0\u901f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,137,132)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,39,80)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,155,61)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7ed3\u6784\u5316\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,52,144)"
                        }
                    }
                },
                {
                    "name": "1141BC-\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,74,125)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5f00\u53d1/unity/\u6d4b\u8bd5/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,54,131)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u5e26\u534f\u8bae\u548c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,82,61)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,117,86)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,114,131)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,12,72)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,147,33)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,17,33)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5e73\u53f0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,54,107)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,144,156)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u591a\u6a21\u6001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,63,25)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,139,5)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6a21\u578b\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,106,153)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,81,92)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,34,146)"
                        }
                    }
                },
                {
                    "name": "\u7269\u7406\u5c42\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,157,89)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,116,138)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,135,76)"
                        }
                    }
                },
                {
                    "name": "11122I-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,68,96)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,103,29)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,14,95)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,30,103)"
                        }
                    }
                },
                {
                    "name": "AIOPs\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,49,58)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,87,110)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,4,11)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u624b\u5199\u8bc6\u522b-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,150,117)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,94,1)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,88,87)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,24,79)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,102,92)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,102,72)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,93,131)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u5e73\u53f0-\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,82,141)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,0,18)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,86,73)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,73,16)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,90,45)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u5e02\u8ba1\u7b97\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,35,126)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,51,129)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,128,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,144,37)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,53,50)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,41,92)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,112,80)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,2,122)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,110,127)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,63,88)"
                        }
                    }
                },
                {
                    "name": "SJY-\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,40,69)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,141,52)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,95,60)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,66,107)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,59,148)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u4e09\u7ef4\u9ad8\u7cbe\u5efa\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,15,56)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,7,23)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,103,99)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,36,136)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,155,94)"
                        }
                    }
                },
                {
                    "name": "BK32CA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,134,127)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u603b\u76d1\uff08\u5927\u6570\u636e/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,53,87)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\uff08\u8bed\u8a00\u5efa\u6a21\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,74,112)"
                        }
                    }
                },
                {
                    "name": "AI\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,68,146)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,95,73)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,64,115)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,4,87)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,115,39)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,158,107)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,107,41)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,9,112)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,102,150)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,41,137)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,33,143)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,60,121)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,9,114)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,5,134)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,137,110)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,9,127)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,75,26)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,71,93)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,121,99)"
                        }
                    }
                },
                {
                    "name": "C++\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,85,101)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,60,83)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,87,134)"
                        }
                    }
                },
                {
                    "name": "55413N-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,94,49)"
                        }
                    }
                },
                {
                    "name": "SJY-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,117,82)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,146,62)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22/\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,136)"
                        }
                    }
                },
                {
                    "name": "11122N-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,62,22)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,152,98)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,59,82)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,144,4)"
                        }
                    }
                },
                {
                    "name": "\u4eca\u65e5\u5934\u6761-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,67,4)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,58,134)"
                        }
                    }
                },
                {
                    "name": "0241VF-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,134,32)"
                        }
                    }
                },
                {
                    "name": "114125-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,68,1)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,39,108)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,121,115)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u7fa4\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,15,133)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,24,0)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,78,48)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5149\u8c31\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,44,59)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,3,48)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,150,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ea7\u54c1\u7ecf\u7406(\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,18,73)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,57,83)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,68,49)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u9690\u79c1\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,22,52)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,42,159)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,67,132)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,38,155)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,37,62)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5065\u5eb7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,63,115)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,99,47)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,1,54)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,45,131)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,64,31)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,18,118)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,144,129)"
                        }
                    }
                },
                {
                    "name": "AI\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,96,64)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,142,71)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,140,56)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,2,93)"
                        }
                    }
                },
                {
                    "name": "1141BD-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,26,152)"
                        }
                    }
                },
                {
                    "name": "PCG-\u5e7f\u544a\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,6,72)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,121,11)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,116,121)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,145,88)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u683c\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,85,138)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,98,93)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,15,27)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,48,75)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,49,135)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,131,124)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,86,102)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,108)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,6,65)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe-SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,146,47)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,55,143)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,50,128)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,6,137)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,107,12)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u56ed\u62db\u8058-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,134,59)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,111,153)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,151,87)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,151,136)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,153,98)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7/\u97f3\u4e50\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,100,89)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,8,137)"
                        }
                    }
                },
                {
                    "name": "11318V-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,138,111)"
                        }
                    }
                },
                {
                    "name": "1131HA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,3,10)"
                        }
                    }
                },
                {
                    "name": "1121XJ-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,51,33)"
                        }
                    }
                },
                {
                    "name": "05415O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,137,99)"
                        }
                    }
                },
                {
                    "name": "11412I-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,7,60)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,54,28)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u533b\u7597\u641c\u7d22-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,106,145)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,67,87)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,149,154)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f81\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,29,10)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,155,5)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,4,35)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,12,112)"
                        }
                    }
                },
                {
                    "name": "\u6545\u969c\u8bca\u65ad(PHM)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,150,51)"
                        }
                    }
                },
                {
                    "name": "55413Q-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,152,21)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,64,94)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,145,27)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5de5\u7a0b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,85,112)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,124,114)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,16,90)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,28,127)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,4,83)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,114,132)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5b89\u5168\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,145,138)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08\uff08\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,10,40)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,57,140)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,22,44)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,70,69)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,84,49)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,0,74)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,56,52)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22&\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,123,28)"
                        }
                    }
                },
                {
                    "name": "\u521d\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,132,142)"
                        }
                    }
                },
                {
                    "name": "ASR/TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,32,120)"
                        }
                    }
                },
                {
                    "name": "0241UC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,27,51)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,147,58)"
                        }
                    }
                },
                {
                    "name": "11312J-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,137,60)"
                        }
                    }
                },
                {
                    "name": "25318B-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,82,103)"
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
                "\u89c6\u89c9\u7b97\u6cd5",
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
        chart_cc514c2d85614b70b5b3f1dc4a6b8749.setOption(option_cc514c2d85614b70b5b3f1dc4a6b8749);
    </script>
                <div id="ed9bab0f4392473095092a343e272434" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ed9bab0f4392473095092a343e272434 = echarts.init(
            document.getElementById('ed9bab0f4392473095092a343e272434'), 'white', {renderer: 'canvas'});
            
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
    
        var option_ed9bab0f4392473095092a343e272434 = {
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
                    "value": 234,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,152,148)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 119,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,149,101)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 114,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,19,75)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 107,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,106,79)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,57,27)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,106,11)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,126,87)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,60,39)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,90,19)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,0,17)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,111,145)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,22,31)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,119,138)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,102,102)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,6,133)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,27,102)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,152,66)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,86,35)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,74,159)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,68,1)"
                        }
                    }
                },
                {
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,75,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,104,139)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,14,36)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,140,14)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,77,73)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,10,3)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,78,55)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,35,92)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,26,123)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,38,113)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,22,114)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,123,5)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,58,144)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,153,52)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,146,153)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,7,36)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,131,140)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,101,3)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,14,82)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,155,91)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,145,19)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,80,26)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,25,17)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,31,6)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,38,100)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,117,100)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,93,26)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,2,7)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,91,35)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,16,48)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,11,49)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,104,28)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,133,77)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,60,113)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,31,36)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,155,148)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,31,88)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,149,145)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,85,86)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,70,12)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,152,135)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,92,22)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,103,55)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,94,132)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,95,91)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,46,39)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,66,65)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u4f18\u79c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,77,117)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,41,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,26,73)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,55,7)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,45,59)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,11,121)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,123,158)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,136,69)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,108,46)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,52,156)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,94,98)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,144,67)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,82,128)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,59,140)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,84,58)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,21,78)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,146,57)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,21,85)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,92,113)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,119,19)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,152,77)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,52,145)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,129,91)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,50,122)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,60,145)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,70,76)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,68,91)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,129,11)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,50,99)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,81,149)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,106,120)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,82,6)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,72,59)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,0,110)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,16,148)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,1,44)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5e74\u7ec8",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,57,20)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,51,30)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,88,49)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,18,52)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,133,134)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,160,15)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,64,89)"
                        }
                    }
                },
                {
                    "name": "\u6025\u901f\u6210\u957f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,80,82)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,72,61)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,158,34)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,13,116)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,124,107)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,14)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,32,130)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,146,46)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929\u884c\u4e1a\u524d\u666f\u826f\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,1,53)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,57,16)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,55,146)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,17,6)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,56,28)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,134,56)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,31,103)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,117,148)"
                        }
                    }
                },
                {
                    "name": "\u8bf1\u4eba\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,52,141)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,130,53)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,23,50)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,103,30)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,111,150)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,70,123)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,57,18)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,133,81)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,42,9)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,23,9)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,135,27)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,18,98)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,56,12)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f73",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,134,93)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,1,94)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,128,14)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4e2d\u5fc3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,69,140)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,96,129)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,85,135)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,124,73)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,81,76)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,101,68)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,57,27)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,36,106)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,69,69)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,6,134)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,140,59)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5f00\u516c\u6b63",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,150,24)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,93,52)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,110,105)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,14,52)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u8865\u5145",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,139,76)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,77,1)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,72,73)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,130,35)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,65,134)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,47,67)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,39,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,21,135)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,125,80)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,8,48)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,78,47)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,61,21)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,57,155)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,8,0)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,63,26)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,15,58)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,56,104)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,38,146)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,120,89)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,88,51)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,97,152)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,125,39)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,37,40)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u53d1\u5c55\u7a7a\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,126,153)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,17,106)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,43,160)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,44,0)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,109,131)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,132,100)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,158,150)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,86,16)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,24,67)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,82,67)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,8,99)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,135,89)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,58,66)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,78,33)"
                        }
                    }
                },
                {
                    "name": "8\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,60,81)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,47,133)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,128,67)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,71,9)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,38,137)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,159,157)"
                        }
                    }
                },
                {
                    "name": "\u843d\u6237\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,84,87)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,106,21)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,74,17)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,129,103)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,104,74)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,19,125)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,5,65)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,9,1)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,141,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,99,137)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,38,40)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,46,74)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u652f\u6301\u7ed9\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,98,107)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,147,77)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,152,10)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,64,62)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,19,50)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,0,95)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u9636\u8dc3\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,10,0)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,133,8)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,0,141)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,125,31)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,100,89)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,6,15)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,33,58)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,43,2)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,60,147)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,85,152)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,44,145)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u574718\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,77,147)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,24,46)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,127,32)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,65,118)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u7b79\u5907",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,66,121)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,9,49)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,36,4)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,130,146)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,68,51)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,89,133)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,22,105)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,65,129)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,89,125)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u52b1\u5236",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,98,160)"
                        }
                    }
                },
                {
                    "name": "\u5bbf\u820d\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,46,40)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,6,146)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,93,31)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,56,10)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u5b9e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,78,57)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,7,138)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u56db\u6b21\u8bc4\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,31,44)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u5f00\u653e\u73af\u5883",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,64,101)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5\u6838\u5fc3\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,45,41)"
                        }
                    }
                },
                {
                    "name": "\uff0858\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,39,27)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,80,109)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,59,102)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,152,45)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u6c1b\u56f4\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,25,45)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,18,69)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,81,35)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,44,152)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,45,17)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,122,117)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,121,70)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,92,65)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,93,100)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,140,58)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,75,47)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,40,50)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,3,24)"
                        }
                    }
                },
                {
                    "name": "\u65e0996",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,40,111)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,114,60)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,17,102)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,14,98)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u4e1a\u52a1\u573a\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,88,62)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,60,132)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,83,23)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,153,25)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,43,85)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,115,148)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,144,54)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,42,70)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,66,87)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,123)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,85,2)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,70,5)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7cbe\u6e5b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,75,135)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,156,86)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,39,105)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,53,50)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,27,145)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,32,16)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,29,103)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,37,128)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,15,90)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,39,125)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,64,111)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,159,75)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,79,15)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,147,25)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,88,46)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,49,29)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,25,28)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,107,129)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,34,100)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,91,23)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,25,62)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,105,131)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,105,117)"
                        }
                    }
                },
                {
                    "name": "AI\u82af\u7247",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,31,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,9,123)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,154,18)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,68,94)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,141,107)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u52b2\u535a\u58eb\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,102,156)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,110,63)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,154,66)"
                        }
                    }
                },
                {
                    "name": "\u7845\u8c37\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,115,62)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,88,104)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u63d0\u4f9b\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,38,131)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,23,108)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u6307\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,9,51)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,134,102)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,103,117)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,115,15)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,15,36)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,118,138)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,150,86)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,0,67)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,76,4)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0a\u5e02\u9884\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,68,35)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5730\u5b66\u751f\u5b9e\u4e60\u6709\u4f4f\u5bbf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,132,14)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,35,90)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u578b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,90,28)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u521b\u65b0\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,113,46)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f/\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,137,70)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u751f\u65e5\u8282\u5047\u65e5\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,153,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u957f\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,154,77)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,8,16)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,68,37)"
                        }
                    }
                },
                {
                    "name": "*\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,58,25)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,126,66)"
                        }
                    }
                },
                {
                    "name": "AI\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,107,55)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,3,112)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,65,29)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,69,94)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,52,5)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,45,6)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u521b\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,34,19)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,39,18)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,36,113)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,27,7)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u6fc0\u60c5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,54,56)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,149,25)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,87,57)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9510\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,58,98)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,16,4)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,144,54)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,74,103)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,16,51)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,1,89)"
                        }
                    }
                },
                {
                    "name": "80%\u8f6c\u6b63\u7387",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,142,88)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5956\u91d1+\u80a1\u6743/\u671f\u6743\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,75,69)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7ebf\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,73,147)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236\u5ea6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,118,159)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,62,139)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,111,51)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,116,91)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,106,132)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,20,33)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,82,39)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,20,79)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,120,106)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,5,13)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,112,74)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1\u7cfb\u7edf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,19,35)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,26,76)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,28,96)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u4f18\u6e25",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,74,37)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,153,85)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,153,144)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,55,131)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,131,89)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,143,34)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,109,143)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,135,31)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,144,52)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,110,60)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,23,0)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,63,45)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,152,46)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,2,98)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,41,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,17,74)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,131,101)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5496\u5561",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,32,144)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,62,38)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,2,37)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,102,124)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,64,79)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,158,122)"
                        }
                    }
                },
                {
                    "name": "*\u6708\u5ea6\u7ee9\u6548\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,11,45)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8d85\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,148,43)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,39,95)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u65b0\u5174\u9886\u57df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,113,10)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u901a\u8054\u6570\u636e\u8054\u5408\u62db\u8058",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,27,116)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u6587\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,71,73)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,49,49)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185TOP3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,98,74)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,3,113)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,154,92)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,84,89)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,109,139)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,49,43)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,95,48)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,78,157)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,122,35)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,71,127)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,107,86)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,42,30)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,52,145)"
                        }
                    }
                },
                {
                    "name": "\u516d\u65e5\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,117,18)"
                        }
                    }
                },
                {
                    "name": "\u989c\u503c\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,89,59)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,143,154)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,151,137)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,68,137)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,148,143)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u516c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,76,19)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,38,128)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,39,127)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,66,93)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,54,45)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,1,119)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,1,4)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,91,19)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,152,21)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u5e95\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,60,36)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,15,57)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,17,62)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,66,155)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u5730\u94c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,83,10)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,159,114)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,131,92)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,62,55)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1/\u5b63\u5ea6\u5956/\u5e26\u85aa\u5e74\u5047/\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,155,112)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u9886\u5148\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,59,80)"
                        }
                    }
                },
                {
                    "name": "6\u96692\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,0,119)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,47,18)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,127,67)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u8005\u7ed9\u4e0e\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,125,33)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u6709\u5b9e\u529b\u7684\u5927\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,16,140)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u7a7a\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,96,109)"
                        }
                    }
                },
                {
                    "name": "\u671f\u5f85\u60a8\u7684\u52a0\u5165",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,127,101)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,124,11)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,141,156)"
                        }
                    }
                },
                {
                    "name": "IOT\u9886\u5148\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,51,59)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,1,54)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,9,80)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,81,113)"
                        }
                    }
                },
                {
                    "name": "16\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,124,43)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,25,19)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,128,158)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,75,99)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,145,141)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,115,63)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,13,0)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,112,131)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,61,60)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u9910\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,91,69)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,113,30)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u8d8b\u52bf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,35,20)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,104,12)"
                        }
                    }
                },
                {
                    "name": "Geek",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,151,104)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,85,119)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u6c1b\u56f4\u4ff1\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,105,16)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,113,148)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5177\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u5f85\u9047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,104,16)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,105,30)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,116,76)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,9,147)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,65,74)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,148,109)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4e2d\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,5,81)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,33,50)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,77,113)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u51fa\u6d77\u524d\u4e09",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,131,77)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,39,128)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,12,143)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,106,127)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,92,37)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,122,12)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,155,118)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,117,117)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,56,47)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,153,60)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,37,158)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,130,121)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,34,33)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,125,17)"
                        }
                    }
                },
                {
                    "name": "\u745c\u4f3d\u5065\u8eab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,56,81)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,159,48)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,120,57)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8bafC\u8f6e\u9886\u6295",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,68,84)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,61,157)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,127,149)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,47,36)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51\u53cc\u8de8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,68,129)"
                        }
                    }
                },
                {
                    "name": "\u9910\u901a\u8baf\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,109,131)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,59,62)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,87,31)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,57,113)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,128,46)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,53,142)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e24\u4f4d\u79d1\u5b66\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,56,26)"
                        }
                    }
                },
                {
                    "name": "**\u533b\u9662\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,151,60)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237\u7684\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,141,48)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df10+\u7ecf\u9a8c\u7b97\u6cd5\u548cC++\u7684\u53cc\u5bfc\u5e08\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,122,58)"
                        }
                    }
                },
                {
                    "name": "\u6709\u826f\u597d\u7684\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,34,48)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,79,34)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u9988\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,97,25)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u4e2a\u5c97\u4f4d\u6210\u5c31\u4e00\u756a\u4e8b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,81,127)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,41,37)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,2,28)"
                        }
                    }
                },
                {
                    "name": "\u7f34\u7eb3\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,92,82)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5f71\u50cf\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,110,25)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,67,137)"
                        }
                    }
                },
                {
                    "name": "\u6210\u719f\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,125,137)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,150,57)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u578b\u7ec4\u7ec7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,24,77)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,98,124)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,159,86)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,65,102)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669\u7b49\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,7,12)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u7f34\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,32,76)"
                        }
                    }
                },
                {
                    "name": "\u603b\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,20,85)"
                        }
                    }
                },
                {
                    "name": "\u5929\u9ad8\u4efb\u9e1f\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,159,129)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,5,64)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,157,88)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d\u79d1\u6280\u5934\u90e8\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,12,116)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5148\u7684\u4eba\u5de5\u667a\u80fd\u5b66\u4e60\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,142,146)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,6,59)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,44,101)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u754c\u4e0e\u5b66\u672f\u754c\u76f8\u7ed3\u5408\u7684\u6700\u4f73\u9635\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,108,97)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,115,129)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,120,121)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,61,71)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,23,41)"
                        }
                    }
                },
                {
                    "name": "\u643a\u624b\u594b\u6597\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,5,37)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,0,75)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,43,96)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,74,86)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,7,3)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u4e1a\u52a1\u5b89\u5168\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,4,82)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,110,149)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,18,69)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,118,143)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,101,21)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,83,23)"
                        }
                    }
                },
                {
                    "name": "\u5076\u5c14\u52a0\u73ed\u8c03\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,120,87)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,108,152)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,1,47)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,157,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,152,50)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u805a\u9910~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,154,6)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,130,11)"
                        }
                    }
                },
                {
                    "name": "\u590d\u6742\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,53,121)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,99,68)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u81f4\u8212\u9002\u7684\u529e\u516c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,153,107)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,139,12)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f\u5e26\u85aa\u5e74\u5047\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,88,100)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,109,73)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u5e26\u65b0\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,5,114)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,120,29)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,12,155)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,95,49)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u4e0a\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,33,120)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u8d44\u672c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,135,6)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u8bd5\u7528\u671f\u540c\u85aa\u4e94\u9669\u4e00\u91d1\u957f\u671f\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,41,107)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u590d\u6742",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,14,74)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,4,2)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,87,69)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53e3\u5348\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,124,140)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u9886\u57df\u7814\u53d1\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,43,139)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,106,143)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u6211\u53d1\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,60,91)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,146,0)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c0f\u5468",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,64,128)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u7684\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,1,154)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,100,91)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,139,42)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,31,77)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u5019\u9009\u4eba\u53ef\u4ee5\u6210\u4e3a\u6280\u672f\u5408\u4f19\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,94,106)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,82,81)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,17,80)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u77bb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,26,70)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7528\u8fd0\u7b79\u4f18\u5316\u77e5\u8bc6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,83)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,1,30)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,39,62)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,49,2)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u4ea4\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,36,55)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,32,69)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,85,122)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,112,129)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,91,62)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,149,135)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,51,2)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,141,70)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,155,126)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,13,67)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,41,65)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,50,14)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,128,138)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u6216\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,63,59)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,26,35)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,79,48)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,134,30)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,93,22)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,82,35)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,134,70)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,84,143)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,53,43)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,19,118)"
                        }
                    }
                },
                {
                    "name": "\u83b7\u591a\u5bb6**\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,4,138)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u4f18\u5f02\u7684\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,16,99)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,105,27)"
                        }
                    }
                },
                {
                    "name": "\u811a\u8e0f\u5b9e\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,24,27)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,70,60)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,130,31)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u679c\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,62,78)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,108,113)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,158,75)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,36,77)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,3,3)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u54c8\u5570\u51fa\u884c\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,151,42)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,53,136)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u5927\u4f6c\u4e00\u8d77\u53c2\u52a0\u56fd\u9645\u9876\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,90,79)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,37,29)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,100,99)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,125,13)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u6bcf\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,34,40)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,151,70)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,91,148)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,91,114)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,146,100)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,89,112)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u5f88\u5f3a\u7684\u540c\u4e8b\u4e00\u8d77\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,28,79)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u770b\u597d\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,143,149)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6742\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,99,43)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,17,58)"
                        }
                    }
                },
                {
                    "name": "\u91c7\u7f16\u5236\u64ad\u5b58",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,156,72)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,20,60)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,28,106)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u7cbe\u6e5b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,63,90)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,92,65)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,121,148)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,45,22)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,49,74)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,154,85)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,24,44)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,20,34)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,124,159)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,83,107)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u8d77\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,3,112)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u52a0\u73ed\u4e09\u500d\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,17,113)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,40,78)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,42,86)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,62,99)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,113,48)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,7,159)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a\u6838\u5fc3\u4ea7\u54c1\uff08\u70ed\u641c\u699c\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,128,151)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u673a\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,129,96)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7814\u53d1\u4eba\u6570\u5360\u6bd470%",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,98,135)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b66\u4e60\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,110,79)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,43,123)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,12,155)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,107,89)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u798f\u5229\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,39,109)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,84,62)"
                        }
                    }
                },
                {
                    "name": "\u548c\u8c10\u7684\u56e2\u961f\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,40,98)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,4,87)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,148,51)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,159,104)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,61,37)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u9f50\u805a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,151,148)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,66,80)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,75,30)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,95,144)"
                        }
                    }
                },
                {
                    "name": "\u3010\u8304\u5b50\u5feb\u4f20\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,139,155)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,63,128)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,151,101)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,53,73)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,113,151)"
                        }
                    }
                },
                {
                    "name": "\u6587\u827a\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,63,89)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,54,123)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,101,142)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,37,18)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,105,90)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,96,57)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u98ce\u63a7\u5782\u76f4\u9886\u57df\u6df1\u5ea6\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,81,147)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,81,49)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,3,113)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148\u5546\u7528\u670d\u52a1\u673a\u5668\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,68,40)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u884c\u4e1a\u524d\u666f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,80,78)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u826f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,158,9)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,125,4)"
                        }
                    }
                },
                {
                    "name": "\u5177\u89c4\u6a21\u7684\u5927\u6570\u636e\u5e73\u53f0\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,33,94)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,57,122)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,139,146)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u65b0\u9896",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,149,90)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916SaaS\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,56,10)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1\u5168\u8d44\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,63,104)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u6da8\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,145)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,70,57)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,103,74)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,51,102)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,9,35)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,33,131)"
                        }
                    }
                },
                {
                    "name": "\u6574\u4f53\u89e3\u51b3\u65b9\u6848\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,152,157)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,34,34)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,30,112)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0/\u5f39\u6027\u4e0a\u4e0b\u73ed/\u5e74\u7ec8\u7ee9\u6548/\u514d\u8d39\u5348\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,147,81)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,93,60)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,13,107)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,142,14)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u540d\u6821\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,125,155)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,66,83)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,98,30)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u7b97\u6cd5\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,10,114)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,123,40)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,111,81)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,154,22)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,121,10)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,148,94)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,46,149)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,155,1)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,128,91)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80a1\u4e1c\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,69,1)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,114,99)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,76,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d1f\u8d23\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,91,112)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,20,114)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,7,102)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,13,24)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,145,47)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,44,39)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,87,60)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,64,57)"
                        }
                    }
                },
                {
                    "name": "\u7528\u524d\u6cbf\u6280\u672f\u53d8\u9769\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,151,76)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4eba\u624d\u4f4f\u623f\u63d0\u4f9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,48,105)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,160,126)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,40,10)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,62,149)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,123,2)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,116,41)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,133,102)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u4f5c\u4e3a\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,69,19)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,70,87)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,123,74)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,87,79)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,8,104)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,51,115)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,47,87)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,93,146)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,108,71)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u725b\u4e91\u96c6\u9879\u76ee\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,149,30)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,18,150)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,139,77)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5\u9a71\u52a8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,43,92)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNic",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,64)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,19,56)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,116,8)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u6709\u529b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,8,156)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,63,101)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,134,45)"
                        }
                    }
                },
                {
                    "name": "\u6ce8\u91cd\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,146,63)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,126,75)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,50,53)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e0e\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,23,22)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,121,46)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,18,120)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,26,16)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d8520\u5e74\u76f8\u5173\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,140,4)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,157,75)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,19,59)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,73,112)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,75,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,47,115)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,56,121)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,65,24)"
                        }
                    }
                },
                {
                    "name": "CBA\u660e\u661f\u521b\u4e1a\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,13,158)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,101,116)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530CBD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,132,25)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,35,133)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7b49\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,114,46)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,89,105)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5f02\u8005\u53ef\u8f6c\u6821\u62db\u6b63\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,64,50)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,140,95)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,130,94)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,127,8)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,100,6)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,29,125)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,32,140)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,94,136)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,72,84)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,89,155)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,48,117)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,49,133)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5148\u8fdb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,80,158)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,121,141)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,31,55)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,44,32)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,84,36)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,143,103)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,51,70)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,64,66)"
                        }
                    }
                },
                {
                    "name": "\u5404\u7c7b\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,93,152)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,87,27)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,101,58)"
                        }
                    }
                },
                {
                    "name": "\u5df2\u83b7\u591a\u5bb6\u4e00\u7ebfVC\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,129,96)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,57,116)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u7ee9\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,123,115)"
                        }
                    }
                },
                {
                    "name": "12%\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,34,112)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u9971\u6ee1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,23,149)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,62,36)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,121,148)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,50,22)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,128,56)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,33,24)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,42,70)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,122,112)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,96,25)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,131,48)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e00\u6863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,122,0)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5bfc\u5e26\u961f\u7684\u6df1\u5ea6\u5b66\u4e60\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,84,128)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u573a\u9762\u8bd5\u6d41\u7a0b\u4e00\u6b21\u8d70\u5b8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,154,29)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,1,11)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,156,135)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,154,156)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,15,26)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,140,56)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,81,130)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,138,152)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u505c\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,46,116)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4eba\u5458300\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,86,8)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,76,148)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,73,97)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u6ee1\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,27,111)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,20,16)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,121,107)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,132,1)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u81ea\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,81,66)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,81,20)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,138,126)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,138,82)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u6709\u7231\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,99,71)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,69,81)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,118,116)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,77,150)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,156,26)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,159,125)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u516c\u53f8\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,38,56)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,76,155)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,7,38)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,132,3)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,4,108)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,112,154)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,143,75)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,40,71)"
                        }
                    }
                },
                {
                    "name": "\u9519\u8fc7\u4e8610\u5e74\u7684\u624b\u6dd8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,52,25)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,30,128)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,148,26)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,151,148)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,150,52)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,34,61)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,28,60)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,35,125)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56e2\u961f\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,113,70)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6d3b\u5343\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,150,128)"
                        }
                    }
                },
                {
                    "name": "1.\u56e2\u961f\u4e1a\u52a1\u7d27\u8ddf\u96c6\u56e2\u7684\u4e1a\u52a1\u76ee\u6807",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,71,69)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,26,2)"
                        }
                    }
                },
                {
                    "name": "\u56db\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,21,88)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4up",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,30,57)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,142,141)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u533b\u7597\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,146,31)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,18,30)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0d\u5dee\u94b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,123,151)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,95,133)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,140,13)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,21,118)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,58,108)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6837\u5316\u7684\u5b66\u4e60\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,35,135)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e00\u4ee3\u6587\u5a31\u98ce\u53e3\u9886\u822a\u8005",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,149,125)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21review\u664b\u5347\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,30,50)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,158,150)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,103,97)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,50,117)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,85,92)"
                        }
                    }
                },
                {
                    "name": "\u65e0007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,30,145)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,150,48)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,131,110)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,1,130)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,120,10)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,29,148)"
                        }
                    }
                },
                {
                    "name": "C\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,75,54)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u63a5\u89e6\u4e1a\u754c\u6700\u524d\u6cbf\u4eba\u5de5\u667a\u80fd\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,39,69)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,87,126)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u6280\u672f\u4ea4\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,1,8)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,144,45)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,130,147)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,147,67)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,97,52)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,23,105)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,114,49)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,160,60)"
                        }
                    }
                },
                {
                    "name": "\u5171\u521b\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,30,154)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,118,143)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,137,29)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,90,136)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,81,118)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,145,121)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,17,62)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,91,7)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,43,27)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,85,87)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,160,14)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,146,58)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,70,31)"
                        }
                    }
                },
                {
                    "name": "\u4eab\u6709\u80a1\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,107,119)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,81,76)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,104,125)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u7684\u56e2\u961f\u5de5\u7a0b\u548c\u7b97\u6cd5\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,88,116)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,1,31)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,102,75)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,10,46)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,125,102)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,131,114)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,11,65)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,140,129)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,11,104)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,143,109)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,95,24)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,11,129)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,88,101)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,21,92)"
                        }
                    }
                },
                {
                    "name": "14-18\u85aa+\u4e30\u539a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,48,24)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,111,140)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,90,36)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u81ea\u6211\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,69,138)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,93,26)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,149,10)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,67,63)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,155,31)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,58,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u80fd\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,53,99)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,129,84)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,47,17)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u767e\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,2,25)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6e\u5c97\u6216\u8f6c\u5c97\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,60,3)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,134,121)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,118,35)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,24,16)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,25,105)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5f88\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,5,33)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,138,99)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,139,61)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,66,81)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,147,74)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,152,25)"
                        }
                    }
                },
                {
                    "name": "\u65af\u5766\u798f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,89,102)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u975e\u5e38\u597d\u3002\u5458\u5de5\u85aa\u8d44\u798f\u5229\u5f88\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,131,83)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,47,36)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe\u6838\u5fc3\u4e1a\u52a1\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,58,1)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u5927\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,71,145)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,99,3)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,52,19)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,57,150)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,159,62)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,148,39)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,23,154)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8def\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,9,48)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,51,123)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,81,58)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,42,133)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,2,65)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,82,118)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u591a\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,133,85)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,34,115)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,112,150)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4e07DAU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,37,117)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,48,101)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,47,21)"
                        }
                    }
                },
                {
                    "name": "\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,93,94)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,110,60)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u5458\u5de5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,113,0)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u5236\u8f83\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,70,3)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,144,29)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,66,54)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u57fa\u56e0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,30,109)"
                        }
                    }
                },
                {
                    "name": "\u7535\u89c6\u53f0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,76,152)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d\u9886\u57df\u524d\u6cbf\u7b97\u6cd5\u7814\u7a76\u548c\u5b9e\u73b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,23,1)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,62,8)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,68,156)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,91,157)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,9,147)"
                        }
                    }
                },
                {
                    "name": "\u624e\u624e\u5b9e\u5b9e\u505a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,51,150)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,17,67)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u4e24\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,143,132)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,60,92)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,36,44)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,95,35)"
                        }
                    }
                },
                {
                    "name": "\u6784\u5efa\u4eba\u7c7b\u865a\u62df\u4e16\u754c\u65b0\u4f53\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,56,145)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,157,138)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,42,77)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,63,141)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,27,110)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,50,68)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,37,93)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,11,80)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,12,147)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u4e0e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,91,63)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,42,66)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,95,36)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u89c4\u8303",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,27,127)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,49,97)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,104,23)"
                        }
                    }
                },
                {
                    "name": "\u5373\u5c06\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,64,19)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,135,61)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,62,116)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,60,70)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,30,6)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,117,19)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,80,55)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u5e73\u53f0\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,120,10)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u83b7\u5f97\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,24,83)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,38,134)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,96,142)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,38,143)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,73,92)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,8,23)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,106,59)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,76,82)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,39,114)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,48,17)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,4,117)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u7b49\u884c\u4e1a\u6700\u4f18\u79c0\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,107,153)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,142,148)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,122,60)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u798f\u5229\u5e74\u5ea6\u4f53\u68c0\u52a0\u73ed\u8865\u52a9\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,135,63)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,49,127)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,147,17)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,57,159)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,6,16)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u7ee9\u4f18\u79c0+\u5e74\u7ec8\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,109,29)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,98,64)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u676d\u5dde\u5b9e\u5728\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,62,26)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,57,47)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,99,37)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,42,92)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u5927\u4f6c\u5e26\u4f60\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,132,105)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5229\u4e8e\u53d1\u8bba\u6587",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,7,134)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,7,52)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,21,29)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e94\u8fbe\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,122,143)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u8fd1\u767e\u4ebf\u7f8e\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,38,159)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,143,17)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,53,106)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u65e5\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,116,31)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f83\u597d\u7684\u8d44\u6e90\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,138,116)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,150,119)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,31,109)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,152,50)"
                        }
                    }
                },
                {
                    "name": "\u9876\u683c\u4f4f\u623f\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,12,53)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,144,23)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,58,116)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,26,35)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,76,23)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,52,1)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,144,140)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,71,83)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,64,121)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,90,51)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u5168\u7403\u5316\u548c\u591a\u6d3b\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,134,74)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,60,105)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403**\u79d1\u5b66\u5bb6\u8ddf\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,14,131)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,90,19)"
                        }
                    }
                },
                {
                    "name": "6\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,32,132)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,110,95)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,56,135)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,41,71)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,132,73)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,7,38)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,75,139)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,53,131)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u7d22\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,5,121)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,155,76)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,148,5)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u5173\u8054\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,150,121)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,140,103)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,156,142)"
                        }
                    }
                },
                {
                    "name": "\u653f\u5e9c\u91cd\u70b9\u652f\u6301\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,32,147)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,128,86)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,36,33)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u81ea\u6211",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,47,116)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,140,55)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,84,12)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,3,31)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,143,59)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,126,86)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,109,120)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u5907\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,58,17)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9879\u76ee\u7814\u7a76\u524d\u6cbf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,11,132)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,152,126)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u7ea7\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,141,160)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u60a8\u52a0\u5165\u4e00\u70b9\u5927\u5bb6\u5ead~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,21,40)"
                        }
                    }
                },
                {
                    "name": "CTO\u7b97\u6cd5\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,13,59)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u50478\u5929\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,116,38)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,123,23)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,148,96)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,137,24)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,20,66)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,121,90)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,146,16)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u5047\u65e5\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,141,52)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,159,37)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,140,107)"
                        }
                    }
                },
                {
                    "name": "AI\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,21,92)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,94,151)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u5bfc\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,58,92)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u548c\u5e26\u85aa\u75c5\u5047\u540415\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,37,137)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,48,5)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,132,48)"
                        }
                    }
                },
                {
                    "name": "\u3010\u611f\u77e5\u9636\u8dc3\u3011\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,39,66)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,148,18)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,153,66)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u96c6\u7fa4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,27,93)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,8,0)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5c0f\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,61,154)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,128,153)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,87,132)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,113,85)"
                        }
                    }
                },
                {
                    "name": "Pro\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,28,118)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,156,11)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,81,109)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,152,21)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,107,118)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u9690\u5f62**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,72,31)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,52,98)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,18,159)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,85,31)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,121,10)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,50,118)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\uff1a\u957f\u671f\u6280\u672f\u79ef\u6dc0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,44,88)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,82,51)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u548c\u80fd\u529b\u6210\u957f\u6027\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,16,72)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,121,152)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,93,148)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,107,138)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,155,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,147,124)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u4eba\u5458\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,82,14)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f118\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,85,9)"
                        }
                    }
                },
                {
                    "name": "007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,27,95)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53/\u7535\u89c6\u53f0/\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,100,52)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5c0f\u800c\u7cbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,158,159)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,21,83)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,121,147)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u8d44\u6e90\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,28,19)"
                        }
                    }
                },
                {
                    "name": "\u5171\u540c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,148,125)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u52a8\u4e2d\u56fd\u533b\u7597\u6539\u53d8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,124,50)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,121,148)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,35,87)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,113,99)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u63a5\u8ddf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,110,21)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,95,69)"
                        }
                    }
                },
                {
                    "name": "NICE\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,123,8)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,109,49)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,20,59)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5b9e\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,48,2)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,76,105)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,116,88)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,151,31)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df\u7684\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,52,67)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u8d5b\u83b7\u5956\u7ecf\u9a8c\u4f18\u5148\u8003\u8651",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,28,141)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,56,67)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u6c7d\u8f66\uff08\u730e\u5934\u5c97\u4f4d\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,93,87)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,148,28)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,132,87)"
                        }
                    }
                },
                {
                    "name": "7\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,37,3)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,128,113)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,79,155)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,137,124)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,136,124)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,14,146)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,97,23)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,122,152)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,122,29)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,138,29)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7f51\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,12,143)"
                        }
                    }
                },
                {
                    "name": "\u5305\u53cc\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,11,13)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u6c1b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,92,141)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,98,124)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f14\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,25,100)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,57,121)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u538b\u529b\u5c0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,3,53)"
                        }
                    }
                },
                {
                    "name": "**\u6295\u8d44\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,122,63)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,109,150)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,160,129)"
                        }
                    }
                },
                {
                    "name": "\u7075\u6d3b\u5de5\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,99,103)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,149,109)"
                        }
                    }
                },
                {
                    "name": "\u9662\u58eb\u5e26\u961f\u53c2\u4e0e\u9ad8\u6821\u8054\u5408\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,133,136)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,53,35)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,160,50)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,143,35)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,127,74)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,89,115)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u5feb\u624b\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,63,41)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,154,55)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8bf1\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,89,135)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,92,80)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,31,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,124,1)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,87,1)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,66,36)"
                        }
                    }
                },
                {
                    "name": "\u9769\u65b0\u7684\u9879\u76ee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,87,23)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,59,118)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,129,135)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,97,116)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,110,0)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8d85\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,133,83)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,102,124)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u7a0b\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,131,26)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,137,52)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,141,113)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,155,83)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,63,54)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,54,108)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u6e20\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,87,2)"
                        }
                    }
                },
                {
                    "name": "\u6709\u66f4\u9ad8\u66f4\u5927\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,34,8)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,52,143)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,117,38)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u6caa\u676d\u5747\u6709hc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,96,69)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,42,110)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9614\u51ed\u9c7c\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,130,14)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,119,120)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,111,153)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,23,151)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,69,33)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,19,43)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,1,98)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,73,14)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,100,101)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,63,148)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,24,52)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,9,127)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,94,26)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,5,148)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u540c\u884c\u4e1a\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,72,13)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,135,7)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,68,21)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,20,111)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,58,40)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,160,76)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,7,82)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,53,100)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1aAI\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,150,19)"
                        }
                    }
                },
                {
                    "name": "0-1\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,83,58)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6709\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,98,13)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,17,34)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,34,5)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79ef\u91d1\u5168\u989d\u6700\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,45,2)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,94,97)"
                        }
                    }
                },
                {
                    "name": "\u522b\u518d\u9519\u8fc7Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,120,18)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,97,80)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,143,82)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6587\u6863\u968f\u4fbf\u770b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,82,30)"
                        }
                    }
                },
                {
                    "name": "\u961f\u53cb\u5948\u65af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,127,47)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,59,138)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,31,28)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,47,111)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,127,23)"
                        }
                    }
                },
                {
                    "name": "\u80cc\u666f\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,22,80)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,9,80)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,58,106)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5bfc\u8d2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,31,153)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,117,157)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,71,26)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,114,14)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,39,140)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,0,160)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,151,105)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,91,115)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,135,65)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,87,122)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,78,146)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u5883\u5962\u4f88\u54c1\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,129,83)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,61,91)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,114,87)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,25,140)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,21,10)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,72,69)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,109,57)"
                        }
                    }
                },
                {
                    "name": "\u5145\u6ee1\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,38,64)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u6027\u7684\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,137,127)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,159,14)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,95,47)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,71,127)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,87,81)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u8d70\u8fdb\u5343\u5bb6\u4e07\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,26,62)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,89,5)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,128,158)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,47,79)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,120,99)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,78,10)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,125,98)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,71,156)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,40,5)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,43,38)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,117,97)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,46,142)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,46,123)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,49,2)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,149,2)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,19,141)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,23,128)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,30,57)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,87,58)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbfAR\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,11,122)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53e3\u7891\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,105,148)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u81ea\u52a9\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,119,75)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,152,158)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,49,23)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,91,6)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u6700\u5927\u4e09\u65b9\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,22,24)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,54,133)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u5747\u4e3a\u81ea\u52a8\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,25,39)"
                        }
                    }
                },
                {
                    "name": "Mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,81,55)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,106,57)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,97,109)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,45,140)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,145,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,29,84)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9738",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,86,123)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,133,12)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,73,67)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,154,80)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,101,92)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u804c\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,23,155)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,106,86)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,112,122)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,149,76)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,28,34)"
                        }
                    }
                },
                {
                    "name": "15-20\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,52,63)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,110,88)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,111,15)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,79,17)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,59,69)"
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
        chart_ed9bab0f4392473095092a343e272434.setOption(option_ed9bab0f4392473095092a343e272434);
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
