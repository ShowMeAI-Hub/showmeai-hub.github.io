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
            <button class="tablinks" onclick="showChart(event, '283f23ad4b264fb9bd15f8e419b14526')">公司</button>
            <button class="tablinks" onclick="showChart(event, 'a13ac2893d39486cbda0643ccc91dbab')">城市</button>
            <button class="tablinks" onclick="showChart(event, 'f8b0da34eb65493c8f70c3266d6cb046')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, 'b08040c1b1e94557827aaeba615967c5')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, '568ca8c9afb347e39ac4521ff63058bd')">区域</button>
            <button class="tablinks" onclick="showChart(event, 'fc0f5d7aacaa4a25b387deda6355c51c')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, '1ea438fc959f4d2aa7e6075be383e240')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, '6f8b5d72482349108c293641734a5255')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, '42bc9f679a814404841a1ce619ed6397')">行业</button>
            <button class="tablinks" onclick="showChart(event, 'f46facd580db42a8aa05f03b4e92746e')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, '20131a9d07984280a1fc2e1a71ca5db9')">公司福利</button>
    </div>

    <div class="box">
                <div id="283f23ad4b264fb9bd15f8e419b14526" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_283f23ad4b264fb9bd15f8e419b14526 = echarts.init(
            document.getElementById('283f23ad4b264fb9bd15f8e419b14526'), 'white', {renderer: 'canvas'});
            
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
    
        var option_283f23ad4b264fb9bd15f8e419b14526 = {
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
                            "color": "rgb(51,21,156)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,29,115)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,55,148)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,122,157)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,127,3)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,54,147)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,114,153)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,45,135)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,145,151)"
                        }
                    }
                },
                {
                    "name": "\u964c\u964c",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,99,2)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,128)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u591a\u591a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,109,106)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,14,21)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,68,100)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,157,43)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,45,136)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,39,90)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,131,137)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,52,39)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,95,21)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,88,36)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,0,157)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8054\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,122,67)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,19,127)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,96,98)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,157,23)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,5,79)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,135,21)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,133,16)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,111,114)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,28,42)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,116,20)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,32,44)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,32,110)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,1,146)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u91cf\u5b50",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,112,59)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,63,79)"
                        }
                    }
                },
                {
                    "name": "\u732b\u5c90\u667a\u80fd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,4,142)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,116,56)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,34,157)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,103,6)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,92,81)"
                        }
                    }
                },
                {
                    "name": "\u8363\u8000\u7ec8\u7aef",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,129,10)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,3,25)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7814\u7a76\u9662",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,63,140)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,114,80)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,90,94)"
                        }
                    }
                },
                {
                    "name": "\u53c2\u6570",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,138,98)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,124,100)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,10,121)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u4fe1\u91d1\u79d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,54,3)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,104,77)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,27,1)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,33,136)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5b87\u65e0\u9650",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,101,75)"
                        }
                    }
                },
                {
                    "name": "\u660e\u7565\u79d1\u6280\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,119,147)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,82,24)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,156,134)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u667a\u6167",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,6,82)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5411\u4e7e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,49,143)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,103,50)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,44,71)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,129,6)"
                        }
                    }
                },
                {
                    "name": "\u6613\u8f66\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,119,97)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,155,25)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,98,138)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,71,92)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,68,152)"
                        }
                    }
                },
                {
                    "name": "\u827a\u6570\u672a\u6765",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,98,107)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,145,27)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,125,90)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,34,150)"
                        }
                    }
                },
                {
                    "name": "\u5219\u4e00\u4f9b\u5e94\u94fe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,92,57)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,83,131)"
                        }
                    }
                },
                {
                    "name": "\u6155\u601d\u5065\u5eb7\u7761\u7720",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,43,104)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u89c6\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,81,12)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,9,97)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,96,96)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,28,143)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,130,106)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,141,18)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,125,133)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,90,69)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,115,158)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,79,103)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,117,10)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,101,61)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,88,90)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,126,51)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,45,116)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,91,62)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5c1a\u535a\u745e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,150,35)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,125,71)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,3,107)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,52,28)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,132,130)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,110,13)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,108,42)"
                        }
                    }
                },
                {
                    "name": "\u641c\u624d\u4eba\u529b\u8d44\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,14,111)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,15,45)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,16,16)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,48,63)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,39,11)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,56,132)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,14,81)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,30,137)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u9014\u8bfe\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,104,79)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,28,149)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,153,85)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,106,31)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,115,13)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,84,68)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,127,97)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,73,32)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u676d\u5dde\u7814\u7a76\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,126,51)"
                        }
                    }
                },
                {
                    "name": "\u745e\u9f99\u90a6\u730e\u5934",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,5,68)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,4,156)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,149,36)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,26,57)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,75,123)"
                        }
                    }
                },
                {
                    "name": "Convert lab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,107,53)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,136,107)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,73,86)"
                        }
                    }
                },
                {
                    "name": "Mobvista",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,100,75)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u5fc3\u97f3\u7b26",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,99,83)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,101,55)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,34,111)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,36,24)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u7eff\u571f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,103,70)"
                        }
                    }
                },
                {
                    "name": "\u597d\u897f\u67da\u6559\u80b2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,35,93)"
                        }
                    }
                },
                {
                    "name": "EM3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,38,11)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,156,85)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,75,102)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,90,63)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,134,154)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u805a\u96c6\u56e2\uff08JOYY Inc.\uff09",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,133,144)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e92\u6559\u6559\u80b2\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,69,140)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,53,51)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,151,76)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,25,20)"
                        }
                    }
                },
                {
                    "name": "\u574e\u5fb7\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,128,110)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,89,122)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,18,93)"
                        }
                    }
                },
                {
                    "name": "NIO\u851a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,86,39)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,35,149)"
                        }
                    }
                },
                {
                    "name": "\u9053\u9053",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,96,80)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,77,81)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,16,86)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,12,116)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,148,97)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,58,44)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,37,66)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,73,40)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,97,158)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,117,46)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,84,111)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,145,104)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,8,45)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,109,66)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7075\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,119,159)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,115,28)"
                        }
                    }
                },
                {
                    "name": "\u888b\u9f20\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,59,1)"
                        }
                    }
                },
                {
                    "name": "\u767d\u7280\u725b\u667a\u8fbe\uff08\u5317\u4eac\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,35,70)"
                        }
                    }
                },
                {
                    "name": "Veniibot\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,96,146)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,154,36)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,137,12)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,71,21)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u60f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,24,25)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,160,12)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u777f\u667a\u836f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,76,57)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u770b\u6f2b\u753b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,114,82)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u878d\u521b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,0,7)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u5570\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,142,2)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,94,61)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u91ce\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,79,112)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u9053\u5b87",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,97,82)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,57,11)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,98,78)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,101,27)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,49,118)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,113,46)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,152,18)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u4eab\u5929\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,151,152)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,83,63)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9c81\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,123)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11\u5065\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,111,50)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u601d\u7586",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,129,68)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,24,4)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ebf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,24,133)"
                        }
                    }
                },
                {
                    "name": "\u73cd\u7231\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,158,127)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,56,11)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,97,60)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,157,33)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,105,143)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,99,142)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u601d\u4fe1\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,87,91)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77\u4f18\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,90,123)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u89c2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,84,28)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,12,51)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,11,119)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,142,72)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,83,145)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u4fe1\u521b\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,84,54)"
                        }
                    }
                },
                {
                    "name": "\u5bc4\u4e91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,122,69)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,119,123)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\uff08\u5e7f\u4e1c\uff09\u4ea7\u4e1a\u4e92\u8054\u7f51...",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,106,70)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,52,100)"
                        }
                    }
                },
                {
                    "name": "\u6613\u822a\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,8,153)"
                        }
                    }
                },
                {
                    "name": "\u6781\u89c6\u89d2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,12,71)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,146,126)"
                        }
                    }
                },
                {
                    "name": "\u5929\u667a\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,24,94)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,118,60)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,135,29)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,107,146)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,147,124)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,24,139)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f71APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,45,154)"
                        }
                    }
                },
                {
                    "name": "\u864e\u535a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,104,26)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,124,139)"
                        }
                    }
                },
                {
                    "name": "Rokid",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,79,49)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u79d1\u5b66\u9662\u7535\u5b50\u5b66\u7814\u7a76\u6240\u82cf\u5dde\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,130,107)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,131,97)"
                        }
                    }
                },
                {
                    "name": "\u552f\u54c1\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,101,104)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,91,102)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u76db\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,125,25)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\uff08\u4e2d\u56fd\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,25,87)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,121,86)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,26,128)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u4e30\u5de2\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,77,155)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9a6c\u4f01\u670d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,136,28)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,106,109)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,9,85)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,129,6)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u56fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,68,39)"
                        }
                    }
                },
                {
                    "name": "\u6765\u56de\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,124,113)"
                        }
                    }
                },
                {
                    "name": "UU\u8dd1\u817f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,124,104)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,135,20)"
                        }
                    }
                },
                {
                    "name": "Ximmerse",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,82,73)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5f18\u548c\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,81,68)"
                        }
                    }
                },
                {
                    "name": "\u5947\u68a6\u8005",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,100,2)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u65b9\u548c\u5317\u4eac",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,115,17)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u725b\u7535\u52a8\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,157,6)"
                        }
                    }
                },
                {
                    "name": "\u601d\u56fe\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,85,36)"
                        }
                    }
                },
                {
                    "name": "\u901f\u611f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,106,59)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,148,22)"
                        }
                    }
                },
                {
                    "name": "\u572d\u76ee\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,57,81)"
                        }
                    }
                },
                {
                    "name": "eBrain",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,124,142)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u96f6\u8dc3\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,61,9)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,156,82)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,118,130)"
                        }
                    }
                },
                {
                    "name": "\u777f\u755c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,154,33)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,24,78)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e5d\u8857\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,6,6)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,104,118)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,91,98)"
                        }
                    }
                },
                {
                    "name": "LinkDoc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,145,109)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,151,126)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,113,151)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,133,58)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,97,73)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u63a2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,111,121)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,75,71)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,86,113)"
                        }
                    }
                },
                {
                    "name": "\u6570\u6f9c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,115,32)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,28,88)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,109,29)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u7279\u7eb3\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,84,138)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,141,74)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,45,52)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,133,22)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,64,108)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,113,66)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,73,121)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,158,55)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,112,153)"
                        }
                    }
                },
                {
                    "name": "\u745e\u591a\u601d\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,122,107)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,24,0)"
                        }
                    }
                },
                {
                    "name": "\u9cb2\u9e4f\u4e91\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,79,19)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,114,64)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,63,108)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,72,143)"
                        }
                    }
                },
                {
                    "name": "\u6653\u6a3e\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,97,63)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,32,47)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,123,2)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,37,23)"
                        }
                    }
                },
                {
                    "name": "\u97e9\u521b\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,52,139)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,130,43)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,70,102)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,62,41)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53ca\u96f6\u552e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,134,33)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,154,18)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e91\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,97,35)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,48,11)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,98,77)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u7535\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,25,91)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,149,69)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,78,140)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,121,159)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,2,109)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,71,134)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,56,22)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,1,144)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,50,6)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,33,108)"
                        }
                    }
                },
                {
                    "name": "\u667a\u52a0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,133,34)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,60,97)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6d4b\u5bfc\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,80,75)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u56fe\u817e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,10,6)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u6700\u597d\u7684\u5728\u7ebf\u4eba\u8138\u8bc6\u522b\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,49,63)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7267\u539f\u6570\u5b57\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,152,144)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,67,120)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,123,154)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,149,49)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,67,115)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,79,92)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,48,64)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,104,22)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80fd\u534e\u667a\u80fd\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,158,46)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u9536\u5170\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,59,134)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,27,112)"
                        }
                    }
                },
                {
                    "name": "\u68a6\u9977\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,4,6)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u5929\u5fae\u661f\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,155,21)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u9f13\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,95,111)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,133,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,83,156)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,41,77)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,114,30)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8c61\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,30,3)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6b21\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,57,98)"
                        }
                    }
                },
                {
                    "name": "\u5353\u8f69\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,9,45)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5fc5\u9009\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,85,46)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,110,0)"
                        }
                    }
                },
                {
                    "name": "\u4e98\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,92,115)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7fcc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,77,147)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u7ae0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,44,160)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,133,53)"
                        }
                    }
                },
                {
                    "name": "\u6700\u53f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,10,150)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u77e5\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,93,144)"
                        }
                    }
                },
                {
                    "name": "\u957f\u4ead\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,81,29)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,148,110)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,61,106)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,112,42)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,156,44)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,141,125)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u4f17\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,70,96)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u80fd\u8fbe\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,152,41)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,77,142)"
                        }
                    }
                },
                {
                    "name": "\u822a\u5929\u7231\u9510",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,12,142)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,24,143)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,142,44)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8702\u7a9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,152,64)"
                        }
                    }
                },
                {
                    "name": "\u4e01\u9999\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,141,114)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u91d1\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,110,25)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u4e91\u6749",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,22,98)"
                        }
                    }
                },
                {
                    "name": "Sleepace \u4eab\u7761",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,90,83)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,139,36)"
                        }
                    }
                },
                {
                    "name": "\u67d2\u96f6\u58f9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,23,40)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,33,70)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u667a\u52a0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,31,115)"
                        }
                    }
                },
                {
                    "name": "\u65af\u683c\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,149,106)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u8302\u5929\u521d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,5,150)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,151,126)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,130,154)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u57ce\u601d\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,6,109)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,100,117)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u540d\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,58,3)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,93,68)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,115,133)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,91,23)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,0,150)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,106,40)"
                        }
                    }
                },
                {
                    "name": "\u503c\u5f97\u4e70\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,105,151)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6570\u667a\u82af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,73,96)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,31,147)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,129,155)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u798f\u7984\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,41,142)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,156,150)"
                        }
                    }
                },
                {
                    "name": "\u9014\u5bb6\u6c11\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,18,127)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u5fc3\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,71,43)"
                        }
                    }
                },
                {
                    "name": "\u5531\u5427-\u73a9\u97f3\u4e50\uff0c\u5c31\u4e0a\u5531\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,159,47)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u6f2b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,83,136)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,75,128)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,16,142)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6f14\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,121,75)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,133,55)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,160,157)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6469\u8c61\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,69,80)"
                        }
                    }
                },
                {
                    "name": "\u592a\u521d\u5f08\u5baa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,15,109)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,20,47)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,18,91)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,71,144)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,63,94)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,148,42)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u96c6\u8054\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,89,41)"
                        }
                    }
                },
                {
                    "name": "BaseBit AI \u7ffc\u65b9\u5065\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,14,83)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,38,126)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,112,157)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u5fae\u5149\u96c6\u7535\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,116,121)"
                        }
                    }
                },
                {
                    "name": "\u8054\u6613\u878dlinklogis",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,94,130)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,49,3)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5bb6\u7f51\u7edc\u6280\u672f\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,95,138)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8fea\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,8,42)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,100,11)"
                        }
                    }
                },
                {
                    "name": "\u8d28\u5b50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,90,117)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,118,6)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u4e16\u7eaa\u4e1c\u65b9\u901a\u8baf\u8bbe\u5907\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,160,156)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4e13\u5bb6.COM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,76,142)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f26\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,141,91)"
                        }
                    }
                },
                {
                    "name": "\u7231\u8bed\u5427",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,62,21)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,142,84)"
                        }
                    }
                },
                {
                    "name": "\u771f\u6e90\u6865\u4f01\u4e1a\u54a8\u8be2\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,0,95)"
                        }
                    }
                },
                {
                    "name": "\u6f2b\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,94,103)"
                        }
                    }
                },
                {
                    "name": "WeLab\u536b\u76c8\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,99,133)"
                        }
                    }
                },
                {
                    "name": "IntraMirror",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,2,147)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,121,123)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9ad8\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,124,154)"
                        }
                    }
                },
                {
                    "name": "\u8d22\u76c8\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,116,1)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,71,61)"
                        }
                    }
                },
                {
                    "name": "\u70ed\u4e91\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,95,65)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,52,50)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,121,23)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6728\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,1,156)"
                        }
                    }
                },
                {
                    "name": "\u6469\u822a\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,99,101)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,130,71)"
                        }
                    }
                },
                {
                    "name": "\u5341\u624d\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,155,47)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u5c0f\u6ee1\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,91,120)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u6c7d\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,16,91)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,67,105)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6167\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,49,102)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u7ff0\u683c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,54,55)"
                        }
                    }
                },
                {
                    "name": "\u5373\u6784\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,157,30)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,33,118)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,38,13)"
                        }
                    }
                },
                {
                    "name": "\u53eb\u53eb\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,68,49)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,23,154)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,18,135)"
                        }
                    }
                },
                {
                    "name": "\u98de\u5e38\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,31,68)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u5fc3\u529b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,4,115)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u52bf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,101,76)"
                        }
                    }
                },
                {
                    "name": "\u5c0fi\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,143,43)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,82,126)"
                        }
                    }
                },
                {
                    "name": "\u987a\u7f51\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,14,72)"
                        }
                    }
                },
                {
                    "name": "\u76ca\u76df\u64cd\u76d8\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,145,142)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99\u7adf\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,2,58)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u661f\u63a2\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,59,94)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,145,85)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u667a\u80fd\u5236\u9020\u8f6f\u4ef6\u5f00\u53d1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,62,132)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u8fbe\u6570\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,151,146)"
                        }
                    }
                },
                {
                    "name": "\u9e3f\u6cf0\u9f0e\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,62,153)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,84,51)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u4ee5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,85,117)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,156,158)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,31,102)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,138,148)"
                        }
                    }
                },
                {
                    "name": "\u94a2\u94c1\u4fa0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,154,73)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,154,32)"
                        }
                    }
                },
                {
                    "name": "Udesk\uff0d\u4f01\u4e1a\u7ea7\u667a\u80fd\u5ba2\u670d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,59,10)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,142,14)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,136,131)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,49,22)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79fb\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,121,130)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,151,120)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u62c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,74,100)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u98de\u7f51\u7edc-\u8f66\u8f7d\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,30,61)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,141,36)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,86,116)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u6bd4\u7279\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,51,80)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,127,58)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,82,108)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u89c8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,72,7)"
                        }
                    }
                },
                {
                    "name": "\u9038\u4eab\u7535\u5b50\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,121,100)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,85,14)"
                        }
                    }
                },
                {
                    "name": "OPENAILAB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,60,63)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5f84\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,46,30)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,67,148)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u89c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,98,76)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u627f\u6cf0\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,55,105)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,73,158)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8f85\u7279\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,13,134)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,28,63)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,146,140)"
                        }
                    }
                },
                {
                    "name": "\u9636\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,53,44)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u666e\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,8,127)"
                        }
                    }
                },
                {
                    "name": "\u591a\u725b\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,61,14)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u67da\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,28,159)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u91d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,110,32)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6d1b\u514b\u822a\u7a7a\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,72,61)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,30,124)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,59,1)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5de5\u540c\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,117,106)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u70b9\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,17,64)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,150,17)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u8dc3\u6609\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,89,32)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6781\u777f\u79d1\u6280\u6709\u9650\u8d23\u4efb\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,108,111)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,65,71)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u90a6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,116,13)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u7f8e\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,154,118)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,145,21)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,55,15)"
                        }
                    }
                },
                {
                    "name": "\u6c85\u9038\u65b9\u8fbe\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,104,157)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,46,56)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,46,135)"
                        }
                    }
                },
                {
                    "name": "\u4ee5\u89c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,144,75)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,24,154)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,39,109)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,28,27)"
                        }
                    }
                },
                {
                    "name": "\u9541\u4fe1\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,79,121)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,39,153)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,150,138)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,122,89)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,135,29)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,117,8)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u5ba2\u6615\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,145,19)"
                        }
                    }
                },
                {
                    "name": "\u6c57\u9a6c\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,23,129)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,5,67)"
                        }
                    }
                },
                {
                    "name": "\u886b\u6570\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,152,125)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,54,112)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,152,120)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8c19\u65af\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,91,65)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,156,148)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u51cc\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,43,159)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,86,133)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,110,56)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u6e38\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,99,114)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,2,91)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,58,8)"
                        }
                    }
                },
                {
                    "name": "\u8354\u679d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,56,142)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u7403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,64,66)"
                        }
                    }
                },
                {
                    "name": "\u9091\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,41,81)"
                        }
                    }
                },
                {
                    "name": "\u8d62\u706b\u866b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,26,106)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u9886\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,140,9)"
                        }
                    }
                },
                {
                    "name": "InMobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,12,24)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,64,119)"
                        }
                    }
                },
                {
                    "name": "\u9e70\u4e4b\u773c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,74,122)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,89,133)"
                        }
                    }
                },
                {
                    "name": "\u660e\u6e90\u4e91\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,32,108)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5353\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,133,49)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,108,44)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,82,14)"
                        }
                    }
                },
                {
                    "name": "\u6c90\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,129,155)"
                        }
                    }
                },
                {
                    "name": "OSR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,80,87)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d0\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,20,99)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u679c\u6bd4\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,101,16)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,25,17)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5e2e\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,84,85)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u95fb\u6b4c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,105,12)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5219\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,128,100)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,78,124)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,81,120)"
                        }
                    }
                },
                {
                    "name": "\u9756\u6208\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,107,49)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,90,68)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,19,16)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,146,104)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,55,25)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,95,11)"
                        }
                    }
                },
                {
                    "name": "UMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,155,82)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,154,79)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u7f51\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,80,102)"
                        }
                    }
                },
                {
                    "name": "\u745e\u5a01\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,101,64)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,156,141)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,13,57)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,85,39)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,121,58)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,86,70)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,112,143)"
                        }
                    }
                },
                {
                    "name": "\u548c\u7f8e\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,100,38)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,84,134)"
                        }
                    }
                },
                {
                    "name": "\u8baf\u6c47\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,5,76)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u4e70\u53cb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,18,36)"
                        }
                    }
                },
                {
                    "name": "\u67ab\u53f6\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,102,19)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,94,76)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,10,135)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,142,63)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,36,57)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,33,111)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u6570\u79d1\u96c6\u56e2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,125,127)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,25,108)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5927\u8baf\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,138,160)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,29,87)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,5,41)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u76f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,132,25)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,10,112)"
                        }
                    }
                },
                {
                    "name": "\u8c46\u679c\u7f8e\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,13,30)"
                        }
                    }
                },
                {
                    "name": "spring professional",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,108,89)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u4ee3\u62d3\u7075",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,46,160)"
                        }
                    }
                },
                {
                    "name": "\u5149\u9274\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,142,105)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u5b9a\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,2,16)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,24,134)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,18,39)"
                        }
                    }
                },
                {
                    "name": "\u660e\u671d\u4e07\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,67,80)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5bb6\u5065\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,115,69)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e09\u77f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,91,38)"
                        }
                    }
                },
                {
                    "name": "\u5965\u6bd4\u4e2d\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,58,109)"
                        }
                    }
                },
                {
                    "name": "Fordeal",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,129,125)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,118,110)"
                        }
                    }
                },
                {
                    "name": "\u667a\u878d\u4fe1\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,110,142)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,124,51)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,115,95)"
                        }
                    }
                },
                {
                    "name": "\u8054\u4ec1\u5065\u5eb7\u533b\u7597\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,19,118)"
                        }
                    }
                },
                {
                    "name": "AfterShip",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,70,102)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,4,12)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,157,2)"
                        }
                    }
                },
                {
                    "name": "Nox\u591c\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,49,116)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5370\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,71,5)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,141,105)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e2d\u8f6f\u534e\u817e\u8f6f\u4ef6\u7cfb\u7edf\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,33,122)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,118,61)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,115,5)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,49,108)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9488\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,103,144)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,68,32)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u987f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,160,22)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,155,82)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u770b\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,42,129)"
                        }
                    }
                },
                {
                    "name": "DataEye",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,24,77)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u7ef4\u667a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,142,145)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u4f4e\u78b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,3,59)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u7279\u7f8e\u8fea",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,72,82)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9Dmall",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,51,126)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,148,109)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u4f17\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,54,49)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7279\u66fc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,89,26)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,99,18)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,133,93)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,63,104)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,39,28)"
                        }
                    }
                },
                {
                    "name": "\u81f3\u771f\u4e92\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,73,84)"
                        }
                    }
                },
                {
                    "name": "Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,42,66)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u8bfa\u5fae\u94f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,50,73)"
                        }
                    }
                },
                {
                    "name": "\u83ab\u6bd4\u55e8\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,69,54)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5fc5\u80dc\u4e92\u5a31\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,30,87)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,14,15)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,48,24)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,31,61)"
                        }
                    }
                },
                {
                    "name": "\u533b\u51c6\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,102,124)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,31,5)"
                        }
                    }
                },
                {
                    "name": "\u76db\u4e16\u9e92\u9e9f\u519c\u4e1a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,17,20)"
                        }
                    }
                },
                {
                    "name": "\u5bd3\u8a00\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,109,24)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,29,125)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,124,115)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u521b\u66e6\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,51,28)"
                        }
                    }
                },
                {
                    "name": "\u516d\u4e00\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,42,34)"
                        }
                    }
                },
                {
                    "name": "\u667a\u4e91\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,68,134)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d28\u6570\u65af\u8fbe\u514b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,70,71)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,116,39)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,20,75)"
                        }
                    }
                },
                {
                    "name": "\u5916\u7814\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,104,58)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98ce\u7231\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,59,57)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,56,86)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,124,79)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,98,6)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u4ed5\u8fbe\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,36,133)"
                        }
                    }
                },
                {
                    "name": "\u7425\u73c0\u521b\u60f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,146,133)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,42,31)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5bb8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,75,155)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,26,134)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,13,35)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,138,76)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u79d1\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,106,106)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,15,13)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,123,33)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5b8f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,129,91)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7b97\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,125,26)"
                        }
                    }
                },
                {
                    "name": "FreeWheel",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,155,151)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,131,54)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,150,149)"
                        }
                    }
                },
                {
                    "name": "\u4e3d\u7acb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,63,101)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,127,23)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,156,99)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,103,97)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,115,0)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,0,121)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,91,114)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,137,19)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,97,63)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u653f\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,129,20)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6df1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,31,37)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,84,14)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u7280\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,116,26)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,7,56)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,119,49)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,101,13)"
                        }
                    }
                },
                {
                    "name": "\u5154\u73a9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,79,71)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,2,117)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,155,114)"
                        }
                    }
                },
                {
                    "name": "\u53cb\u5854\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,3,131)"
                        }
                    }
                },
                {
                    "name": "\u8109\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,59,129)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u91cd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,154,18)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,45,81)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u7f19\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,64,141)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,96,99)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,100,116)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,123,36)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,145,1)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,74,139)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u8346\u6843\u674e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,50,155)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,21,109)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,65,63)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,67,16)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,152,12)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,2,108)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u70b9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,10,103)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,51,17)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4ea7\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,145,124)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,21,16)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,50,3)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,46,74)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,52,137)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,114,90)"
                        }
                    }
                },
                {
                    "name": "\u5b97\u7533\u521b\u65b0\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,40,31)"
                        }
                    }
                },
                {
                    "name": "\u534e\u665f\u660e\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,73,96)"
                        }
                    }
                },
                {
                    "name": "\u79cd\u68a6\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,32,101)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,25,76)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,151,31)"
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
        chart_283f23ad4b264fb9bd15f8e419b14526.setOption(option_283f23ad4b264fb9bd15f8e419b14526);
    </script>
                <div id="a13ac2893d39486cbda0643ccc91dbab" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_a13ac2893d39486cbda0643ccc91dbab = echarts.init(
            document.getElementById('a13ac2893d39486cbda0643ccc91dbab'), 'white', {renderer: 'canvas'});
        var option_a13ac2893d39486cbda0643ccc91dbab = {
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
                            "color": "rgb(76,38,141)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 309,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,136,88)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 309,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,150,29)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 171,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,157,92)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,31,128)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,13,149)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,57,47)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,41,21)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,95,139)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,155,111)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,30,101)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,138)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,151,71)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,118,42)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,130,39)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,119,54)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,132,78)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,123,126)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,5,55)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,101,107)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,61,27)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6d25",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,47,21)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,85,107)"
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
        chart_a13ac2893d39486cbda0643ccc91dbab.setOption(option_a13ac2893d39486cbda0643ccc91dbab);
    </script>
                <div id="f8b0da34eb65493c8f70c3266d6cb046" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_f8b0da34eb65493c8f70c3266d6cb046 = echarts.init(
            document.getElementById('f8b0da34eb65493c8f70c3266d6cb046'), 'white', {renderer: 'canvas'});
        var option_f8b0da34eb65493c8f70c3266d6cb046 = {
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
                    "name": "\u957f\u6c99"
                },
                {
                    "value": 7,
                    "name": "\u5357\u4eac"
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
                    "name": "\u5408\u80a5"
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
                    "value": 2,
                    "name": "\u60e0\u5dde"
                },
                {
                    "value": 2,
                    "name": "\u5b81\u6ce2"
                },
                {
                    "value": 1,
                    "name": "\u9752\u5c9b"
                },
                {
                    "value": 1,
                    "name": "\u5929\u6d25"
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
        chart_f8b0da34eb65493c8f70c3266d6cb046.setOption(option_f8b0da34eb65493c8f70c3266d6cb046);
    </script>
                <div id="b08040c1b1e94557827aaeba615967c5" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b08040c1b1e94557827aaeba615967c5 = echarts.init(
            document.getElementById('b08040c1b1e94557827aaeba615967c5'), 'white', {renderer: 'canvas'});
            
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
    
        var option_b08040c1b1e94557827aaeba615967c5 = {
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
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        7
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
                    "name": "\u5408\u80a5",
                    "value": [
                        117.27,
                        31.86,
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
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        3
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
                    "name": "\u5b81\u6ce2",
                    "value": [
                        121.56,
                        29.86,
                        2
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
        chart_b08040c1b1e94557827aaeba615967c5.setOption(option_b08040c1b1e94557827aaeba615967c5);
    </script>
                <div id="568ca8c9afb347e39ac4521ff63058bd" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_568ca8c9afb347e39ac4521ff63058bd = echarts.init(
            document.getElementById('568ca8c9afb347e39ac4521ff63058bd'), 'white', {renderer: 'canvas'});
        var option_568ca8c9afb347e39ac4521ff63058bd = {
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
                            "color": "rgb(83,66,84)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 134,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,100,141)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 131,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,1,114)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,54,24)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,46,53)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,17,114)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,48,119)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,134,46)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,77,0)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,60,64)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,86,39)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,66,103)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,128,132)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,50,131)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,82,57)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,52,25)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,119,102)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,86,160)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,137,54)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,129,35)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,106,127)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,159,52)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,36,23)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,55,106)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,75,114)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,84,26)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,23,91)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,134,108)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,125,51)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,145,36)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,108,110)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,120,76)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,142,60)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,119,61)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,154,155)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,139,135)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,83,52)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,117,2)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,7,3)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,156,0)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,67,66)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,63,68)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,74,145)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,10,159)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,4,47)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,113,99)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,59,136)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,109,157)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,88,113)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,100,119)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,118,31)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,70,40)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,54,140)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,86,48)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,25,37)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,61,135)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,27,139)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,154,8)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,54,23)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,9,157)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,52,79)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,65,93)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,59,6)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,128,136)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,50,95)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,127,86)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,154,125)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,11,131)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,56,93)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,125,96)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,79,108)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,10,111)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,28,49)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,12,103)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,137,42)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,72,65)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,136,23)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,17,122)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,87,83)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,92)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,11,61)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,147,124)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,128,111)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,14,10)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,69,88)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,98,123)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,128,63)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,22,32)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,115,78)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,113,153)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,45,110)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,134,33)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,68,144)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,129,145)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9a\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,61,23)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8425",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,87,103)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,54,118)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,45,130)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,17,5)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,155,119)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,100,149)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,110,82)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,71,88)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,87,3)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,79,153)"
                        }
                    }
                },
                {
                    "name": "\u76d0\u7530\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,110,79)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,158,19)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,70,154)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u8def",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,93,26)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,1,86)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,107,142)"
                        }
                    }
                },
                {
                    "name": "\u671d\u5916",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,119,43)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,148,53)"
                        }
                    }
                },
                {
                    "name": "\u5149\u660e\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,128,45)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,151,86)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,80,134)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,147,1)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6c34\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,41,79)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,7,71)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,90,57)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,50,125)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,46,100)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,51,51)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5858",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,92,35)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,28,116)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,99,32)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,137,137)"
                        }
                    }
                },
                {
                    "name": "\u65e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,103,41)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,61,25)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,88,40)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,40,113)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,29,31)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,76,153)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,50,78)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u5143\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,61,141)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u5858\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,101,14)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,45,65)"
                        }
                    }
                },
                {
                    "name": "\u80dc\u6d66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,118,6)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,87,35)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,135,123)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6cc9\u9a7f\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,25,130)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,34,24)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,101,32)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,74,2)"
                        }
                    }
                },
                {
                    "name": "\u5b98\u6d32",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,95,27)"
                        }
                    }
                },
                {
                    "name": "\u673a\u6295\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,11,134)"
                        }
                    }
                },
                {
                    "name": "\u6885\u9647",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,40,118)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5885\u6e56",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,80,86)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,144,80)"
                        }
                    }
                },
                {
                    "name": "\u5929\u76ee\u5c71\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,112,86)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,27,124)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,60,34)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,79,94)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9f99\u5761\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,26,94)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,39,105)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,12,84)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6d77\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,26,76)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,84,132)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,160,81)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,136,70)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,78,32)"
                        }
                    }
                },
                {
                    "name": "\u5ba3\u6b66\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,72,88)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,31,58)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,0,91)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,76,55)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,102,117)"
                        }
                    }
                },
                {
                    "name": "\u5927\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,50,100)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,107,67)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,41,49)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,81,155)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,81,76)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,117,136)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,156,119)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,27,57)"
                        }
                    }
                },
                {
                    "name": "\u5434\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,58,29)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,112,32)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,159,15)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,125,17)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,90,133)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8fde\u6d3c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,88,2)"
                        }
                    }
                },
                {
                    "name": "\u7436\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,83,97)"
                        }
                    }
                },
                {
                    "name": "\u5510\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,52,79)"
                        }
                    }
                },
                {
                    "name": "\u6797\u6821\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,73,78)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,151,1)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,104,146)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,67,12)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,125,36)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,89,15)"
                        }
                    }
                },
                {
                    "name": "\u5858\u8fb9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,15,19)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,78,8)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,53,20)"
                        }
                    }
                },
                {
                    "name": "\u911e\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,151,63)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,159,122)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,64,113)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u5c9b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,80,106)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,122,135)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,74,69)"
                        }
                    }
                },
                {
                    "name": "\u6ca3\u6e2d\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,103,139)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f\u4e1c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,2,106)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,141,135)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5bff\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,78,118)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,65,42)"
                        }
                    }
                },
                {
                    "name": "\u8700\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,149,137)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,15,22)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,139,59)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,126,60)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,8,29)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6ca7\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,100,105)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,149,29)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,151,65)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5fb7\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,60,139)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e49\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,112,155)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,140,22)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e00\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,123,101)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,78,13)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,134,60)"
                        }
                    }
                },
                {
                    "name": "\u51bc\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,20,142)"
                        }
                    }
                },
                {
                    "name": "\u7fe0\u82d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,156,107)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,54,53)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,103,49)"
                        }
                    }
                },
                {
                    "name": "\u8700\u6c49\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,140,35)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,119,29)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99\u53bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,29,70)"
                        }
                    }
                },
                {
                    "name": "\u78a7\u4e91\u793e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,27,16)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,76,15)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u5e7f\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,39,56)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,26,17)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u534e\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,109,46)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,66,31)"
                        }
                    }
                },
                {
                    "name": "\u9b4f\u516c\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,6,30)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,131,90)"
                        }
                    }
                },
                {
                    "name": "\u6f58\u5bb6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,6,66)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,104,13)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,78,11)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u798f\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,34,77)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,79,53)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,146,52)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6d77\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,115,100)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6c5f\u6e7e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,18,73)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,5,74)"
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
        chart_568ca8c9afb347e39ac4521ff63058bd.setOption(option_568ca8c9afb347e39ac4521ff63058bd);
    </script>
                <div id="fc0f5d7aacaa4a25b387deda6355c51c" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_fc0f5d7aacaa4a25b387deda6355c51c = echarts.init(
            document.getElementById('fc0f5d7aacaa4a25b387deda6355c51c'), 'white', {renderer: 'canvas'});
        var option_fc0f5d7aacaa4a25b387deda6355c51c = {
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
                    "name": "\u798f\u7530\u533a"
                },
                {
                    "value": 26,
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 26,
                    "name": "\u4e94\u9053\u53e3"
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
                    "name": "\u77e5\u6625\u8def"
                },
                {
                    "value": 14,
                    "name": "\u6ee8\u6c5f\u533a"
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
                    "name": "\u4e1c\u57ce\u533a"
                },
                {
                    "value": 12,
                    "name": "\u62f1\u5885\u533a"
                },
                {
                    "value": 11,
                    "name": "\u4e1c\u6e56\u65b0\u2026"
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
                    "value": 10,
                    "name": "\u9f99\u534e\u65b0\u2026"
                },
                {
                    "value": 9,
                    "name": "\u9f99\u534e"
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
                    "value": 9,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 9,
                    "name": "\u666e\u9640\u533a"
                },
                {
                    "value": 8,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 8,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 8,
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 8,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 8,
                    "name": "\u77f3\u666f\u5c71\u2026"
                },
                {
                    "value": 8,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 8,
                    "name": "\u8d8a\u79c0\u533a"
                },
                {
                    "value": 8,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 7,
                    "name": "\u9ec4\u6d66\u533a"
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
                    "name": "\u5357\u6c99\u533a"
                },
                {
                    "value": 7,
                    "name": "\u5f90\u5bb6\u6c47"
                },
                {
                    "value": 6,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 6,
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 6,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 6,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 5,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 5,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 5,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 5,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 5,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 5,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 5,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 5,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 5,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 4,
                    "name": "\u56de\u9f99\u89c2"
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
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 4,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 4,
                    "name": "\u6587\u4e09\u8def"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 4,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 4,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 3,
                    "name": "\u9759\u5b89\u533a"
                },
                {
                    "value": 3,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 3,
                    "name": "\u9526\u6c5f\u533a"
                },
                {
                    "value": 3,
                    "name": "\u65b0\u6e2f"
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
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 3,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 3,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 3,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5609\u5b9a\u533a"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u8425"
                },
                {
                    "value": 3,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 3,
                    "name": "\u5f90\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 3,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 3,
                    "name": "\u6f15\u6cb3\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 3,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 2,
                    "name": "\u76d0\u7530\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6e05\u6cb3"
                },
                {
                    "value": 2,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u8def"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 2,
                    "name": "\u671d\u5916"
                },
                {
                    "value": 2,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u5149\u660e\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5357\u5934"
                },
                {
                    "value": 2,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u6c34\u533a"
                },
                {
                    "value": 2,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5357\u6cb9"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5858"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 2,
                    "name": "\u65e0"
                },
                {
                    "value": 2,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u5143\u6865"
                },
                {
                    "value": 2,
                    "name": "\u94b1\u5858\u533a"
                },
                {
                    "value": 2,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 2,
                    "name": "\u80dc\u6d66"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 2,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u6cc9\u9a7f\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u590f\u533a"
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
                    "name": "\u673a\u6295\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6885\u9647"
                },
                {
                    "value": 2,
                    "name": "\u72ec\u5885\u6e56"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 2,
                    "name": "\u5929\u76ee\u5c71\u2026"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 2,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 2,
                    "name": "\u4e5d\u9f99\u5761\u2026"
                },
                {
                    "value": 2,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5357\u6d77\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u6d41\u533a"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5ba3\u6b66\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 1,
                    "name": "\u4e0b\u57ce\u533a"
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
                    "name": "\u5927\u77f3"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u884c"
                },
                {
                    "value": 1,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u56ed\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u5434\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u5317\u5927\u5730"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u5e73\u6e56"
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
                    "name": "\u7436\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u5510\u9547"
                },
                {
                    "value": 1,
                    "name": "\u6797\u6821\u8def"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u5dde\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u5858\u8fb9"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u911e\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u5c9b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u6ca3\u6e2d\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6e2f\u4e1c"
                },
                {
                    "value": 1,
                    "name": "\u8679\u6865"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5bff\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u8700\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6865"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6865"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
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
                    "name": "\u9f99\u6eaa"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5fb7\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u987a\u4e49\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
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
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u51bc\u6751"
                },
                {
                    "value": 1,
                    "name": "\u7fe0\u82d1"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5c71\u533b\u2026"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u8700\u6c49\u8def"
                },
                {
                    "value": 1,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 1,
                    "name": "\u957f\u6c99\u53bf"
                },
                {
                    "value": 1,
                    "name": "\u78a7\u4e91\u793e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u4eac\u5e7f\u6865"
                },
                {
                    "value": 1,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u534e\u8def"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u9b4f\u516c\u6751"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6f58\u5bb6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u4e03\u5b9d"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u798f\u533a"
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
                    "name": "\u6ee8\u6d77\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6c5f\u6e7e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
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
        chart_fc0f5d7aacaa4a25b387deda6355c51c.setOption(option_fc0f5d7aacaa4a25b387deda6355c51c);
    </script>
                <div id="1ea438fc959f4d2aa7e6075be383e240" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1ea438fc959f4d2aa7e6075be383e240 = echarts.init(
            document.getElementById('1ea438fc959f4d2aa7e6075be383e240'), 'white', {renderer: 'canvas'});
        var option_1ea438fc959f4d2aa7e6075be383e240 = {
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
        chart_1ea438fc959f4d2aa7e6075be383e240.setOption(option_1ea438fc959f4d2aa7e6075be383e240);
    </script>
                <div id="6f8b5d72482349108c293641734a5255" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_6f8b5d72482349108c293641734a5255 = echarts.init(
            document.getElementById('6f8b5d72482349108c293641734a5255'), 'white', {renderer: 'canvas'});
        var option_6f8b5d72482349108c293641734a5255 = {
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
        chart_6f8b5d72482349108c293641734a5255.setOption(option_6f8b5d72482349108c293641734a5255);
    </script>
                <div id="42bc9f679a814404841a1ce619ed6397" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_42bc9f679a814404841a1ce619ed6397 = echarts.init(
            document.getElementById('42bc9f679a814404841a1ce619ed6397'), 'white', {renderer: 'canvas'});
        var option_42bc9f679a814404841a1ce619ed6397 = {
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
                            "color": "rgb(65,61,124)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 284,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,39,24)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 199,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,132,116)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 195,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,122,153)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 169,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,80,71)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 126,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,4,48)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,10,151)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,16,126)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,104,103)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,112,82)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,49,32)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,30,16)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,31,15)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,52,37)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,36,62)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,8,21)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,134,101)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,40,103)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,33,4)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,155,106)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,91,146)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,56,65)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,27,111)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,100,39)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,107,118)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,116,83)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,60,101)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,19,106)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,39,122)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,73,151)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,66,84)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,67,145)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,104,148)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,97,100)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,17,129)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,142,84)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,159,141)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,140,75)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,46,70)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,47,40)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,130,12)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,12,129)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,63,21)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,10,79)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,159,63)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,24,64)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,60,6)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,71,145)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,143,135)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,128,104)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,31,62)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,47,47)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,128,144)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,118,16)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,142,127)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,149,115)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,37,74)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,149,31)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,44,10)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,124,14)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,54,91)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,48,140)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,27,10)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,54,31)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,150,139)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,82,30)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,85,26)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,126,71)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,45,117)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,40,121)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,47,137)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,50,118)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,108,47)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,71,72)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,42,122)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,155,13)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,2,156)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1\u3001\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,104,44)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,41,28)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,15,129)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,52,92)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,41,98)"
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
        chart_42bc9f679a814404841a1ce619ed6397.setOption(option_42bc9f679a814404841a1ce619ed6397);
    </script>
                <div id="f46facd580db42a8aa05f03b4e92746e" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_f46facd580db42a8aa05f03b4e92746e = echarts.init(
            document.getElementById('f46facd580db42a8aa05f03b4e92746e'), 'white', {renderer: 'canvas'});
        var option_f46facd580db42a8aa05f03b4e92746e = {
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
                            "color": "rgb(153,30,103)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 101,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,68,115)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,136,144)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,114,98)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,82,24)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,72,103)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,124,104)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,107,88)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,98,68)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,31,4)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,155,60)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,26,60)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,71,104)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,12,129)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,124,126)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,35,84)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,112,29)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,22,12)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,72,85)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,31,60)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,131,94)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,38,21)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,131,88)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,29,114)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,118,96)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,22,2)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,141,127)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,70,8)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,150,91)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,135,147)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,121,43)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,30,28)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,89,96)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,71,141)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,150,8)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,139,87)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,45,14)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,6,76)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,2,76)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,31,31)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,88,29)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,155,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,57,146)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,22,20)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,124,49)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,43,97)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,75,145)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,90,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,78,155)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,158,96)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,92,147)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,19,149)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,78,88)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,64,105)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,142,136)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,96,153)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,146,48)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,27,126)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,74,22)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,21,79)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,136,20)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,154,102)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,10,18)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,100,41)"
                        }
                    }
                },
                {
                    "name": "DSP\u5e7f\u544a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,144,151)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,64,2)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,137,143)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5546\u54c1\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,37,134)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,108,60)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,60,60)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,37,128)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,30,57)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,42,52)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,32,3)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,102,100)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u9891/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,55,101)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,130,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,12,150)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,78,85)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,50,26)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,151,156)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,0,0)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,26,110)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6691\u5047\u5b9e\u4e60\u751f\u3011\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,115,159)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,123,120)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,101,124)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,50,96)"
                        }
                    }
                },
                {
                    "name": "GNSS\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,49,85)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,67,40)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,7,110)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,64,74)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,126,75)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,106,1)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u5e08\\\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,142,94)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,90,106)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,48,114)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,147,5)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,60,79)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,41,115)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,120,65)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,103,76)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,154,78)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,24,157)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,54,51)"
                        }
                    }
                },
                {
                    "name": "\u6545\u969c\u8bca\u65ad(PHM)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,36,1)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u5185\u63a8 - \u5f00\u53d1/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,105,130)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,88,31)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,106,24)"
                        }
                    }
                },
                {
                    "name": "SW-\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,4,11)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,148,117)"
                        }
                    }
                },
                {
                    "name": "SJY-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,84,68)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u914d\u51c6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,18,120)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,62,0)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u624b\u5199\u8bc6\u522b-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,136,156)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u603b\u76d1\uff08\u5927\u6570\u636e/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,66,70)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,99,125)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,65,95)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,46,143)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,118,118)"
                        }
                    }
                },
                {
                    "name": "Algorithm Engineer \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,133,66)"
                        }
                    }
                },
                {
                    "name": "C++\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,5,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,147,103)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,56,138)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,108,6)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,68,28)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,79,67)"
                        }
                    }
                },
                {
                    "name": "nlp/cv \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,33,129)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,73,23)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,42,3)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,72,76)"
                        }
                    }
                },
                {
                    "name": "AIOPs\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,54,72)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,45,76)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,145,25)"
                        }
                    }
                },
                {
                    "name": "AI\u8bad\u7ec3/\u63a8\u7406\u52a0\u901f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,56,4)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,143,48)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,100,71)"
                        }
                    }
                },
                {
                    "name": "114114-\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,135,78)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,85,133)"
                        }
                    }
                },
                {
                    "name": "11318V-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,91,18)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,87,152)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7ade\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,61,59)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,4,21)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u770b\u70b9\u5546\u4e1a\u5316\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,152,5)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,144,113)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u9690\u79c1\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,90,143)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,56,13)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,133,42)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,70,60)"
                        }
                    }
                },
                {
                    "name": "02416A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,142,122)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,19,123)"
                        }
                    }
                },
                {
                    "name": "1121PC-LT-354-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,113,102)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,126,37)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,98,39)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,147,36)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u5f00\u53d1\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,28,0)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,109,40)"
                        }
                    }
                },
                {
                    "name": "ARVR/\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,21,33)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,84,92)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,8,139)"
                        }
                    }
                },
                {
                    "name": "29912-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,0,22)"
                        }
                    }
                },
                {
                    "name": "Camera\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,46,99)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,74,8)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,154,40)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,64,124)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u5e02\u8ba1\u7b97\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,77,64)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,10,157)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5e73\u53f0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,17,138)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,0,14)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,30,94)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,43,95)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,154,144)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,127,70)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6027\u80fd\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,49,16)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,157,129)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,63,29)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,12,14)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,119,69)"
                        }
                    }
                },
                {
                    "name": "11416Z-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,123,111)"
                        }
                    }
                },
                {
                    "name": "AI\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,52,80)"
                        }
                    }
                },
                {
                    "name": "114125-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,11,78)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,144,25)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,104,117)"
                        }
                    }
                },
                {
                    "name": "25317O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,38,146)"
                        }
                    }
                },
                {
                    "name": "SJY-\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,20,128)"
                        }
                    }
                },
                {
                    "name": "npu\u67b6\u6784\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,59,66)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,44,85)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u4e09\u7ef4\u9ad8\u7cbe\u5efa\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,62,103)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5f00\u53d1/unity/\u6d4b\u8bd5/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,105,98)"
                        }
                    }
                },
                {
                    "name": "\u8def\u7f51\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,78,149)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,44,34)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,86,42)"
                        }
                    }
                },
                {
                    "name": "11312J-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,15,33)"
                        }
                    }
                },
                {
                    "name": "11417L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,111,118)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,123,87)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,124,141)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u683c\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,2,3)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u4f53\u9a8c\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,91,104)"
                        }
                    }
                },
                {
                    "name": "11122I-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,23,129)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,43,39)"
                        }
                    }
                },
                {
                    "name": "\u4eca\u65e5\u5934\u6761-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,14,51)"
                        }
                    }
                },
                {
                    "name": "113195-\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,3,81)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,45,81)"
                        }
                    }
                },
                {
                    "name": "024254-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,74,49)"
                        }
                    }
                },
                {
                    "name": "05412O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,59,63)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,1,24)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,63,104)"
                        }
                    }
                },
                {
                    "name": "KHQ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,30,141)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,55,132)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,121,85)"
                        }
                    }
                },
                {
                    "name": "11412I-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,18,129)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,7,116)"
                        }
                    }
                },
                {
                    "name": "11413S-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,118,67)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,53,129)"
                        }
                    }
                },
                {
                    "name": "00239-\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,144,37)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,73,90)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u533a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,155,2)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,159,35)"
                        }
                    }
                },
                {
                    "name": "1121XJ-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,37,17)"
                        }
                    }
                },
                {
                    "name": "0241VF-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,84,90)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,46,103)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,74,108)"
                        }
                    }
                },
                {
                    "name": "\u521d\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,71,58)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u548c\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,157,63)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,70,4)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,80,158)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,130,92)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,114,139)"
                        }
                    }
                },
                {
                    "name": "0241UC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,38,118)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,28,76)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,5,113)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,140,64)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,114,79)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,65,66)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76\u5b9a\u4f4d\u4e0e\u5730\u56fe\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,50,97)"
                        }
                    }
                },
                {
                    "name": "00233-\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,20,76)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,93,13)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,133,48)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,118,143)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,77,5)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,19,118)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,40,54)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,137,27)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ea7\u54c1\u7ecf\u7406(\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,65,7)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,151,37)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5b89\u5168\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,9,90)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,93,35)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08\uff08\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,120,121)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,118,3)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,85,22)"
                        }
                    }
                },
                {
                    "name": "1131HA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,94,3)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,132,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,51,27)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,142,117)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,92,107)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,41,136)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u6d4f\u89c8\u5668\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,110,93)"
                        }
                    }
                },
                {
                    "name": "\u63a5\u7ba1\u9884\u8b66\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,101,3)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u4eba\u4f53/\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,11,22)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,99,41)"
                        }
                    }
                },
                {
                    "name": "PCG09-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,123,88)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08-\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,140,131)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,105,70)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,112,135)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,59,37)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,85,35)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,109,2)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,79,132)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,27,113)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u7fa4\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,71,30)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,73,55)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,85,6)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,160,93)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,48,3)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,19,107)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,88,70)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,47,106)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,104,130)"
                        }
                    }
                },
                {
                    "name": "AIOPS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,92,157)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,159,52)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,97,19)"
                        }
                    }
                },
                {
                    "name": "1141BC-\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,42,72)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,154,151)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,113,49)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,12,160)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u56ed\u62db\u8058-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,105,66)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,42,79)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,35,81)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,142,31)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u533b\u7597\u641c\u7d22-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,89,5)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,124,48)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,21,121)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,114,19)"
                        }
                    }
                },
                {
                    "name": "25318B-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,74,159)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,114,84)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u591a\u6a21\u6001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,152,125)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,33,82)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,1,115)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,135,34)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,88,67)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,2,80)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,13,133)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,117,150)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,157,29)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,20,128)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7/\u97f3\u4e50\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,90,150)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,6,18)"
                        }
                    }
                },
                {
                    "name": "PCG-\u5e7f\u544a\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,105,23)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,91,21)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,9,86)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,38,82)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6a21\u578b\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,68,19)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,82,65)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe-SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,61,126)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,39,129)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,86,122)"
                        }
                    }
                },
                {
                    "name": "05415O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,151,85)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,114,113)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,39,34)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,0,133)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,115,121)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,9,67)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u5e26\u534f\u8bae\u548c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,55,85)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,121,109)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,95,80)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,146,92)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,100,71)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,84,110)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,70,79)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u5e73\u53f0-\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,124,88)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7ed3\u6784\u5316\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,29,1)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5de5\u7a0b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,61,99)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f81\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,8,9)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,134,33)"
                        }
                    }
                },
                {
                    "name": "55414C-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,131,110)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,51,128)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,5,127)"
                        }
                    }
                },
                {
                    "name": "YAI-\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,125,24)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,120,64)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,72,132)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,103,36)"
                        }
                    }
                },
                {
                    "name": "BK32CA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,0,82)"
                        }
                    }
                },
                {
                    "name": "55413N-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,29,13)"
                        }
                    }
                },
                {
                    "name": "\u7269\u7406\u5c42\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,32,97)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,70,148)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,157,135)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,31,0)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,28,81)"
                        }
                    }
                },
                {
                    "name": "02426A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,152,103)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\uff08\u8bed\u8a00\u5efa\u6a21\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,122,18)"
                        }
                    }
                },
                {
                    "name": "11312H-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,73,116)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,142,101)"
                        }
                    }
                },
                {
                    "name": "11122M-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,36,149)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,45,24)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,66,73)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,117,23)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,131,105)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,14,66)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,74,160)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,84,94)"
                        }
                    }
                },
                {
                    "name": "55413Q-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,66,155)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,42,107)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,112,132)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,112,98)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,66,17)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,79,137)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,19,78)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,118,87)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,41,81)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5149\u8c31\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,7,64)"
                        }
                    }
                },
                {
                    "name": "\u7ec4\u5408\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,62,29)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,146,66)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,83,68)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22&\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,69,56)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,27,127)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,3,69)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,123,89)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,66,40)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,109,90)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,155,87)"
                        }
                    }
                },
                {
                    "name": "11122K-LT-310-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,123,102)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,156,157)"
                        }
                    }
                },
                {
                    "name": "1141BD-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,114,106)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,37,76)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u7814\u7a76\u5458/\u4e34\u5e8a\u7814\u7a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,84,126)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,83,110)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7d27\u6025\u5c97\u4f4d\u3011\u301095\u5206\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,146,68)"
                        }
                    }
                },
                {
                    "name": "AI\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,85,140)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,141,22)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,14,50)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,121,46)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,90,40)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,156,132)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,96,108)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,73,38)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,109,69)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,33,55)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,15,138)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,37,150)"
                        }
                    }
                },
                {
                    "name": "ASR/TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,9,45)"
                        }
                    }
                },
                {
                    "name": "11122N-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,98,1)"
                        }
                    }
                },
                {
                    "name": "11413B-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,44,9)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,60,91)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,71,133)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,28,149)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22/\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,41,136)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,9,20)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,20,3)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,47,48)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5065\u5eb7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,126,150)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,87,91)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u56fe\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,95,3)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,113,153)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,24,76)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,120,19)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,141,35)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,10,34)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,108,38)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,160,123)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,49,157)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\uff083D\u65b9\u5411\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,101,125)"
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
        chart_f46facd580db42a8aa05f03b4e92746e.setOption(option_f46facd580db42a8aa05f03b4e92746e);
    </script>
                <div id="20131a9d07984280a1fc2e1a71ca5db9" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_20131a9d07984280a1fc2e1a71ca5db9 = echarts.init(
            document.getElementById('20131a9d07984280a1fc2e1a71ca5db9'), 'white', {renderer: 'canvas'});
            
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
    
        var option_20131a9d07984280a1fc2e1a71ca5db9 = {
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
                            "color": "rgb(58,4,56)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 119,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,51,62)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 114,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,117,79)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 107,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,54,90)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,114,71)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,121,116)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,155,158)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,15,115)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,28,127)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,133,144)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,155,54)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,119,129)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,33,74)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,39,112)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,126,73)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,16,32)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,9,81)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,68,136)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,80,67)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,142,153)"
                        }
                    }
                },
                {
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,104,49)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,34,136)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,58,38)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,157,0)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,43,160)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,140,99)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,136,155)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,57,74)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,30,142)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,43,131)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,10,127)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,64,18)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,85,40)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,156,69)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,82,47)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,29,6)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,14,73)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,1,88)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,63,135)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,134,74)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,15,45)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,101,22)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,76,112)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,45,45)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,78,24)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,134,35)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,103,92)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,145,114)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,80,78)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,108,41)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,89,42)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,112,19)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,7,108)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,70,123)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,37,145)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,137,120)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,56,137)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,24,41)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,30,160)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,37,51)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,7,56)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,58,96)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,137,91)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,16,56)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,106,146)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,131,54)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u4f18\u79c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,104,67)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,23,30)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,100,83)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,159,114)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,79,158)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,69,143)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,130,153)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,101,86)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,119,34)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,48,14)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,104,130)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,26,26)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,127,14)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,71,151)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,78,30)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,9,158)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,152,60)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,1,65)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,91,41)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,134,22)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,38,90)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,24,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,156,79)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,3,84)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,45,146)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,125,135)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,15,116)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,132,116)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,3,111)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,45,62)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,43,88)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,53,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,47,49)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,123,57)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,17,117)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5e74\u7ec8",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,21,76)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,14,117)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,59,34)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,115,37)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,54,146)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,125,153)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,143,23)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,62,116)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,148,89)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,5,68)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,157,25)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,123,43)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,116,63)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,104,131)"
                        }
                    }
                },
                {
                    "name": "\u8bf1\u4eba\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,159,49)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,0,93)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,47,26)"
                        }
                    }
                },
                {
                    "name": "\u6025\u901f\u6210\u957f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,13,34)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,20,81)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,39,131)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,159,47)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,127,18)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,69,26)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929\u884c\u4e1a\u524d\u666f\u826f\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,102,78)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,66,119)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,8,89)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,76,131)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,98,42)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,107,96)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,38,61)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5f00\u516c\u6b63",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,30,105)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,130,147)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,106,34)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,26,39)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,150,131)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,10,158)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,141,33)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,49,107)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,22,7)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,13,4)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,10,133)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4e2d\u5fc3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,92,138)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,134,145)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,124,18)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,51,1)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,35,104)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,47,67)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,107,68)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,61,55)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,40,130)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f73",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,3,150)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,32,128)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,72,121)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,87,124)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,50,39)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,34,6)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,148,17)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u8865\u5145",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,100,9)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,53,128)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,61,26)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,41,102)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,133,125)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u53d1\u5c55\u7a7a\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,75,144)"
                        }
                    }
                },
                {
                    "name": "\u843d\u6237\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,27,59)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,71,128)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,115,140)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,106,105)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,43,109)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,43,130)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,14,47)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,2,112)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,35,52)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,37,82)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,142,90)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,2,5)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,99,140)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,158,1)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,32,10)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,95,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,140,119)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,16,120)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,85,126)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,96,152)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,47,32)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,59,140)"
                        }
                    }
                },
                {
                    "name": "8\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,34,154)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,9,108)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,126,33)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,113,30)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,155,1)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,8,53)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,1,85)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,13,79)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,21,119)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,88,85)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,75,18)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,111,114)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,129,160)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,143,103)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,87,16)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,148,91)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,59,145)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,22,93)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,120,82)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,150,98)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,88,142)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,128,93)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,35,120)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,132,137)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,156,149)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,31,33)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,60,9)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,29,141)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,83,28)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,119,74)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u4e1a\u52a1\u573a\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,90,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,33,97)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,47,136)"
                        }
                    }
                },
                {
                    "name": "\u65e0996",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,32,106)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,34,135)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,88,100)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,111,72)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,49,69)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,118,49)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u5b9e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,19,85)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,109,118)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,77,116)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,132,107)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,60)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,135,97)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u52b1\u5236",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,143,11)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,30,150)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,0,8)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,92,49)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u574718\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,78,29)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,29,158)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,55,147)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,72,57)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,145,83)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,43,98)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,61,72)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,21,49)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,128,47)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u652f\u6301\u7ed9\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,76,60)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,34,44)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,51,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,117,107)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,47,52)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u7b79\u5907",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,114,20)"
                        }
                    }
                },
                {
                    "name": "\u5bbf\u820d\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,107,140)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,126,143)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7cbe\u6e5b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,2,31)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,147,122)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,142,73)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5\u6838\u5fc3\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,119,80)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,15,89)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,135,81)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,72,60)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,61,127)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,27,148)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,53,55)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,99,50)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,107,136)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u56db\u6b21\u8bc4\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,79,144)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,140,0)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,109,18)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,79,22)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,20,31)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,86,68)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,30,65)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,113,74)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,54,144)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,138,142)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,81,32)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,90,107)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,59,130)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,19,10)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,39,8)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,31,43)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,21,55)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,112,38)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,85,65)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,19,98)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u6c1b\u56f4\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,115,130)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,20,145)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,114,122)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,64,114)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,142,76)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,62,73)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,29,34)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,138,112)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,2,45)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,111,91)"
                        }
                    }
                },
                {
                    "name": "\uff0858\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,79,152)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,74,48)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,128,82)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,29,155)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,130,73)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u9636\u8dc3\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,120,144)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,6,36)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,57,96)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,100,69)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u5f00\u653e\u73af\u5883",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,133,46)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,99,43)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,3,99)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,14,148)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,85,42)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,25,42)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,138,132)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,20,10)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,107,138)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u516c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,81,77)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,145,26)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,34,112)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,90,106)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,23,109)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,89,34)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u51fa\u6d77\u524d\u4e09",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,20,113)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185TOP3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,69,59)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,103,47)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,136,43)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7ebf\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,109,20)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,156,144)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,83,104)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,122,136)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,53,24)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,14,117)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,26,30)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,141,51)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1\u7cfb\u7edf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,123,126)"
                        }
                    }
                },
                {
                    "name": "16\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,49,144)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u6fc0\u60c5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,102,136)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f/\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,84,45)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,17,10)"
                        }
                    }
                },
                {
                    "name": "AI\u82af\u7247",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,84,73)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,119,45)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,46,33)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,9,93)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,135,33)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,64,118)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,133,30)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,46,76)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u578b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,49,146)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8d85\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,73,37)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5177\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u5f85\u9047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,72,158)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u65b0\u5174\u9886\u57df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,108,113)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,87,149)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236\u5ea6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,115,76)"
                        }
                    }
                },
                {
                    "name": "6\u96692\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,135,38)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,31,62)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,33,40)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,55,112)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,35,147)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5496\u5561",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,79,127)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u6709\u5b9e\u529b\u7684\u5927\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,144,140)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,47,149)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,62,131)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u751f\u65e5\u8282\u5047\u65e5\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,48,26)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u63d0\u4f9b\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,153,76)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,129,101)"
                        }
                    }
                },
                {
                    "name": "AI\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,81,156)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,122,129)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,112,133)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,117,17)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,126,65)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,95,139)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,5,101)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,80,29)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,149,24)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,9,80)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,59,71)"
                        }
                    }
                },
                {
                    "name": "\u989c\u503c\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,11,149)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,153,129)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,33,127)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u5e95\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,126,153)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u521b\u65b0\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,126,25)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,31,130)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,108,147)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,125,54)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,156,144)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,94,76)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u8005\u7ed9\u4e0e\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,44,130)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,0,43)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,16,60)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,100,135)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,14,60)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,149,119)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,120,27)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,155,148)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,56,67)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u5730\u94c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,42,140)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,62,137)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,78,127)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u9886\u5148\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,124,46)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,10,107)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,89,38)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,84,47)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,17,9)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u7a7a\u95f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,72,16)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u4f18\u6e25",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,28,71)"
                        }
                    }
                },
                {
                    "name": "Geek",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,98,113)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u8d8b\u52bf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,60,97)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5956\u91d1+\u80a1\u6743/\u671f\u6743\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,1,43)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,121,128)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,72,125)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,123,153)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,77,156)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8bafC\u8f6e\u9886\u6295",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,118,47)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,150,139)"
                        }
                    }
                },
                {
                    "name": "\u516d\u65e5\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,85,65)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,156,28)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,155,42)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,91,44)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,28,41)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,65,118)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,9,45)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,158,71)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,4,18)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,48,30)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,13,57)"
                        }
                    }
                },
                {
                    "name": "IOT\u9886\u5148\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,115,60)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,53,125)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,37,102)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,37,53)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,72,23)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,116,94)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,78,128)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9510\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,16,44)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,87,73)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u901a\u8054\u6570\u636e\u8054\u5408\u62db\u8058",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,25,11)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,137,105)"
                        }
                    }
                },
                {
                    "name": "\u745c\u4f3d\u5065\u8eab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,147,4)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0a\u5e02\u9884\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,118,132)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,44,40)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,17,141)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,9,132)"
                        }
                    }
                },
                {
                    "name": "*\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,112,88)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,160,39)"
                        }
                    }
                },
                {
                    "name": "\u7845\u8c37\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,33,24)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u52b2\u535a\u58eb\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,78,50)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,72,140)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4e2d\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,88,13)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,101,86)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,145,150)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,153,151)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,28,106)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,21,1)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u521b\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,63,59)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,99,21)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,118,68)"
                        }
                    }
                },
                {
                    "name": "80%\u8f6c\u6b63\u7387",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,159,28)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,133,39)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,7,122)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,131,0)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,46,49)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,103,158)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,70,160)"
                        }
                    }
                },
                {
                    "name": "\u671f\u5f85\u60a8\u7684\u52a0\u5165",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,61,1)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,63,2)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u9910\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,12,76)"
                        }
                    }
                },
                {
                    "name": "*\u6708\u5ea6\u7ee9\u6548\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,126,81)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,158,59)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,81,144)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,147,43)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,15,138)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,127,55)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,85,34)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1/\u5b63\u5ea6\u5956/\u5e26\u85aa\u5e74\u5047/\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,98,113)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,59,85)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,18,90)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,151,73)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,7,119)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,102,12)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,86,157)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,135,3)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,86,12)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u798f\u5229\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,7,92)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,95,149)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,79,10)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,84,84)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,151,26)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,77,155)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,0,88)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u6307\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,31,143)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,66,112)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,136,22)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,16,57)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,87,125)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,42,58)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,109,18)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,109,105)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5730\u5b66\u751f\u5b9e\u4e60\u6709\u4f4f\u5bbf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,126,83)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u957f\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,101,137)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,39,154)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,114,7)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,49,1)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u6c1b\u56f4\u4ff1\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,102,3)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,83,21)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u6587\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,156,113)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,64,120)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,129,140)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,13,16)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,136,19)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,66,139)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,135,73)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,73,9)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,39,68)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,119,66)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u4e0a\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,80,41)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,86,24)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,73,105)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,131,86)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,123,36)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,21,60)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u798f\u5229\u5e74\u5ea6\u4f53\u68c0\u52a0\u73ed\u8865\u52a9\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,67,91)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,48,6)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u8d70\u8fdb\u5343\u5bb6\u4e07\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,40,26)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,116,96)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f14\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,16,122)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,38,19)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u8d77\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,5,65)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,45,46)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,107,8)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,150,19)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f\u5e26\u85aa\u5e74\u5047\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,54,102)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,90,67)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u5747\u4e3a\u81ea\u52a8\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,76,15)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,139,50)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,131,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,131,69)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,77,67)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,63,93)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,25,121)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,106,16)"
                        }
                    }
                },
                {
                    "name": "CTO\u7b97\u6cd5\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,96,13)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,51,100)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u81ea\u6211\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,96,24)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,97,129)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,94,58)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51\u53cc\u8de8\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,148,158)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,86,16)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,23,89)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,32,147)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,119,0)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,45,42)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u5f88\u5f3a\u7684\u540c\u4e8b\u4e00\u8d77\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,151,127)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,20,38)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,114,100)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,107,148)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,71,137)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,25,105)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,153,58)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,120,42)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,120,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,112,3)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,20,91)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,136,65)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,151,115)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,131,152)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,149,89)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,59,49)"
                        }
                    }
                },
                {
                    "name": "\u7528\u524d\u6cbf\u6280\u672f\u53d8\u9769\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,121,114)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,132,70)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,136,112)"
                        }
                    }
                },
                {
                    "name": "\u65af\u5766\u798f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,102,110)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,76,105)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,46,136)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,11,118)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,123,21)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5bfc\u5e26\u961f\u7684\u6df1\u5ea6\u5b66\u4e60\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,159,56)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u57fa\u56e0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,8,135)"
                        }
                    }
                },
                {
                    "name": "\u65e0007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,35,87)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,151)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,90,95)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,40,83)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,115,68)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,129,81)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,45,141)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u6bcf\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,110,99)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,156,70)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,6,138)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6d3b\u5343\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,107,82)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,29,1)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,145,115)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,110,72)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,51,22)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,63,121)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u4e1a\u52a1\u5b89\u5168\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,111,102)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,145,91)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c0f\u5468",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,39,7)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,115,91)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,69,24)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5148\u7684\u4eba\u5de5\u667a\u80fd\u5b66\u4e60\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,148,106)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,125,24)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,154,32)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u804c\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,36,106)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,13,22)"
                        }
                    }
                },
                {
                    "name": "\u5305\u53cc\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,15,22)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1\u5168\u8d44\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,62,12)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,39,115)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u805a\u9910~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,19,44)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,97,21)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,130,8)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237\u7684\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,124,37)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,107,15)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,154,98)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,91,108)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,146,108)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,160,102)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8def\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,87,6)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,94,143)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,130,41)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,108,160)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,49,116)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,150,134)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u6700\u5927\u4e09\u65b9\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,65,54)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,39,93)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a\u6838\u5fc3\u4ea7\u54c1\uff08\u70ed\u641c\u699c\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,90,10)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u6c1b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,83,51)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,124,115)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,2,19)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,73,54)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,17,16)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,105,147)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u7a0b\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,45,92)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u548c\u80fd\u529b\u6210\u957f\u6027\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,94,6)"
                        }
                    }
                },
                {
                    "name": "\u961f\u53cb\u5948\u65af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,35,11)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u4e0e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,139,15)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,45,84)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u65b0\u9896",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,5,74)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,108,7)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,27,105)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,24,28)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,119,79)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,27,4)"
                        }
                    }
                },
                {
                    "name": "\u6784\u5efa\u4eba\u7c7b\u865a\u62df\u4e16\u754c\u65b0\u4f53\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,72,148)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,127,94)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,117,152)"
                        }
                    }
                },
                {
                    "name": "\u811a\u8e0f\u5b9e\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,111,129)"
                        }
                    }
                },
                {
                    "name": "\u9910\u901a\u8baf\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,82,135)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,33,7)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,81,60)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,79,17)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,104,120)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u89c4\u8303",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,71,19)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,70,87)"
                        }
                    }
                },
                {
                    "name": "\u603b\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,45,58)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b66\u4e60\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,102,159)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u5927\u4f6c\u4e00\u8d77\u53c2\u52a0\u56fd\u9645\u9876\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,73,35)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,67,67)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,26,115)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,145,102)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,28,89)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u9690\u5f62**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,54,152)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,63,12)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,29,104)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,119,62)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,87,82)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u65e5\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,157,101)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,138,120)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,30,15)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,148,110)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,135,69)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,141,56)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,112,129)"
                        }
                    }
                },
                {
                    "name": "\u5373\u5c06\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,141,49)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,107,55)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,26,12)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,66,31)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,90,123)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,107,41)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u5bfc\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,35,122)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,46,31)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,135,81)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,52,107)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,90,39)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,12,146)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,12,100)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,9,126)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,151,111)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,84,159)"
                        }
                    }
                },
                {
                    "name": "7\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,34,23)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f118\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,141,31)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,15,63)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5b9e\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,91,88)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,134,89)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,150,83)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,75,64)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,100,118)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,86,78)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,33,9)"
                        }
                    }
                },
                {
                    "name": "\u7075\u6d3b\u5de5\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,124,54)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,119,79)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,5,61)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,6,118)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u5168\u7403\u5316\u548c\u591a\u6d3b\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,43,2)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,63,24)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,117,146)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,105,146)"
                        }
                    }
                },
                {
                    "name": "\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,94,49)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,49,149)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,131,124)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,155,126)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,0,151)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u54c8\u5570\u51fa\u884c\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,21,33)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,78,93)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,68,159)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,81,26)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u81ea\u6211",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,74,30)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,123,61)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u6e20\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,8,144)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,50,71)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,93,128)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u679c\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,109,125)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,96,64)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,120,104)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,45,102)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,136,102)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,138,154)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5229\u4e8e\u53d1\u8bba\u6587",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,82,160)"
                        }
                    }
                },
                {
                    "name": "\u522b\u518d\u9519\u8fc7Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,73,99)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6742\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,124,38)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,37,43)"
                        }
                    }
                },
                {
                    "name": "AI\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,149,75)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df10+\u7ecf\u9a8c\u7b97\u6cd5\u548cC++\u7684\u53cc\u5bfc\u5e08\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,56,149)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u4ea4\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,50,53)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,143,141)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e0e\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,59,127)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,131,152)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,149,95)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,155,123)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148\u5546\u7528\u670d\u52a1\u673a\u5668\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,28,10)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,28,33)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,60,102)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,58,31)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,139,157)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,130,0)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,149,15)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,37,26)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,85,70)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u63a5\u8ddf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,11,2)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6837\u5316\u7684\u5b66\u4e60\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,110,8)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u9f50\u805a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,40,7)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,7,118)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,2,105)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,15,159)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,76,132)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,115,106)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u5927\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,131,28)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,25,112)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,144,15)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,64,154)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e24\u4f4d\u79d1\u5b66\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,150,118)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u7ee9\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,34,57)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,44,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,38,24)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u826f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,45,77)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u754c\u4e0e\u5b66\u672f\u754c\u76f8\u7ed3\u5408\u7684\u6700\u4f73\u9635\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,45,103)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,104,40)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,10,65)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,149,58)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,41,102)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,22,80)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,25,30)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,80,154)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,7,74)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u884c\u4e1a\u524d\u666f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,47,96)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,117,10)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,75,121)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,121,97)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,34,54)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,66,147)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,54,152)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\uff1a\u957f\u671f\u6280\u672f\u79ef\u6dc0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,42,21)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u63a5\u89e6\u4e1a\u754c\u6700\u524d\u6cbf\u4eba\u5de5\u667a\u80fd\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,102,124)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,52,126)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,44,34)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,97,94)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,125,47)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,85,136)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,106,140)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21review\u664b\u5347\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,92,85)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e94\u8fbe\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,119,3)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u8fd1\u767e\u4ebf\u7f8e\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,54,64)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,64,94)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,3,124)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u6ee1\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,36,127)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,131,19)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,104,86)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,53,14)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u83b7\u5f97\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,151,134)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7f51\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,64,46)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,130,64)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,84,37)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,61,34)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,78,25)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u505c\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,30,43)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,124,12)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,146,154)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,147,160)"
                        }
                    }
                },
                {
                    "name": "\u7f34\u7eb3\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,36,142)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,117,75)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,142,62)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,110,92)"
                        }
                    }
                },
                {
                    "name": "\u5076\u5c14\u52a0\u73ed\u8c03\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,124,66)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u77bb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,32,89)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,109,99)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,138,108)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,37,41)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7b49\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,104,70)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,141,130)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53/\u7535\u89c6\u53f0/\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,112,120)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,3,66)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u6caa\u676d\u5747\u6709hc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,39,33)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,28,129)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,7,125)"
                        }
                    }
                },
                {
                    "name": "\u624e\u624e\u5b9e\u5b9e\u505a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,20,74)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,0,134)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,24,26)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,140,21)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,99,63)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,104,35)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,103,14)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,0,104)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7528\u8fd0\u7b79\u4f18\u5316\u77e5\u8bc6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,123,118)"
                        }
                    }
                },
                {
                    "name": "\u9769\u65b0\u7684\u9879\u76ee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,5,48)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,159,35)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,75,75)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5185\u9f99\u5934\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,17,29)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,93,42)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e00\u4ee3\u6587\u5a31\u98ce\u53e3\u9886\u822a\u8005",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,101,19)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,21,71)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,101,45)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,113,119)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,157,30)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,40,17)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,135,41)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,24,26)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,118,139)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,129,74)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,53,149)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u676d\u5dde\u5b9e\u5728\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,118,80)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,63,113)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53e3\u7891\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,151,45)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,87,134)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,148,154)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u6211\u53d1\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,15,4)"
                        }
                    }
                },
                {
                    "name": "\u5df2\u83b7\u591a\u5bb6\u4e00\u7ebfVC\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,56,101)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,66,53)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNic",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,80,112)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6709\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,24,41)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9738",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,52,116)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,64,151)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,80,24)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,137,68)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,53,50)"
                        }
                    }
                },
                {
                    "name": "1.\u56e2\u961f\u4e1a\u52a1\u7d27\u8ddf\u96c6\u56e2\u7684\u4e1a\u52a1\u76ee\u6807",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,135,149)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,37,138)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u5883\u5962\u4f88\u54c1\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,134,28)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,144,50)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,102,38)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0d\u5dee\u94b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,142,79)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,131,158)"
                        }
                    }
                },
                {
                    "name": "\u590d\u6742\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,15,14)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,90,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,147,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,79,29)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,54,108)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,126,6)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,91,75)"
                        }
                    }
                },
                {
                    "name": "\u6709\u66f4\u9ad8\u66f4\u5927\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,149,59)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u540d\u6821\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,146,98)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,61,104)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u81f4\u8212\u9002\u7684\u529e\u516c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,1,30)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,108,82)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,48,138)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,44,20)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,61,12)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,50,146)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,43,97)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,160,87)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,46,22)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,147,30)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,119,109)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,122,113)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,46,6)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,0,38)"
                        }
                    }
                },
                {
                    "name": "\u3010\u611f\u77e5\u9636\u8dc3\u3011\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,79,88)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,119,84)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,66,42)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,101,137)"
                        }
                    }
                },
                {
                    "name": "\u6574\u4f53\u89e3\u51b3\u65b9\u6848\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,114,71)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4e07DAU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,82,125)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,33,125)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,4,103)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u573a\u9762\u8bd5\u6d41\u7a0b\u4e00\u6b21\u8d70\u5b8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,55,21)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,5,80)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,18,21)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,12,133)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,57,96)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,99,4)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,88,93)"
                        }
                    }
                },
                {
                    "name": "\u6709\u7ade\u8d5b\u83b7\u5956\u7ecf\u9a8c\u4f18\u5148\u8003\u8651",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,0,113)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,59,21)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4eba\u624d\u4f4f\u623f\u63d0\u4f9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,65,61)"
                        }
                    }
                },
                {
                    "name": "C\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,117,111)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,53,91)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56e2\u961f\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,42,100)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u6027\u7684\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,71,158)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,56,112)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,18,86)"
                        }
                    }
                },
                {
                    "name": "\u6210\u719f\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,12,151)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,51,125)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u6da8\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,17,17)"
                        }
                    }
                },
                {
                    "name": "\u4eab\u6709\u80a1\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,80,36)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916SaaS\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,150,53)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,126,69)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,87,158)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e00\u6863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,106,144)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,19,98)"
                        }
                    }
                },
                {
                    "name": "\u83b7\u591a\u5bb6**\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,154,25)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,26,86)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,17,101)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u798f\u5229\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,98,91)"
                        }
                    }
                },
                {
                    "name": "\u5145\u6ee1\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,76,142)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,131,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,57,94)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,118,55)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,90,79)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,29,157)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u7b97\u6cd5\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,110,15)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,8,35)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,97,33)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u5927\u4f6c\u5e26\u4f60\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,10,98)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,115,70)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,59,152)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,90,110)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,79,140)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,85,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,28,55)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,11,122)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,49,78)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,95,52)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,86,62)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,41,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,151,131)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,110,159)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,138,125)"
                        }
                    }
                },
                {
                    "name": "NICE\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,137,13)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,98,138)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u590d\u6742",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,52,119)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u770b\u597d\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,1,68)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,21,114)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u7684\u56e2\u961f\u5de5\u7a0b\u548c\u7b97\u6cd5\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,6,85)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,51,60)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,53,140)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u5feb\u624b\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,90,54)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,44,33)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u4f18\u5f02\u7684\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,127,57)"
                        }
                    }
                },
                {
                    "name": "6\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,68,42)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,86,10)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,9,106)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,125,159)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,86,34)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,153,102)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,125,0)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,96,3)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,63,50)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,158,3)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,75,60)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,4,42)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,49,101)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,19,146)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,118,34)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u538b\u529b\u5c0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,135,157)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,72,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6587\u6863\u968f\u4fbf\u770b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,55,117)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,76,70)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,56,76)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f83\u597d\u7684\u8d44\u6e90\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,159,141)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,119,47)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,23,31)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,78,33)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,96,135)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,1,18)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,121,67)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,118,84)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,9,42)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,132,157)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,11,42)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9879\u76ee\u7814\u7a76\u524d\u6cbf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,61,102)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79ef\u91d1\u5168\u989d\u6700\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,24,83)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5f02\u8005\u53ef\u8f6c\u6821\u62db\u6b63\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,6,44)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,5,82)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,98,79)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,109,2)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u8fc5\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,28,72)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u725b\u4e91\u96c6\u9879\u76ee\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,103,29)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,150,122)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,7,140)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,84,120)"
                        }
                    }
                },
                {
                    "name": "\u6587\u827a\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,102,122)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u533b\u7597\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,88,83)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,49,21)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u7ee9\u4f18\u79c0+\u5e74\u7ec8\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,56,3)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,18,72)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,110,22)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,132,45)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,54,53)"
                        }
                    }
                },
                {
                    "name": "\u80cc\u666f\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,119,118)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u5907\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,142,67)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,71,57)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,99,127)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u5019\u9009\u4eba\u53ef\u4ee5\u6210\u4e3a\u6280\u672f\u5408\u4f19\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,82,70)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,116,94)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,160,87)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,78,101)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,24,133)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,103,85)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9614\u51ed\u9c7c\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,8,137)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,153,40)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,63,59)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8bf1\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,70,120)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,75,7)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,99,20)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6e\u5c97\u6216\u8f6c\u5c97\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,144,129)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,83,133)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe\u6838\u5fc3\u4e1a\u52a1\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,121,75)"
                        }
                    }
                },
                {
                    "name": "\u9876\u683c\u4f4f\u623f\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,142,129)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,97,18)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,135,140)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,82,126)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,25,39)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,99,117)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,41,160)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u4f5c\u4e3a\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,141,29)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,36,156)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,40,12)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,108,158)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,58,33)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,12,67)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,22,4)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u7ea7\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,13,47)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1aAI\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,16,24)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,108,51)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,158,69)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,156,24)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,29,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,90,77)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,71,153)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,28,120)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,52,95)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,68,123)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,141,87)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,23,73)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,125,21)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u50478\u5929\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,34,126)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,130,122)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,51,106)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,116,86)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,20,160)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,140,125)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,39,19)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u767e\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,137,5)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,40,74)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,103,39)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,27,159)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,84,62)"
                        }
                    }
                },
                {
                    "name": "**\u533b\u9662\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,109,125)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,116,32)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u5236\u8f83\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,120,16)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,153,148)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,123,122)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5\u9a71\u52a8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,18,78)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,135,19)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u516c\u53f8\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,53,151)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u7b49\u884c\u4e1a\u6700\u4f18\u79c0\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,79,2)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,78,52)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,101,3)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,132,26)"
                        }
                    }
                },
                {
                    "name": "\u5929\u9ad8\u4efb\u9e1f\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,90,61)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,12,4)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u5047\u65e5\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,5,102)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,104,12)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4eba\u5458300\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,64,92)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,89,71)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u9886\u57df\u7814\u53d1\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,70,5)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,125,0)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,59,35)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,149,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d8520\u5e74\u76f8\u5173\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,109,156)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,23,131)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4up",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,5,4)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df\u7684\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,50,32)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,6,53)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,124,90)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,83,155)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,79,8)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,14,154)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,3,1)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,131,111)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,0,136)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,35,11)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u540c\u884c\u4e1a\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,36,133)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,79,143)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,60,124)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,16,86)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,110,106)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u7684\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,136,43)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u6280\u672f\u4ea4\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,135,63)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,54,24)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,147,29)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,108,75)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,45,149)"
                        }
                    }
                },
                {
                    "name": "\u6709\u826f\u597d\u7684\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,9,65)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,47,41)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,48,102)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,95,11)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,129,65)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,45,95)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,26,133)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u6216\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,53,126)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u98ce\u63a7\u5782\u76f4\u9886\u57df\u6df1\u5ea6\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,106,97)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,92,40)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53e3\u5348\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,15,27)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d1f\u8d23\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,36,109)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,28,97)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,143,155)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u4f6c\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,60,20)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,10,88)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,113,108)"
                        }
                    }
                },
                {
                    "name": "0-1\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,74,99)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,27,54)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,141,66)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,58,127)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,119,96)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,29,160)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,25,102)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u5458\u5de5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,14,61)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,18,48)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,52,105)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,104,112)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,79,76)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,112,4)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,8,102)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,40,87)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,82,140)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,75,39)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,64,127)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u673a\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,55,65)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,77,128)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,46,44)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530CBD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,82,51)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,65,137)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u7f34\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,110,156)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,65,84)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u5e73\u53f0\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,145,10)"
                        }
                    }
                },
                {
                    "name": "12%\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,90,133)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,144,71)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,88,70)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,138,128)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,47,50)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,105,3)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,157,27)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,19,131)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,49,20)"
                        }
                    }
                },
                {
                    "name": "14-18\u85aa+\u4e30\u539a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,129,108)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,38,43)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,13,48)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,27,92)"
                        }
                    }
                },
                {
                    "name": "\u653f\u5e9c\u91cd\u70b9\u652f\u6301\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,26,88)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,137,77)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,36,110)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,16,107)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbfAR\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,111,36)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,8,100)"
                        }
                    }
                },
                {
                    "name": "007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,23,27)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,120,75)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u5e26\u65b0\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,3,64)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,48,31)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,2,84)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,94,112)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,129,68)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,107,83)"
                        }
                    }
                },
                {
                    "name": "CBA\u660e\u661f\u521b\u4e1a\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,8,70)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,148,83)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,123,14)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80a1\u4e1c\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,73,23)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u81ea\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,145,30)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,5,36)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,111,58)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,44,105)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,157,92)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u7cbe\u6e5b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,62,62)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,147,129)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,91,72)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5148\u8fdb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,37,111)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,120,99)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,98,6)"
                        }
                    }
                },
                {
                    "name": "\u7535\u89c6\u53f0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,28,33)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,141,70)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u4e24\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,153,54)"
                        }
                    }
                },
                {
                    "name": "\u548c\u8c10\u7684\u56e2\u961f\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,100,6)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,63,93)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,63,134)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,100,147)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u60a8\u52a0\u5165\u4e00\u70b9\u5927\u5bb6\u5ead~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,66,26)"
                        }
                    }
                },
                {
                    "name": "\u5404\u7c7b\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,14,122)"
                        }
                    }
                },
                {
                    "name": "\u5177\u89c4\u6a21\u7684\u5927\u6570\u636e\u5e73\u53f0\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,77,122)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,140,40)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,27,37)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,158,54)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,92,92)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,46,48)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,86,74)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,58,136)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,106,28)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,6,156)"
                        }
                    }
                },
                {
                    "name": "\u91c7\u7f16\u5236\u64ad\u5b58",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,78,84)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,82,86)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,151,15)"
                        }
                    }
                },
                {
                    "name": "\u9662\u58eb\u5e26\u961f\u53c2\u4e0e\u9ad8\u6821\u8054\u5408\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,139,127)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,23,94)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,39,155)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,78,107)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,41,87)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,76,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,60,22)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,62,108)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,152,108)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,137,57)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,157,39)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,158,14)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,29,135)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,157,146)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,133,30)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,149,153)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,48,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5c0f\u800c\u7cbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,89,51)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u6709\u7231\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,119,133)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,149,29)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,107,66)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,84,131)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,127,60)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,37,77)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,43,158)"
                        }
                    }
                },
                {
                    "name": "\u643a\u624b\u594b\u6597\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,88,44)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,107,101)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,48,6)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,26,150)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,125,144)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,17,9)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,38,79)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u8bd5\u7528\u671f\u540c\u85aa\u4e94\u9669\u4e00\u91d1\u957f\u671f\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,31,102)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,37,109)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,73,80)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,49,37)"
                        }
                    }
                },
                {
                    "name": "Pro\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,134,45)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669\u7b49\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,31,105)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,151,17)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,2,156)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u975e\u5e38\u597d\u3002\u5458\u5de5\u85aa\u8d44\u798f\u5229\u5f88\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,108,8)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u578b\u7ec4\u7ec7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,99,47)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u6c7d\u8f66\uff08\u730e\u5934\u5c97\u4f4d\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,58,146)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403**\u79d1\u5b66\u5bb6\u8ddf\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,44,61)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,137,119)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,156,87)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,155,19)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,93,81)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,75,150)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,121,122)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u4eba\u5458\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,106,95)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,40,69)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,134,120)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u80fd\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,17,23)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,59,4)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u8d44\u672c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,145,4)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,135,126)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,160,149)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,101,72)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d\u79d1\u6280\u5934\u90e8\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,26,57)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,132,134)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8d85\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,111,85)"
                        }
                    }
                },
                {
                    "name": "\u5171\u540c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,133,132)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,69,132)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,155,20)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5f71\u50cf\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,49,83)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7814\u53d1\u4eba\u6570\u5360\u6bd470%",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,96,83)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,109,135)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,160,20)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u9971\u6ee1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,157,136)"
                        }
                    }
                },
                {
                    "name": "\u3010\u8304\u5b50\u5feb\u4f20\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,60,8)"
                        }
                    }
                },
                {
                    "name": "15-20\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,43,57)"
                        }
                    }
                },
                {
                    "name": "\u56db\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,146,130)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,10,115)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u52a0\u73ed\u4e09\u500d\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,142,34)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,52,120)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,46,30)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,20,51)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,31,37)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,145,101)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,94,122)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,1,72)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,116,116)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,67,98)"
                        }
                    }
                },
                {
                    "name": "\u5171\u521b\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,18,160)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5bfc\u8d2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,144,104)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u6709\u529b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,91,29)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,47,126)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5f88\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,11,134)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,139,72)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d\u9886\u57df\u524d\u6cbf\u7b97\u6cd5\u7814\u7a76\u548c\u5b9e\u73b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,11,5)"
                        }
                    }
                },
                {
                    "name": "\u6ce8\u91cd\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,98,12)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u5173\u8054\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,66,27)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,111,14)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0/\u5f39\u6027\u4e0a\u4e0b\u73ed/\u5e74\u7ec8\u7ee9\u6548/\u514d\u8d39\u5348\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,141,3)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,58,57)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,156,80)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,2,12)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,124,130)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u81ea\u52a9\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,145,45)"
                        }
                    }
                },
                {
                    "name": "**\u6295\u8d44\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,70,19)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,64,92)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,120,34)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u548c\u5e26\u85aa\u75c5\u5047\u540415\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,109,133)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,64,96)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,3,115)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,71,128)"
                        }
                    }
                },
                {
                    "name": "\u9519\u8fc7\u4e8610\u5e74\u7684\u624b\u6dd8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,111,140)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,112,6)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,70,53)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u4e2a\u5c97\u4f4d\u6210\u5c31\u4e00\u756a\u4e8b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,114,117)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,124,65)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5c0f\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,42,31)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u591a\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,58,101)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,145,126)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,6,88)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,23,83)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u7d22\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,123,158)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u8d44\u6e90\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,146,115)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,13,37)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,144,114)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,145,59)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,89,149)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,80,104)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,97,92)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,83,92)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u9988\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,9,5)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u52a8\u4e2d\u56fd\u533b\u7597\u6539\u53d8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,44,110)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u96c6\u7fa4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,86,82)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,41,4)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,29,110)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,77,134)"
                        }
                    }
                },
                {
                    "name": "Mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,70,20)"
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
        chart_20131a9d07984280a1fc2e1a71ca5db9.setOption(option_20131a9d07984280a1fc2e1a71ca5db9);
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
