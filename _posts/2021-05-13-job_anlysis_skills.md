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

<h2>（2021-05-22更新）</h2>

<h2>点击按钮查看招聘数据分析详情</h2>
    
<a href="https://showmeai-hub.github.io/2021/05/22/job_data_anlysis.html">
    <button class="button">看薪资</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/22/job_anlysis_company.html">
    <button class="button">看公司</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/22/job_anlysis_skills.html">
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
            <button class="tablinks" onclick="showChart(event, '7a4d6851a9e24c9a8c1d9cdb5fe0df87')">关键词</button>
            <button class="tablinks" onclick="showChart(event, '973d199f676b49d38b93f6989d1576b3')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, '5eab0ffffa3e4aa7897fbab834ca9557')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, 'd2b12f4847ff41c7bb2fc461621bd191')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, 'b05c09e8490a46dbae125e30de76ee79')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '10a03dbe60fc472fbe14b0cd8e2de4e3')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'e561366355cc47fe9485f523bb6ac255')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'bde6c5cf2b794a43b4a20968862bb7e0')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'cceea831045e4ec490ceb8e15cafa387')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '7a1f26c716b74dd4bfadf917bb1d6b2a')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="7a4d6851a9e24c9a8c1d9cdb5fe0df87" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_7a4d6851a9e24c9a8c1d9cdb5fe0df87 = echarts.init(
            document.getElementById('7a4d6851a9e24c9a8c1d9cdb5fe0df87'), 'white', {renderer: 'canvas'});
            
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
    
        var option_7a4d6851a9e24c9a8c1d9cdb5fe0df87 = {
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
                576,
                288,
                235,
                192,
                164,
                157,
                154
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
                    "value": 576,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,117,131)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 288,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,21,78)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 235,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,126,9)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 192,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,18,114)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 164,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,12,42)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 157,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,111,101)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,72,0)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,101,115)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 153,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,60,149)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,59,87)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,22,106)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,51,151)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,105,101)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,85,41)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,11,150)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,19,16)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,103,143)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,29,157)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,57,111)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,124,57)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,71,19)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,63,44)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,73,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,160,46)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,129,120)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,122,13)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,100,65)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,120,86)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,9,107)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,49,148)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,73,154)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,160,39)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,26,28)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,33,77)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,102,56)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,86,155)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,64,16)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,129,87)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,2,160)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,144,57)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,114,95)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,7,115)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,59,86)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,11,89)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,92,101)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,78,52)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,95,51)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,100,44)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,6,93)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,100,15)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,52,24)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,39,82)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,8,3)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,132,102)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,66,63)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,86,128)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,12,43)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,145,46)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,65,159)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,35,55)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,22,82)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,9,67)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,157,0)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,113,99)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,149,19)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,76,68)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,62,140)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,97,142)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,64,0)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,106,11)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,57,68)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,99,53)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,56,39)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,11,94)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,92,139)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,101,152)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,155,123)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,27,83)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,21,32)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,44,123)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,105,112)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,105,68)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,0,114)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,85,27)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,134,57)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,69,127)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,64,157)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,36,42)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,98,37)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,71,111)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,73,129)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,46,25)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,13,31)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,107,68)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,86,11)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,113,122)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,28,2)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,97,159)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,39,11)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,21,65)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,15,75)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,113,27)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,47,91)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,14,149)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,113,52)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,130,23)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,116,83)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,111,13)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,48,33)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,4,44)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,43,154)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,102,75)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,10,6)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,5,156)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,108,40)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,148,70)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,126,148)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,113,10)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,119,127)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,102,128)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,89,16)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,85,118)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,149,131)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,44,3)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,65,13)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,3,116)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,4,33)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,143,60)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,80,112)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,74,90)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,111,105)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,90,31)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,81,38)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,88,85)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,26,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,52,1)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,112,156)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,108,50)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,0,89)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,71,154)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,59,108)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,157)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,27,134)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,38,130)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,92,44)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,41,16)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,49,151)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,128,123)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,109,4)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,145,125)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,93,101)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,157,104)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,121,85)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,28,97)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,144,62)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,154,135)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,145,2)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,124,14)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,60,13)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,65,38)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,115,13)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,60,54)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,136,18)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,104,138)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,101,20)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,58,139)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,40,63)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,96,23)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,67,10)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,46,148)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,129,34)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,34,45)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,103,77)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,94,20)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,77,100)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,36,137)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,77,121)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,29,118)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,62,129)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,116,118)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,32,131)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,130,22)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,154,78)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,24,7)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,104,57)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,67,29)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,97,46)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,25,143)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,25,145)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,72,105)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,152,151)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,110,129)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,139,67)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,129,67)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,53,14)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,81,74)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,112,21)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,124,68)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,74,61)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,13,153)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,71,79)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,45,159)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,135,105)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,102,1)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,36,23)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,18,146)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,82,137)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,63,108)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,41,145)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,63,146)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,115,56)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,138,160)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,64,146)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,157,86)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,19,44)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,72,48)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,118,95)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,150,13)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,58,107)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,22,75)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,19,58)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,154,5)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,144,84)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,130,57)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,134,29)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,69,109)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,88,86)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,105,8)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,123,41)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,145,127)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,103,22)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,70,114)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,24,89)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,140,152)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,65,124)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,45,53)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,48,141)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,102,93)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,53,31)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,15,124)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,159,111)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,104,91)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,131,159)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,117,39)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,149,65)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,98,6)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,100,69)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,22,148)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,28,0)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,120,28)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,86,103)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,147,92)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,57,28)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,92,157)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,79,117)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,148,138)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,137,50)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,38,52)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,117,28)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,24,35)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,132,105)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,118,19)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,3,105)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,114,33)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,51,80)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,45,15)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,33,12)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,36,95)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,62,0)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,43,3)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,71,159)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,19,63)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,19,115)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,32,152)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,80,24)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,146,90)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,145,12)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,109,121)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,111,60)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,149,99)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,64,140)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,107,24)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,40,58)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,145,90)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,15,53)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,25,75)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6001\u89c4\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,74,131)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,44,39)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,131,136)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,56,27)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,134,97)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,133,103)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,68,143)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,81,45)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,151,138)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,142,43)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,26,137)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,148,87)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,0,62)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,0,45)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,79,58)"
                        }
                    }
                },
                {
                    "name": "go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,88,152)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,5,111)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,99,26)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,29,123)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,43,150)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,17,59)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,43,37)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,49,122)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,60,88)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,96,155)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,80,40)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,57,144)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,67,118)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,85,26)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,61,127)"
                        }
                    }
                },
                {
                    "name": "JavaScript",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,12,137)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,16,50)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,25,23)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,124,128)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,95,144)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,49,36)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,14,6)"
                        }
                    }
                },
                {
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,97,135)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,4,12)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,132,103)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,74,83)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,66,98)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,82,78)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,52,13)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,73,73)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,136,24)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,87,5)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,49,87)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,92,90)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,49,106)"
                        }
                    }
                },
                {
                    "name": "FPGA\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,35,137)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,138,125)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,104,138)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,75,22)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,66,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,103,81)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,26,79)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u66fe\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,34,36)"
                        }
                    }
                },
                {
                    "name": "automak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,15,68)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,27,75)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,59,19)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,150,11)"
                        }
                    }
                },
                {
                    "name": "rank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,4,34)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,34,115)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,79,39)"
                        }
                    }
                },
                {
                    "name": "DICOM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,47,66)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,122,124)"
                        }
                    }
                },
                {
                    "name": "shell",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,45,35)"
                        }
                    }
                },
                {
                    "name": "isp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,132,70)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,96,46)"
                        }
                    }
                },
                {
                    "name": "ensorFlow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,55,76)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,14,107)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,28,60)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6cca\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,23,14)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,7,7)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,68,116)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,155,151)"
                        }
                    }
                },
                {
                    "name": "torch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,99,41)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,46,91)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,32,68)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,52,154)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,122,110)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,75,74)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,100,79)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,145,62)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51+",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,151,57)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,37,29)"
                        }
                    }
                },
                {
                    "name": "\u524d\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,116,22)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,96,135)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,83,138)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,118,10)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,137,94)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,45,146)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,39,79)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,141,16)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,4,48)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,49,29)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u7167\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,0,22)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,152,146)"
                        }
                    }
                },
                {
                    "name": "\u7535\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,58,93)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,107,83)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,112,33)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,2,64)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,2,111)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,83,108)"
                        }
                    }
                },
                {
                    "name": "caffe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,110,83)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,6,127)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,90,99)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,151,31)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,12,111)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,134,37)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,41,32)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,42,150)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,9,35)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,132,96)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,14,54)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,35,96)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,105,39)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,2,101)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,41,138)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,104,25)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,95,9)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,18,87)"
                        }
                    }
                },
                {
                    "name": "MIMO\u96f7\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,54,155)"
                        }
                    }
                },
                {
                    "name": "\u70df\u96fe\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,129,133)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,111,35)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,32,126)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,59,107)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,114,94)"
                        }
                    }
                },
                {
                    "name": "hive",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,115,140)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,107,106)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u8fd0\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,87,71)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,106,42)"
                        }
                    }
                },
                {
                    "name": "\u5ba4\u5185\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,152,124)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee/\u53cc\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,139,16)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,74,46)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,27,77)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,131,149)"
                        }
                    }
                },
                {
                    "name": "\u6c42\u89e3\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,8,109)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u9884\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,118,94)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,134,156)"
                        }
                    }
                },
                {
                    "name": "\u4eea\u5668\u4eea\u8868",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,142,26)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,104,58)"
                        }
                    }
                },
                {
                    "name": "3d\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,120,22)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,102,64)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u89c6\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,112,102)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,101,97)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,67,149)"
                        }
                    }
                },
                {
                    "name": "PUSH\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,107,96)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,83,116)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,57,25)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,87,27)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,36,88)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,98,70)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,122,40)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u7ed8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,72,95)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,70,78)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,20,35)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,91,131)"
                        }
                    }
                },
                {
                    "name": "\u9009\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,98,140)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,79,91)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,120,69)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,28,58)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,118,12)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,146,36)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,12,20)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,95,26)"
                        }
                    }
                },
                {
                    "name": "Oracle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,94,46)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,79,122)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,135,109)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,154,112)"
                        }
                    }
                },
                {
                    "name": "cmake",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,72,92)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,127,141)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,45,143)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,56,55)"
                        }
                    }
                },
                {
                    "name": "SQLServer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,75,41)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,111,68)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,23,109)"
                        }
                    }
                },
                {
                    "name": "AlphaGo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,53,32)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,111,76)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,114,19)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,120,90)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u5b58\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,114,91)"
                        }
                    }
                },
                {
                    "name": "\u9891\u8c31\u76d1\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,117,28)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,146,115)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,149,109)"
                        }
                    }
                },
                {
                    "name": "labview",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,84,142)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,132,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,41,79)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,124,18)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,34,42)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,145,128)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,89,107)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,127,37)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,49,151)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,3,117)"
                        }
                    }
                },
                {
                    "name": "openGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,132,68)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,64,22)"
                        }
                    }
                },
                {
                    "name": "O2O",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,97,31)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,160,57)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,53,8)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,97,133)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,87,64)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,143,87)"
                        }
                    }
                },
                {
                    "name": "BFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,63,65)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,16,125)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,154,149)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,50,114)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,98,3)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,89,127)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,59,20)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,39,138)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,46,100)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,7,52)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,12,159)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,136,36)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,115,70)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,57,4)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,27,39)"
                        }
                    }
                },
                {
                    "name": "Pthon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,125,63)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,137,109)"
                        }
                    }
                },
                {
                    "name": "\u914d\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,1,28)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,24,106)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,16,49)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u9002\u5e94",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,136,94)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,104,30)"
                        }
                    }
                },
                {
                    "name": "FPGA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,138,1)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,33,114)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,155,79)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,149,105)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,124,5)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,150,0)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,108,121)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,30,11)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,54,114)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,97,81)"
                        }
                    }
                },
                {
                    "name": "AEC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,112,56)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,68,65)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,97,37)"
                        }
                    }
                },
                {
                    "name": "filnk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,72,78)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u7259",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,47,57)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,36,82)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,96,62)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,80,61)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,61,43)"
                        }
                    }
                },
                {
                    "name": "\u98de\u884c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,143,80)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,134,83)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,155,107)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,86,59)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u6210\u7535\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,60,32)"
                        }
                    }
                },
                {
                    "name": "\u753b\u50cf\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,103,36)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,83,46)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,31,27)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,132,38)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,141,127)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,90,145)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,102,40)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,125,56)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,158,89)"
                        }
                    }
                },
                {
                    "name": "\u9a71\u52a8\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,38,59)"
                        }
                    }
                },
                {
                    "name": "vSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,73,29)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,69,31)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,37,16)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,1,106)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,44,101)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,123,132)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u51c6\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,31,26)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,145,15)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,110,115)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,134,22)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,38,49)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,7,6)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,2,86)"
                        }
                    }
                },
                {
                    "name": "\u6821\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,160,131)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,146,76)"
                        }
                    }
                },
                {
                    "name": "\u7edf\u8ba1\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,27,77)"
                        }
                    }
                },
                {
                    "name": "rpc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,12,18)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,128,128)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,19,123)"
                        }
                    }
                },
                {
                    "name": "CRNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,33,13)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,78,158)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,107,118)"
                        }
                    }
                },
                {
                    "name": "Avatar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,47,15)"
                        }
                    }
                },
                {
                    "name": "Cortex-M\u6838",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,114,39)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,121,128)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,81,63)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,53,84)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,157,99)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,150,104)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,34,73)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,0,134)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,140,50)"
                        }
                    }
                },
                {
                    "name": "\u6846\u67b6\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,21,104)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,78,85)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,134,23)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,117,71)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,76,60)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,10,142)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,84,17)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,79,155)"
                        }
                    }
                },
                {
                    "name": "IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,114,1)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,31,38)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7a7f\u6234",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,108,9)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,71,122)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,55,61)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,69,144)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,118,18)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,28,52)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,108,136)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,4,87)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,124,62)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,123,75)"
                        }
                    }
                },
                {
                    "name": "NR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,132,4)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,155,118)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,65,131)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,31,153)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,91,145)"
                        }
                    }
                },
                {
                    "name": "AB\u5206\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,26,68)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,1,48)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,140,67)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,49,26)"
                        }
                    }
                },
                {
                    "name": "\u6807\u5b9a\u7f16\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,56,124)"
                        }
                    }
                },
                {
                    "name": "Fliter",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,73,114)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,121,86)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,149,13)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,120,1)"
                        }
                    }
                },
                {
                    "name": "WIFI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,146,105)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,73,56)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,128,79)"
                        }
                    }
                },
                {
                    "name": "OpenMesh",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,129,23)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,108,99)"
                        }
                    }
                },
                {
                    "name": "vivado",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,142,73)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,74,3)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,57,132)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,5,149)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,102,87)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,108,140)"
                        }
                    }
                },
                {
                    "name": "MDP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,114,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5377\u79ef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,117,98)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,125,87)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,106,43)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,67,40)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,7,30)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,80,112)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,34,7)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,74,23)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,108,5)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,41,58)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,122,29)"
                        }
                    }
                },
                {
                    "name": "AI\u8d85\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,100,103)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,16,23)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,86,71)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,133,4)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,159,34)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,118,6)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,80,114)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,51,75)"
                        }
                    }
                },
                {
                    "name": "CGAL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,74,69)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,98,27)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,17,97)"
                        }
                    }
                },
                {
                    "name": "\u8499\u7279\u5361\u6d1b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,106,5)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,20,112)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,48,9)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u8fd0\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,107,7)"
                        }
                    }
                },
                {
                    "name": "NRI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,105,93)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,63,18)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,46,137)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,97,64)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,118,4)"
                        }
                    }
                },
                {
                    "name": "hbase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,66,71)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,134,45)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,13,27)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,76,88)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,68,3)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4fe1\u606f\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,144,113)"
                        }
                    }
                },
                {
                    "name": "\u5341\u70b9\u5f00\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,32,153)"
                        }
                    }
                },
                {
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,121,139)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,61,114)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,7,75)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,38,97)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,159,31)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,82,141)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,3,113)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,125,28)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,65,22)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,68,91)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,28,128)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,139,123)"
                        }
                    }
                },
                {
                    "name": "PSENET",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,122,29)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,50,65)"
                        }
                    }
                },
                {
                    "name": "\u540e\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,109,8)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,8,59)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,10,0)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,79,125)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,81,9)"
                        }
                    }
                },
                {
                    "name": "react",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,20,51)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,39,36)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,22,93)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,29,30)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,130,47)"
                        }
                    }
                },
                {
                    "name": "\u591a\u65b9\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,97,155)"
                        }
                    }
                },
                {
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,19,112)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,7,75)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,22,5)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,147,9)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,141,70)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,27,67)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,105,144)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,27,154)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,87,103)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,59,90)"
                        }
                    }
                },
                {
                    "name": "LIDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,88,41)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,122,66)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5316\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,140,74)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,115,65)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,64,125)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5b89\u9632",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,154,110)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,28,29)"
                        }
                    }
                },
                {
                    "name": "VO/VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,117,88)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,134,70)"
                        }
                    }
                },
                {
                    "name": "\u8fb9\u7f18\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,44,110)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,16,65)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,109,57)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7f8e\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,37,150)"
                        }
                    }
                },
                {
                    "name": "ranking",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,138,100)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,73,45)"
                        }
                    }
                },
                {
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,69,124)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,19,94)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,158,127)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,25,139)"
                        }
                    }
                },
                {
                    "name": "XGB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,65,113)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,51,33)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,36,7)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,40,138)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,159,89)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,79,22)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,66,151)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,103,17)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,35,132)"
                        }
                    }
                },
                {
                    "name": "\u62a0\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,51,15)"
                        }
                    }
                },
                {
                    "name": "\u8272\u8c31\u5149\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,67,61)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,37,24)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,8,87)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,24,12)"
                        }
                    }
                },
                {
                    "name": "ESMM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,70,153)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,96,5)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,8,136)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,116,29)"
                        }
                    }
                },
                {
                    "name": "LiDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,103,57)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,152,144)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,74,148)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,74,149)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,131,139)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,84,102)"
                        }
                    }
                },
                {
                    "name": "\u79bb\u6563\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,132,9)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,56,143)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,78,81)"
                        }
                    }
                },
                {
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,31,54)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,160,11)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,16,8)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,75,53)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u63d0\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,103,139)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,28,15)"
                        }
                    }
                },
                {
                    "name": "\u5373\u65f6\u901a\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,76,150)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,99,37)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,93,7)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,133,124)"
                        }
                    }
                },
                {
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,143,56)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,78,37)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,45,51)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,63,62)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,11,41)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,66,76)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,15,25)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,35,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,91,84)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,43,97)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,69,97)"
                        }
                    }
                },
                {
                    "name": "\u914d\u9001\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,152,39)"
                        }
                    }
                },
                {
                    "name": "dl4j",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,47,46)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u94a5\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,96,25)"
                        }
                    }
                },
                {
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,64,69)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,92,70)"
                        }
                    }
                },
                {
                    "name": "DSP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,50,118)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,64,112)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,43,109)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,150,28)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,129,127)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,68,145)"
                        }
                    }
                },
                {
                    "name": "AGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,65,15)"
                        }
                    }
                },
                {
                    "name": "Sox",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,24,35)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,120,62)"
                        }
                    }
                },
                {
                    "name": "5G",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,70,18)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,47,160)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,21,63)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,122,57)"
                        }
                    }
                },
                {
                    "name": "pytroch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,68,72)"
                        }
                    }
                },
                {
                    "name": "\u4f3a\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,126,95)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,23,84)"
                        }
                    }
                },
                {
                    "name": "\u60ef\u6027\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,132,17)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,44,24)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,157,97)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,133,47)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,60,43)"
                        }
                    }
                },
                {
                    "name": "HQRank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,102,101)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,141,36)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,53)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u98de\u51cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,114,104)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b\u53d8\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,140,10)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,24,124)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,56,24)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,112,71)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,47,147)"
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
                "\u6df1\u5ea6\u5b66\u4e60",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "Python",
                "\u6570\u636e\u6316\u6398",
                "\u63a8\u8350\u7b97\u6cd5",
                "\u56fe\u50cf\u7b97\u6cd5",
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
        chart_7a4d6851a9e24c9a8c1d9cdb5fe0df87.setOption(option_7a4d6851a9e24c9a8c1d9cdb5fe0df87);
    </script>
                <div id="973d199f676b49d38b93f6989d1576b3" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_973d199f676b49d38b93f6989d1576b3 = echarts.init(
            document.getElementById('973d199f676b49d38b93f6989d1576b3'), 'white', {renderer: 'canvas'});
        var option_973d199f676b49d38b93f6989d1576b3 = {
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
                    "value": 576,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 288,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 235,
                    "name": "Python"
                },
                {
                    "value": 192,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 164,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 157,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 154,
                    "name": "C/C++"
                },
                {
                    "value": 154,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 153,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 90,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 88,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 78,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 75,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 70,
                    "name": "Java"
                },
                {
                    "value": 68,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 65,
                    "name": "C++"
                },
                {
                    "value": 65,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 64,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
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
                    "value": 53,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 50,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 49,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 49,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 47,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 46,
                    "name": "TensoFlow"
                },
                {
                    "value": 45,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 44,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 43,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 39,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 38,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 38,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 37,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 35,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 35,
                    "name": "NLP"
                },
                {
                    "value": 33,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 33,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 32,
                    "name": "PyTorch"
                },
                {
                    "value": 32,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 32,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 31,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 31,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 31,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 30,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 30,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 29,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 29,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 29,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 28,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 28,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 27,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 27,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 25,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 25,
                    "name": "OpenCV"
                },
                {
                    "value": 24,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 22,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 22,
                    "name": "\u4e94\u9669\u4e00\u91d1"
                },
                {
                    "value": 22,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 21,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 20,
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 20,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 19,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 19,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 19,
                    "name": "nan"
                },
                {
                    "value": 18,
                    "name": "SLAM"
                },
                {
                    "value": 18,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 17,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 17,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 17,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 17,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 17,
                    "name": "C"
                },
                {
                    "value": 17,
                    "name": "Hadoop"
                },
                {
                    "value": 17,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 16,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 16,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 16,
                    "name": "MATLAB"
                },
                {
                    "value": 16,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 16,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 15,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 15,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 15,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 14,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 14,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 14,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 14,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 13,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 13,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 13,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 13,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 12,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 12,
                    "name": "CNN"
                },
                {
                    "value": 12,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 12,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 12,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 12,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 11,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 11,
                    "name": "Keras"
                },
                {
                    "value": 11,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 11,
                    "name": "ROS"
                },
                {
                    "value": 10,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 10,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 10,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 10,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 10,
                    "name": "Scala"
                },
                {
                    "value": 10,
                    "name": "SQL"
                },
                {
                    "value": 10,
                    "name": "python"
                },
                {
                    "value": 10,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 10,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 9,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 9,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 9,
                    "name": "XGBoost"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 9,
                    "name": "AI"
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
                    "name": "\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 9,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 8,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 8,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 8,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 8,
                    "name": "Caffe"
                },
                {
                    "value": 8,
                    "name": "tensorflow"
                },
                {
                    "value": 8,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 8,
                    "name": "RNN"
                },
                {
                    "value": 8,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 8,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 8,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 7,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 7,
                    "name": "Golang"
                },
                {
                    "value": 7,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 7,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 7,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 7,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 7,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 7,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 7,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 7,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 7,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 7,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 7,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 6,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 6,
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 6,
                    "name": "\u5730\u56fe"
                },
                {
                    "value": 6,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 6,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 6,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 6,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 5,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 5,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 5,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 5,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 5,
                    "name": "TensorFlow"
                },
                {
                    "value": 5,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 5,
                    "name": "linux"
                },
                {
                    "value": 5,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 5,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 5,
                    "name": "spark"
                },
                {
                    "value": 5,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 5,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 5,
                    "name": "MySQL"
                },
                {
                    "value": 5,
                    "name": "Linux"
                },
                {
                    "value": 5,
                    "name": "opencv"
                },
                {
                    "value": 5,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 5,
                    "name": "ARM"
                },
                {
                    "value": 5,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 5,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "Shell"
                },
                {
                    "value": 5,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 4,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 4,
                    "name": "Flink"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 4,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 4,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 4,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 4,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 4,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 4,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 4,
                    "name": "salm"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 4,
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "nlp"
                },
                {
                    "value": 4,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 4,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 4,
                    "name": "matlab"
                },
                {
                    "value": 4,
                    "name": "3D"
                },
                {
                    "value": 4,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 3,
                    "name": "GAN"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 3,
                    "name": "MXNet"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 3,
                    "name": "pytorch"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 3,
                    "name": "OpenGL"
                },
                {
                    "value": 3,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 3,
                    "name": "DSP"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "HALCON"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 3,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 3,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 3,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 3,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "CV"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 2,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 2,
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u7814\u7a76"
                },
                {
                    "value": 2,
                    "name": "\u7b56\u7565\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 2,
                    "name": "LTE"
                },
                {
                    "value": 2,
                    "name": "Go"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 2,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 2,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 2,
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "ETL"
                },
                {
                    "value": 2,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 2,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "opengl"
                },
                {
                    "value": 2,
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u6458\u8981"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 2,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 2,
                    "name": "SFM"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 2,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 2,
                    "name": "\u52a8\u6001\u89c4\u5212"
                },
                {
                    "value": 2,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "ETA"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 2,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "CAD"
                },
                {
                    "value": 2,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 2,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "go"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 2,
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 2,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 2,
                    "name": "OCR"
                },
                {
                    "value": 2,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 2,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "JavaScript"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 2,
                    "name": "AI\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u8f7b\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "FPGA\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "AI\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u66fe\u5f3a"
                },
                {
                    "value": 1,
                    "name": "automak"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a"
                },
                {
                    "value": 1,
                    "name": "rank"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "DICOM"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "shell"
                },
                {
                    "value": 1,
                    "name": "isp"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "ensorFlow"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u6cca\u8f66"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4ef7"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "torch"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51+"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u524d\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5fae\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u79d1\u6280"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206"
                },
                {
                    "value": 1,
                    "name": "ACM"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u65e5\u7167\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u667a\u80fd"
                },
                {
                    "value": 1,
                    "name": "\u7535\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "caffe"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
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
                    "name": "SNN"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u90e8\u95e8\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "MIMO\u96f7\u8fbe"
                },
                {
                    "value": 1,
                    "name": "\u70df\u96fe\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "\u77e5\u8bc6\u5e93"
                },
                {
                    "value": 1,
                    "name": "hive"
                },
                {
                    "value": 1,
                    "name": "\u4fdd\u9669"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u8fd0\u8425"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 1,
                    "name": "\u5ba4\u5185\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee/\u53cc\u6444"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u6c42\u89e3\u5668"
                },
                {
                    "value": 1,
                    "name": "\u5e8f\u5217\u9884\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u4eea\u5668\u4eea\u8868"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "3d\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u89c6\u5316"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "PUSH\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u7ed8"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "SLAM\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "VIO"
                },
                {
                    "value": 1,
                    "name": "\u9009\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u5668"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "Oracle"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "cmake"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "JAVA"
                },
                {
                    "value": 1,
                    "name": "SQLServer"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "AlphaGo"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u5e93\u5b58\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u9891\u8c31\u76d1\u6d4b"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "labview"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u5916\u5e02\u573a"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u5149"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "openGL"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u822a\u5929"
                },
                {
                    "value": 1,
                    "name": "O2O"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "BFM"
                },
                {
                    "value": 1,
                    "name": "PCL"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u51b3\u7b56\u6811"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "Pthon"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u914d\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u9002\u5e94"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "FPGA"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5ba2\u670d"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "docker"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "AEC"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "filnk"
                },
                {
                    "value": 1,
                    "name": "\u84dd\u7259"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u98de\u884c\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u67b6\u6784"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "\u96c6\u6210\u7535\u8def"
                },
                {
                    "value": 1,
                    "name": "\u753b\u50cf\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "POI"
                },
                {
                    "value": 1,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u9a71\u52a8\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "vSLAM"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u51c6\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u6821\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u7edf\u8ba1\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "rpc"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "CRNN"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "Avatar"
                },
                {
                    "value": 1,
                    "name": "Cortex-M\u6838"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "ElasticSearch"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u6846\u67b6\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u725b\u4eba\u5206\u4eab"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "IMU"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u7a7f\u6234"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "NR"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u5e76\u53d1"
                },
                {
                    "value": 1,
                    "name": "AB\u5206\u6d41"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "GBDT"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u6807\u5b9a\u7f16\u7801"
                },
                {
                    "value": 1,
                    "name": "Fliter"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "WIFI"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "OpenMesh"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5149"
                },
                {
                    "value": 1,
                    "name": "vivado"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "MDP"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5377\u79ef"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "hadoop"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "AI\u8d85\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "Lucene"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "CGAL"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "\u8499\u7279\u5361\u6d1b"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "\u671f\u6743\u6fc0\u52b1"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u8fd0\u52a8"
                },
                {
                    "value": 1,
                    "name": "NRI"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "hbase"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u4fe1\u606f\u5316"
                },
                {
                    "value": 1,
                    "name": "\u5341\u70b9\u5f00\u5de5"
                },
                {
                    "value": 1,
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "Pytorch"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "PSENET"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u540e\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42"
                },
                {
                    "value": 1,
                    "name": "react"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "\u591a\u65b9\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "LIDAR"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u8f6c\u5316\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u8d37\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5b89\u9632"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "VO/VIO"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u8fb9\u7f18\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u7f8e\u989c\u7f8e\u4f53"
                },
                {
                    "value": 1,
                    "name": "ranking"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "XGB"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217"
                },
                {
                    "value": 1,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u5e95\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "\u5176\u4ed6"
                },
                {
                    "value": 1,
                    "name": "\u62a0\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u8272\u8c31\u5149\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "ESMM"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "LiDAR"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "RTK"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u79bb\u6563\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u63d0\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5373\u65f6\u901a\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 1,
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "GIS"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u914d\u9001\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "dl4j"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u94a5\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "DSP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "AGC"
                },
                {
                    "value": 1,
                    "name": "Sox"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6"
                },
                {
                    "value": 1,
                    "name": "5G"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u7b51\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "pytroch"
                },
                {
                    "value": 1,
                    "name": "\u4f3a\u670d"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u60ef\u6027\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "HQRank"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u82f1\u98de\u51cc"
                },
                {
                    "value": 1,
                    "name": "\u52aa\u529b\u53d8\u5927\u725b"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
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
        chart_973d199f676b49d38b93f6989d1576b3.setOption(option_973d199f676b49d38b93f6989d1576b3);
    </script>
                <div id="5eab0ffffa3e4aa7897fbab834ca9557" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5eab0ffffa3e4aa7897fbab834ca9557 = echarts.init(
            document.getElementById('5eab0ffffa3e4aa7897fbab834ca9557'), 'white', {renderer: 'canvas'});
        var option_5eab0ffffa3e4aa7897fbab834ca9557 = {
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
                1224,
                568,
                106,
                92,
                46,
                19,
                11,
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
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u672c\u79d1",
                    "value": 1224
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 568
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 106
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 92
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 46
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 11
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 10
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
                    "value": 1224
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 568
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 106
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 92
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 46
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 11
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 10
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
        chart_5eab0ffffa3e4aa7897fbab834ca9557.setOption(option_5eab0ffffa3e4aa7897fbab834ca9557);
    </script>
                <div id="d2b12f4847ff41c7bb2fc461621bd191" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d2b12f4847ff41c7bb2fc461621bd191 = echarts.init(
            document.getElementById('d2b12f4847ff41c7bb2fc461621bd191'), 'white', {renderer: 'canvas'});
        var option_d2b12f4847ff41c7bb2fc461621bd191 = {
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
                838,
                429,
                343,
                244,
                215,
                10,
                3
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
                    "value": 838
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 429
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 343
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 244
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 215
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 10
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 3
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
                    "value": 838
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 429
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 343
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 244
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 215
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 10
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 3
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
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c\u5728\u6821",
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
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c\u5728\u6821",
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
        chart_d2b12f4847ff41c7bb2fc461621bd191.setOption(option_d2b12f4847ff41c7bb2fc461621bd191);
    </script>
                <div id="b05c09e8490a46dbae125e30de76ee79" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b05c09e8490a46dbae125e30de76ee79 = echarts.init(
            document.getElementById('b05c09e8490a46dbae125e30de76ee79'), 'white', {renderer: 'canvas'});
            
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
    
        var option_b05c09e8490a46dbae125e30de76ee79 = {
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
                            "color": "rgb(130,122,147)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,120,63)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,32,71)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,48,10)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,133,52)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,152,135)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,48,15)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,155,124)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,148,55)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,131,77)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,81,1)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,26,139)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,58,24)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,153,34)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,85,98)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,9,100)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,157,127)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,60,7)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,135,147)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,38,58)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,97,56)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,58,2)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,7,21)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,10,10)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,86,109)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,51,81)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,96,89)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,15,113)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,1,96)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,68,100)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,25,160)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,86,5)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,129,98)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,23,23)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,98,67)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,52,103)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,160,154)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,146,4)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,82,153)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,29,102)"
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
        chart_b05c09e8490a46dbae125e30de76ee79.setOption(option_b05c09e8490a46dbae125e30de76ee79);
    </script>
                <div id="10a03dbe60fc472fbe14b0cd8e2de4e3" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_10a03dbe60fc472fbe14b0cd8e2de4e3 = echarts.init(
            document.getElementById('10a03dbe60fc472fbe14b0cd8e2de4e3'), 'white', {renderer: 'canvas'});
            
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
    
        var option_10a03dbe60fc472fbe14b0cd8e2de4e3 = {
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
                            "color": "rgb(85,20,152)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,76,160)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,109,15)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,9,36)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,62,98)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,111,17)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,160,18)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,64,94)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,0)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,84,141)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,20,119)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,106,37)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,21,30)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,101,87)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,133,25)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,121,63)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,53,140)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,66,23)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,77,157)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,36,22)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,10,66)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,46,64)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,55,99)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,120,140)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,45,59)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,158,137)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,15,140)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,5,158)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,24,91)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,85,126)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,22,108)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,19,46)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,78,62)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,78,73)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,17,78)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,150,100)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,126,9)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,97,66)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,57,37)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,97,5)"
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
        chart_10a03dbe60fc472fbe14b0cd8e2de4e3.setOption(option_10a03dbe60fc472fbe14b0cd8e2de4e3);
    </script>
                <div id="e561366355cc47fe9485f523bb6ac255" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_e561366355cc47fe9485f523bb6ac255 = echarts.init(
            document.getElementById('e561366355cc47fe9485f523bb6ac255'), 'white', {renderer: 'canvas'});
            
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
    
        var option_e561366355cc47fe9485f523bb6ac255 = {
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
                            "color": "rgb(106,40,78)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,32,127)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,133,146)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,77,93)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,13,102)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,74,47)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,61,58)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,23,44)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,149,60)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,21,131)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,136,125)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,76,48)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,67,115)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,140,23)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,117,77)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,28,73)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,111,1)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,93,56)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,120,5)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,159,89)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,42,44)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,123,48)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,67,31)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,77,69)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,142,130)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,22,126)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,45,146)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,160,14)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,63,101)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,119,35)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,121,73)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,93,114)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,115,152)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,85,15)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,116,2)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,124,153)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,25,39)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,90,42)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,152,119)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,59,33)"
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
        chart_e561366355cc47fe9485f523bb6ac255.setOption(option_e561366355cc47fe9485f523bb6ac255);
    </script>
                <div id="bde6c5cf2b794a43b4a20968862bb7e0" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_bde6c5cf2b794a43b4a20968862bb7e0 = echarts.init(
            document.getElementById('bde6c5cf2b794a43b4a20968862bb7e0'), 'white', {renderer: 'canvas'});
            
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
    
        var option_bde6c5cf2b794a43b4a20968862bb7e0 = {
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
                            "color": "rgb(110,140,145)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,30,108)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,95,37)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,52,15)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,81,72)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,138,118)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,13,159)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,53,75)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,155,24)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,112,147)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,124,75)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,137,64)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,57,17)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,110,38)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,69,74)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,125,2)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,106,114)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,29,148)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,54,98)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,48,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,64,137)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,9,41)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,94,149)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,3,27)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,43,99)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,150,72)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,91,119)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,12,54)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,53,6)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,145,83)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,128,94)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,103,34)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,8,154)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,102,151)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,67,55)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,84,17)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,154,88)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,125,40)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,33,125)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,66,90)"
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
        chart_bde6c5cf2b794a43b4a20968862bb7e0.setOption(option_bde6c5cf2b794a43b4a20968862bb7e0);
    </script>
                <div id="cceea831045e4ec490ceb8e15cafa387" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_cceea831045e4ec490ceb8e15cafa387 = echarts.init(
            document.getElementById('cceea831045e4ec490ceb8e15cafa387'), 'white', {renderer: 'canvas'});
            
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
    
        var option_cceea831045e4ec490ceb8e15cafa387 = {
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
                            "color": "rgb(76,3,135)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,59,79)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,20,40)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,140,159)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,79,92)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,105,45)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,52,81)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,47,46)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,38,46)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,91,96)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,37,18)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,117,72)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,133,15)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,107,151)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,29,79)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,116,44)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,154,157)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,80,80)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,32,82)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,26,78)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,85,152)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,51,5)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,108,8)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,22,111)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,117,125)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,94,97)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,21,71)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,38,151)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,111,51)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,120,27)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,92,58)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,3,58)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,16,103)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,68,72)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,44,128)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,94,64)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,93,52)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,52,52)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,129,80)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,146,144)"
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
        chart_cceea831045e4ec490ceb8e15cafa387.setOption(option_cceea831045e4ec490ceb8e15cafa387);
    </script>
                <div id="7a1f26c716b74dd4bfadf917bb1d6b2a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_7a1f26c716b74dd4bfadf917bb1d6b2a = echarts.init(
            document.getElementById('7a1f26c716b74dd4bfadf917bb1d6b2a'), 'white', {renderer: 'canvas'});
            
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
    
        var option_7a1f26c716b74dd4bfadf917bb1d6b2a = {
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
                            "color": "rgb(65,27,128)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,60,118)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,72,60)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,56,128)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,47,17)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,103,12)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,21,141)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,147,88)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,39,148)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,63,132)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,109,155)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,98,160)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,134,71)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,27,78)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,29,146)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,156,27)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,136,102)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,106,32)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,127,137)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,5,116)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,102,157)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,32,97)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,70,28)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,115,141)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,87,114)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,145,104)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,50,96)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,58,18)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,19,75)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,22,140)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,100,152)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,78,69)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,134,147)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,26,149)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,128,32)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,38,28)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,40,145)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,154,55)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,159,105)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,34,12)"
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
        chart_7a1f26c716b74dd4bfadf917bb1d6b2a.setOption(option_7a1f26c716b74dd4bfadf917bb1d6b2a);
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
