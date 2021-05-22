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
            <button class="tablinks" onclick="showChart(event, '57242a59d923428384af6a1869675d6c')">关键词</button>
            <button class="tablinks" onclick="showChart(event, '9227b7c91b854ed6b0fc4a04d4cacc89')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, '351553e614b44a6cbf6b0fb2b5f800cd')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, 'c61fa8955a7c4a7797272eb5083a9edb')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '3f82f89123da49db8db55c1b255ace36')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'b36926292a184ab69847614974cf2213')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'f221c72473914f4e9e9050f1599ce72a')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '01571d26d71e4521a608fade45b084be')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, '695f8f2331d44fa1bdc6dcb0ead2bcb7')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '1311f507fbd241fc939fd5c1455ac78d')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="57242a59d923428384af6a1869675d6c" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_57242a59d923428384af6a1869675d6c = echarts.init(
            document.getElementById('57242a59d923428384af6a1869675d6c'), 'white', {renderer: 'canvas'});
            
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
    
        var option_57242a59d923428384af6a1869675d6c = {
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
                            "color": "rgb(10,32,128)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 288,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,1,151)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 235,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,72,71)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 192,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,123,70)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 164,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,116,149)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 157,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,75,28)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,24,43)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,91,67)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 153,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,28,99)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,159,41)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,76,144)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,101,72)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,100,117)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,54,76)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,109,153)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,105,85)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,77,137)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,112,58)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,151,80)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,100,107)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,148,17)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,95,59)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,1,45)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,21,40)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,11,109)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,30,59)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,103,142)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,74,160)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,149,4)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,8,135)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,143,26)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,66,35)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,13,117)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,98,97)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,158,155)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,35,53)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,159,128)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,120,86)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,35,101)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,20,103)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,106,119)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,114,113)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,110,44)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,21,81)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,60,7)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,14,88)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,36,113)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,34,25)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,1,98)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,112,65)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,155,118)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,60,146)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,85,18)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,85,99)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,2,59)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,146,136)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,134,117)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,70,75)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,17,135)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,52,20)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,6,11)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,160,39)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,51,5)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,113,33)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,66,57)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,11,42)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,110,73)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,70,137)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,114,16)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,116,107)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,79,72)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,47,160)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,15,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,38,14)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,76,112)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,121,131)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,153,122)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,16,50)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,19,19)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,8,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,114,14)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,66,26)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,41,78)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,103,27)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,54,31)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,66,146)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,38,101)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,4,58)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,7,133)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,105,25)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,114,57)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,115,89)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,76,119)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,147,85)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,119,99)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,32,28)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,113,83)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,104,145)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,153,112)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,132,47)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,130,1)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,143,37)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,143,127)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,63,101)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,47,119)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,22,17)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,24,25)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,90,67)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,155,23)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,115,138)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,17,158)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,63,36)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,144,104)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,133,146)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,139,45)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,137,34)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,45,101)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,18,86)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,0,11)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,9,142)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,32,69)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,138,85)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,31,120)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,21,93)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,90,110)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,158,64)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,79,69)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,8,102)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,51,8)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,62,6)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,142,79)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,22,121)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,29,141)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,92,17)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,88,136)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,11,37)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,62,130)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,2,107)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,61,126)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,85,155)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,119,18)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,111,102)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,72,36)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,25,144)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,42,76)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,43,7)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,47,129)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,143,27)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,155,15)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,78,41)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,123,27)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,96,76)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,17,103)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,97,49)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,100,90)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,106,152)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,81,136)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,98,109)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,144,16)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,55,49)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,54,23)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,136,5)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,10,93)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,99,11)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,86,55)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,87,137)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,154,31)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,81,3)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,35,128)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,30,35)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,138,36)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,129,160)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,105,71)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,118,132)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,3,37)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,133,61)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,160,22)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,110,24)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,83,102)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,107,116)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,76,146)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,134,41)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,111,81)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,49,158)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,31,65)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,71,80)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,25,7)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,77,1)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,109,113)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,143,155)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,7,5)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,92,59)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,12,155)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,27,25)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,114,9)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,23,86)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,10,149)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,132,0)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,80,4)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,4,108)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,45,48)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,18,43)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,132,91)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,152,1)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,142,58)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,4,12)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,52,136)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,38,39)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,28,0)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,45,21)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,61,47)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,67,22)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,98,15)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,133,74)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,46,126)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,24,93)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,46,91)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,128,9)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,17,73)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,43,77)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,3,158)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,118,60)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,106,32)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,106,26)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,151,125)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,130,149)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,87,74)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,48,18)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,143,60)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,82,35)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,10,81)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,0,15)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,148,153)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,156,115)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,106,128)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,143,104)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,91,87)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,107,155)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,44,66)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,91,27)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,132,134)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,29,144)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,81,88)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,128,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,33,59)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,140,123)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,20,125)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,73,52)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,114,52)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,48,119)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,124,142)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,24,65)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,35,143)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,120,91)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,70,8)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,102,75)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,12,61)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,159,28)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,149,135)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,0,124)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,10,119)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,19,133)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,25,45)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,4,105)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,32,103)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,13,92)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,20,19)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,25,73)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,68,70)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,122,58)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,5,22)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,16,33)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,135,101)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,3,58)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,148,134)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,92,144)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,136,11)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6001\u89c4\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,76,85)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,87,55)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,63,32)"
                        }
                    }
                },
                {
                    "name": "go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,7,101)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,94,79)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,85,8)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,76,36)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,112,135)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,91,92)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,32,119)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,45,48)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,84,84)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,68,16)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,156,119)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,60,49)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,65,72)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,137,7)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,53,153)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,114,51)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,61,9)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,29,151)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,127,68)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,101,24)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,149,157)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,140,33)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,88,118)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,30,57)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,43,144)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,28,84)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,34,85)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,113,76)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,51,33)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,52,133)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,160,143)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,52,126)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,93,102)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,53,35)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,27,150)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,91,154)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,149,136)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,106,125)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,14,7)"
                        }
                    }
                },
                {
                    "name": "JavaScript",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,85,28)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,16,2)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,93,147)"
                        }
                    }
                },
                {
                    "name": "caffe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,27,45)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u94a5\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,104,83)"
                        }
                    }
                },
                {
                    "name": "PSENET",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,43,78)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,67,86)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,114,16)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,100,4)"
                        }
                    }
                },
                {
                    "name": "NR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,26,138)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,54,159)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u63d0\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,116,31)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,155,112)"
                        }
                    }
                },
                {
                    "name": "FPGA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,58,67)"
                        }
                    }
                },
                {
                    "name": "Fliter",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,132,139)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,128,72)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,33,32)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,32,49)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,71,71)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u9884\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,51,113)"
                        }
                    }
                },
                {
                    "name": "\u8499\u7279\u5361\u6d1b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,113,103)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,143,38)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,43,82)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,19,107)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,121,31)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,66,41)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,113,85)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u5b58\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,41,117)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,89,155)"
                        }
                    }
                },
                {
                    "name": "\u7edf\u8ba1\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,126,147)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,112,107)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,133,4)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,40,27)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,102,125)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,115,50)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,134,103)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,12,145)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5b89\u9632",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,56,125)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,114,20)"
                        }
                    }
                },
                {
                    "name": "\u98de\u884c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,127,133)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,104,88)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,77,61)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,42,45)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,13,126)"
                        }
                    }
                },
                {
                    "name": "dl4j",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,10,24)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,80,78)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,10,7)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,56,52)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u8fd0\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,117,23)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,10,145)"
                        }
                    }
                },
                {
                    "name": "Cortex-M\u6838",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,136,42)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,30,74)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,5,56)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,154,131)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,149,105)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,11,104)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,88,97)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,144,63)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,144,17)"
                        }
                    }
                },
                {
                    "name": "ESMM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,23,122)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,0,61)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,52,112)"
                        }
                    }
                },
                {
                    "name": "BFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,122,47)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,97,108)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,157,81)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,61,107)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,67,160)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,99,98)"
                        }
                    }
                },
                {
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,39,100)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,43,152)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,48,52)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,44,138)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,142,18)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,89,58)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,79,17)"
                        }
                    }
                },
                {
                    "name": "\u70df\u96fe\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,96,74)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,112,125)"
                        }
                    }
                },
                {
                    "name": "\u591a\u65b9\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,144,74)"
                        }
                    }
                },
                {
                    "name": "DICOM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,114,92)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,140,6)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,140,129)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,55,114)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,54,126)"
                        }
                    }
                },
                {
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,111,146)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,136,21)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,157,107)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,86,140)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,136,56)"
                        }
                    }
                },
                {
                    "name": "openGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,77,126)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,31,157)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,150,73)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,50,65)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,87,107)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,132,126)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,99,2)"
                        }
                    }
                },
                {
                    "name": "filnk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,40,98)"
                        }
                    }
                },
                {
                    "name": "\u79bb\u6563\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,146,99)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5377\u79ef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,16,116)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,94,160)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,128,94)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee/\u53cc\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,87,55)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u6210\u7535\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,123,152)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,153,71)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,77,133)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,46,122)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,100,75)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,41,93)"
                        }
                    }
                },
                {
                    "name": "torch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,111,93)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u66fe\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,54,52)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,114,156)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,2,92)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,81,0)"
                        }
                    }
                },
                {
                    "name": "automak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,88,72)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,143,43)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,85,66)"
                        }
                    }
                },
                {
                    "name": "cmake",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,120,122)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,159,91)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,14,66)"
                        }
                    }
                },
                {
                    "name": "DSP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,47,86)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u7259",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,11,100)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,94,15)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,8,65)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,38,57)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,13,37)"
                        }
                    }
                },
                {
                    "name": "\u60ef\u6027\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,64,141)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,138,18)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,11,156)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,142,126)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,22,0)"
                        }
                    }
                },
                {
                    "name": "vivado",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,159,34)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,44,30)"
                        }
                    }
                },
                {
                    "name": "\u9009\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,92,129)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,116,2)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,18,6)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,84,23)"
                        }
                    }
                },
                {
                    "name": "Sox",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,84,160)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,71,42)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,80,117)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,12,20)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,111,43)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,156,155)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,71,46)"
                        }
                    }
                },
                {
                    "name": "\u6821\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,51,112)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,67,143)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,142,99)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,55,160)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,51,159)"
                        }
                    }
                },
                {
                    "name": "\u5341\u70b9\u5f00\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,15,41)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,140,27)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,74,129)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,112,147)"
                        }
                    }
                },
                {
                    "name": "hive",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,155,95)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,52,136)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b\u53d8\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,152,23)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u8fd0\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,160,149)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,145,136)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,61,70)"
                        }
                    }
                },
                {
                    "name": "\u914d\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,52,109)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,30,27)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,8,56)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,58,53)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,130,121)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,44,71)"
                        }
                    }
                },
                {
                    "name": "FPGA\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,102,89)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,92,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,4,56)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,25,66)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,149,126)"
                        }
                    }
                },
                {
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,64,89)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,54,103)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,44,8)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,154,105)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,105,18)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,43,10)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,9,64)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,68,146)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,90,18)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,22,12)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,79,149)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,138,46)"
                        }
                    }
                },
                {
                    "name": "PUSH\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,131,80)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,51,57)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,35,47)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,3,153)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u7167\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,7,158)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,12,36)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,34,152)"
                        }
                    }
                },
                {
                    "name": "AI\u8d85\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,72,47)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u89c6\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,42,2)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,81,43)"
                        }
                    }
                },
                {
                    "name": "\u8fb9\u7f18\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,105,66)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,41,47)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,85,73)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,44,32)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,97,140)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,118,3)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,94,46)"
                        }
                    }
                },
                {
                    "name": "SQLServer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,66,48)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,22,55)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,12,15)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5316\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,155,138)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,44,143)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,138,67)"
                        }
                    }
                },
                {
                    "name": "\u540e\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,156,69)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,11,24)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,24,43)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,2,21)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,5,88)"
                        }
                    }
                },
                {
                    "name": "3d\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,118,20)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7a7f\u6234",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,21,138)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,84,124)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,24,51)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,137,142)"
                        }
                    }
                },
                {
                    "name": "AlphaGo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,14,122)"
                        }
                    }
                },
                {
                    "name": "HQRank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,76,36)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,72,134)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,71,21)"
                        }
                    }
                },
                {
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,56,75)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,51,126)"
                        }
                    }
                },
                {
                    "name": "NRI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,15,147)"
                        }
                    }
                },
                {
                    "name": "CGAL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,70,132)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,140,139)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,68,101)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,43,141)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,107,137)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,132,61)"
                        }
                    }
                },
                {
                    "name": "\u914d\u9001\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,51,149)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,106,154)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,14,155)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,12,103)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,92,42)"
                        }
                    }
                },
                {
                    "name": "\u6807\u5b9a\u7f16\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,156,38)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,158,125)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,33,66)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,81,84)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,67,23)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,3,78)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,121,55)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,141,95)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,152,33)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,132,159)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,118,121)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,133,125)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,64,50)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,51,157)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,149,39)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,6,76)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,7,124)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,156,130)"
                        }
                    }
                },
                {
                    "name": "WIFI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,131,149)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51+",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,95,97)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,83,28)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,10,83)"
                        }
                    }
                },
                {
                    "name": "5G",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,110,15)"
                        }
                    }
                },
                {
                    "name": "\u8272\u8c31\u5149\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,143,95)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,111,60)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,14,134)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,23,20)"
                        }
                    }
                },
                {
                    "name": "Oracle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,28,100)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,24,119)"
                        }
                    }
                },
                {
                    "name": "ranking",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,135,103)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,87,134)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,149,24)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,17,113)"
                        }
                    }
                },
                {
                    "name": "vSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,158,153)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,142,53)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,12,30)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,84,136)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,131,136)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,67,39)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,137,89)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,113,48)"
                        }
                    }
                },
                {
                    "name": "OpenMesh",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,149,56)"
                        }
                    }
                },
                {
                    "name": "react",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,127,62)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,92,19)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,113,44)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,37,160)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,112,13)"
                        }
                    }
                },
                {
                    "name": "AGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,82,158)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,79,28)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u9002\u5e94",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,2,107)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,56,94)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,63,120)"
                        }
                    }
                },
                {
                    "name": "XGB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,83,136)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,73,41)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,102,10)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,104,43)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,140,27)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,54,68)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,140,153)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,111,45)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,109,81)"
                        }
                    }
                },
                {
                    "name": "O2O",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,106,69)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,67,53)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6cca\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,79,42)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,15,100)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,130,2)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,46,97)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,142,139)"
                        }
                    }
                },
                {
                    "name": "LiDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,17,60)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,69,77)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,80,153)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,130,60)"
                        }
                    }
                },
                {
                    "name": "hbase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,52,62)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,136,140)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,149,44)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,140,6)"
                        }
                    }
                },
                {
                    "name": "labview",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,55,136)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,21,37)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,139,19)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,28,107)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,140,28)"
                        }
                    }
                },
                {
                    "name": "rpc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,26,45)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,61,47)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,105,131)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,103,117)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,116,59)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,98,129)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,0,9)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,67,145)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,84,126)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,46,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,28,122)"
                        }
                    }
                },
                {
                    "name": "\u5ba4\u5185\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,83,25)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,55,94)"
                        }
                    }
                },
                {
                    "name": "\u6846\u67b6\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,28,128)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,98,148)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,66,15)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,104,88)"
                        }
                    }
                },
                {
                    "name": "CRNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,13,82)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,10,36)"
                        }
                    }
                },
                {
                    "name": "MIMO\u96f7\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,17,160)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,49,66)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,55,18)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,29,144)"
                        }
                    }
                },
                {
                    "name": "rank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,105,54)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,124,23)"
                        }
                    }
                },
                {
                    "name": "LIDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,114,1)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,18,73)"
                        }
                    }
                },
                {
                    "name": "shell",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,14,68)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,138,141)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,116,55)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,123,80)"
                        }
                    }
                },
                {
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,4,64)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,31,160)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,16,44)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,97,5)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,72,46)"
                        }
                    }
                },
                {
                    "name": "pytroch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,43,7)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,64,104)"
                        }
                    }
                },
                {
                    "name": "IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,40,79)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,17,143)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,22,30)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,37,127)"
                        }
                    }
                },
                {
                    "name": "\u4eea\u5668\u4eea\u8868",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,15,43)"
                        }
                    }
                },
                {
                    "name": "\u9891\u8c31\u76d1\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,38,43)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,91,6)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,43,152)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,31,66)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,65,147)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,86,61)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,141,106)"
                        }
                    }
                },
                {
                    "name": "Pthon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,66,117)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,78,7)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,105,100)"
                        }
                    }
                },
                {
                    "name": "\u7535\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,87,135)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,38,62)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,117,46)"
                        }
                    }
                },
                {
                    "name": "\u753b\u50cf\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,27,11)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,152,123)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,107,37)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,102,22)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,122,16)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,98,13)"
                        }
                    }
                },
                {
                    "name": "AEC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,97,12)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,12,52)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,101,27)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,9,66)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,147,8)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4fe1\u606f\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,88,39)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,114,65)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,22,95)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,119,110)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,12,88)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,158,122)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,23,146)"
                        }
                    }
                },
                {
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,100,58)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,17,14)"
                        }
                    }
                },
                {
                    "name": "isp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,160,59)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,66,33)"
                        }
                    }
                },
                {
                    "name": "\u524d\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,142,113)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,18,98)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,149,145)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,135,132)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,76,25)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,78,52)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,67,93)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,141,100)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,103,21)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,79,29)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,29,142)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,10,68)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u7ed8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,26,89)"
                        }
                    }
                },
                {
                    "name": "\u6c42\u89e3\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,57,13)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,47,60)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,61,26)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,133,28)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,149,133)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,57,111)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,140,125)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,90,89)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,105,131)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,74,126)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,123,158)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,62,118)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,60,42)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,150,98)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,2,135)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,114,38)"
                        }
                    }
                },
                {
                    "name": "\u5373\u65f6\u901a\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,42,112)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,102,1)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,160,129)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,140,47)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,22,69)"
                        }
                    }
                },
                {
                    "name": "\u62a0\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,8,10)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,95,51)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,156,80)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,82,95)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,131,5)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,105,54)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,4,97)"
                        }
                    }
                },
                {
                    "name": "\u4f3a\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,16,57)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,149,157)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,16,151)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,40,12)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,109,87)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,30,26)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,37,102)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,98,156)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,84,43)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,137,61)"
                        }
                    }
                },
                {
                    "name": "MDP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,55,0)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,125,84)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,123,48)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7f8e\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,6,157)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,150,20)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,127,74)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,141,157)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,160,116)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,44,57)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,41,48)"
                        }
                    }
                },
                {
                    "name": "\u9a71\u52a8\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,37,124)"
                        }
                    }
                },
                {
                    "name": "ensorFlow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,27,140)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,41,113)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,16,29)"
                        }
                    }
                },
                {
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,112,133)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,27,158)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u98de\u51cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,1,17)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,113,29)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u51c6\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,121,86)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,9,62)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,159,63)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,78,67)"
                        }
                    }
                },
                {
                    "name": "Avatar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,20,135)"
                        }
                    }
                },
                {
                    "name": "VO/VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,66,149)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,11,135)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,72,154)"
                        }
                    }
                },
                {
                    "name": "AB\u5206\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,87,76)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,62,42)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,85,41)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,70,66)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,99,51)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,86,19)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,119,10)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,4,64)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,40,150)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,111,8)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,121,35)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,75,42)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,95,21)"
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
        chart_57242a59d923428384af6a1869675d6c.setOption(option_57242a59d923428384af6a1869675d6c);
    </script>
                <div id="9227b7c91b854ed6b0fc4a04d4cacc89" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9227b7c91b854ed6b0fc4a04d4cacc89 = echarts.init(
            document.getElementById('9227b7c91b854ed6b0fc4a04d4cacc89'), 'white', {renderer: 'canvas'});
        var option_9227b7c91b854ed6b0fc4a04d4cacc89 = {
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
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 33,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 32,
                    "name": "PyTorch"
                },
                {
                    "value": 32,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 32,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 31,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 31,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 31,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
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
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 29,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 29,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 28,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 28,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
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
                    "name": "OpenCV"
                },
                {
                    "value": 25,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 24,
                    "name": "\u610f\u56fe\u8bc6\u522b"
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
                    "value": 22,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
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
                    "name": "nan"
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
                    "value": 18,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 18,
                    "name": "SLAM"
                },
                {
                    "value": 17,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 17,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 17,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
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
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 17,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 16,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 16,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 16,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
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
                    "value": 15,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 15,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 15,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 14,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 14,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
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
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 12,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 12,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 12,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 12,
                    "name": "CNN"
                },
                {
                    "value": 12,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 11,
                    "name": "Keras"
                },
                {
                    "value": 11,
                    "name": "ROS"
                },
                {
                    "value": 11,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 11,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 10,
                    "name": "SQL"
                },
                {
                    "value": 10,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 10,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 10,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 10,
                    "name": "Scala"
                },
                {
                    "value": 10,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 10,
                    "name": "python"
                },
                {
                    "value": 10,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 10,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 9,
                    "name": "XGBoost"
                },
                {
                    "value": 9,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u53f7\u5904\u7406"
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
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 9,
                    "name": "Spark"
                },
                {
                    "value": 9,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 8,
                    "name": "tensorflow"
                },
                {
                    "value": 8,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 8,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 8,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 8,
                    "name": "Caffe"
                },
                {
                    "value": 8,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 8,
                    "name": "RNN"
                },
                {
                    "value": 8,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 8,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 8,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 7,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 7,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 7,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 7,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 7,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 7,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 7,
                    "name": "Golang"
                },
                {
                    "value": 7,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 7,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 7,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
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
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 7,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 7,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 6,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 6,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 6,
                    "name": "\u91d1\u878d\u4e1a"
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
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 5,
                    "name": "spark"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 5,
                    "name": "opencv"
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
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 5,
                    "name": "MySQL"
                },
                {
                    "value": 5,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 5,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 5,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 5,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 5,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 5,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 5,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 5,
                    "name": "Shell"
                },
                {
                    "value": 5,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 5,
                    "name": "Linux"
                },
                {
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 5,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 5,
                    "name": "TensorFlow"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 5,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 5,
                    "name": "ARM"
                },
                {
                    "value": 4,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 4,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 4,
                    "name": "Flink"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 4,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "nlp"
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
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 4,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 4,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 4,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 4,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 4,
                    "name": "3D"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 4,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 4,
                    "name": "matlab"
                },
                {
                    "value": 4,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "OpenGL"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
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
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 3,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 3,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 3,
                    "name": "pytorch"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 3,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 3,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 3,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 3,
                    "name": "DSP"
                },
                {
                    "value": 3,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "HALCON"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
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
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 3,
                    "name": "GAN"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 3,
                    "name": "CV"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 2,
                    "name": "ETL"
                },
                {
                    "value": 2,
                    "name": "Go"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
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
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 2,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 2,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u6458\u8981"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe"
                },
                {
                    "value": 2,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 2,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd"
                },
                {
                    "value": 2,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 2,
                    "name": "SFM"
                },
                {
                    "value": 2,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "AI\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "\u7b56\u7565\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "LTE"
                },
                {
                    "value": 2,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "CAD"
                },
                {
                    "value": 2,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 2,
                    "name": "\u52a8\u6001\u89c4\u5212"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 2,
                    "name": "go"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 2,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "ETA"
                },
                {
                    "value": 2,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 2,
                    "name": "opengl"
                },
                {
                    "value": 2,
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "OCR"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "JavaScript"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u7814\u7a76"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "caffe"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u94a5\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "PSENET"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "NR"
                },
                {
                    "value": 1,
                    "name": "\u725b\u4eba\u5206\u4eab"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u63d0\u53d6"
                },
                {
                    "value": 1,
                    "name": "docker"
                },
                {
                    "value": 1,
                    "name": "FPGA"
                },
                {
                    "value": 1,
                    "name": "Fliter"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "\u5176\u4ed6"
                },
                {
                    "value": 1,
                    "name": "\u5e8f\u5217\u9884\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u8499\u7279\u5361\u6d1b"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u5e93\u5b58\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u7edf\u8ba1\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5b89\u9632"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u98de\u884c\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "dl4j"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u8fd0\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "Cortex-M\u6838"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "ESMM"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "BFM"
                },
                {
                    "value": 1,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "GBDT"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u67b6\u6784"
                },
                {
                    "value": 1,
                    "name": "\u70df\u96fe\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u591a\u65b9\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "DICOM"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "openGL"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8c31"
                },
                {
                    "value": 1,
                    "name": "filnk"
                },
                {
                    "value": 1,
                    "name": "\u79bb\u6563\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5377\u79ef"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee/\u53cc\u6444"
                },
                {
                    "value": 1,
                    "name": "\u96c6\u6210\u7535\u8def"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "torch"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u66fe\u5f3a"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "automak"
                },
                {
                    "value": 1,
                    "name": "JAVA"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "cmake"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "DSP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u84dd\u7259"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u51b3\u7b56\u6811"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u60ef\u6027\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "vivado"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "\u9009\u578b"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Sox"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u822a\u5929"
                },
                {
                    "value": 1,
                    "name": "\u6821\u51c6"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Lucene"
                },
                {
                    "value": 1,
                    "name": "\u5341\u70b9\u5f00\u5de5"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "hive"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "\u52aa\u529b\u53d8\u5927\u725b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u8fd0\u8425"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u914d\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "FPGA\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "ACM"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "PUSH\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65e5\u7167\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "AI\u8d85\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u89c6\u5316"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u8fb9\u7f18\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "GIS"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "SQLServer"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
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
                    "name": "\u671f\u6743\u6fc0\u52b1"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u540e\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "3d\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u7a7f\u6234"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "AlphaGo"
                },
                {
                    "value": 1,
                    "name": "HQRank"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "NRI"
                },
                {
                    "value": 1,
                    "name": "CGAL"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "Pytorch"
                },
                {
                    "value": 1,
                    "name": "\u914d\u9001\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "\u6807\u5b9a\u7f16\u7801"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 1,
                    "name": "WIFI"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51+"
                },
                {
                    "value": 1,
                    "name": "SNN"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "5G"
                },
                {
                    "value": 1,
                    "name": "\u8272\u8c31\u5149\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u79d1\u6280"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "Oracle"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "ranking"
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
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad"
                },
                {
                    "value": 1,
                    "name": "vSLAM"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u77e5\u8bc6\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u90e8\u95e8\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "OpenMesh"
                },
                {
                    "value": 1,
                    "name": "react"
                },
                {
                    "value": 1,
                    "name": "\u5fae\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "ElasticSearch"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "AGC"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u9002\u5e94"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5149"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "XGB"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u7b51\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "O2O"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u8d37\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u6cca\u8f66"
                },
                {
                    "value": 1,
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "LiDAR"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "hbase"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "labview"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "rpc"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "hadoop"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5ba4\u5185\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6846\u67b6\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "CRNN"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "MIMO\u96f7\u8fbe"
                },
                {
                    "value": 1,
                    "name": "SLAM\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u5e76\u53d1"
                },
                {
                    "value": 1,
                    "name": "rank"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "LIDAR"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "shell"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u8f7b\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3"
                },
                {
                    "value": 1,
                    "name": "VIO"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u4fdd\u9669"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "pytroch"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "IMU"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u4eea\u5668\u4eea\u8868"
                },
                {
                    "value": 1,
                    "name": "\u9891\u8c31\u76d1\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Pthon"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "\u7535\u63a7"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u753b\u50cf\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u5149"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "AEC"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u4fe1\u606f\u5316"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "isp"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u524d\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u5916\u5e02\u573a"
                },
                {
                    "value": 1,
                    "name": "AI\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u667a\u80fd"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u7ed8"
                },
                {
                    "value": 1,
                    "name": "\u6c42\u89e3\u5668"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "PCL"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a"
                },
                {
                    "value": 1,
                    "name": "MCU"
                },
                {
                    "value": 1,
                    "name": "\u5373\u65f6\u901a\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "\u62a0\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u4f3a\u670d"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u5668"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "MDP"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u7f8e\u989c\u7f8e\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "POI"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u9a71\u52a8\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "ensorFlow"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u82f1\u98de\u51cc"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u51c6\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "Avatar"
                },
                {
                    "value": 1,
                    "name": "VO/VIO"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "AB\u5206\u6d41"
                },
                {
                    "value": 1,
                    "name": "RTK"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4ef7"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u5e95\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
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
        chart_9227b7c91b854ed6b0fc4a04d4cacc89.setOption(option_9227b7c91b854ed6b0fc4a04d4cacc89);
    </script>
                <div id="351553e614b44a6cbf6b0fb2b5f800cd" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_351553e614b44a6cbf6b0fb2b5f800cd = echarts.init(
            document.getElementById('351553e614b44a6cbf6b0fb2b5f800cd'), 'white', {renderer: 'canvas'});
        var option_351553e614b44a6cbf6b0fb2b5f800cd = {
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
        chart_351553e614b44a6cbf6b0fb2b5f800cd.setOption(option_351553e614b44a6cbf6b0fb2b5f800cd);
    </script>
                <div id="c61fa8955a7c4a7797272eb5083a9edb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_c61fa8955a7c4a7797272eb5083a9edb = echarts.init(
            document.getElementById('c61fa8955a7c4a7797272eb5083a9edb'), 'white', {renderer: 'canvas'});
        var option_c61fa8955a7c4a7797272eb5083a9edb = {
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
        chart_c61fa8955a7c4a7797272eb5083a9edb.setOption(option_c61fa8955a7c4a7797272eb5083a9edb);
    </script>
                <div id="3f82f89123da49db8db55c1b255ace36" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_3f82f89123da49db8db55c1b255ace36 = echarts.init(
            document.getElementById('3f82f89123da49db8db55c1b255ace36'), 'white', {renderer: 'canvas'});
            
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
    
        var option_3f82f89123da49db8db55c1b255ace36 = {
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
                            "color": "rgb(46,45,116)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,83,123)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,70,116)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,146,52)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,90,153)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,16,139)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,109,29)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,138,64)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,41,44)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,96,121)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,135,38)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,79,90)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,85,148)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,26,63)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,24,151)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,158,80)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,61,22)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,2,2)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,139,15)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,143,57)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,39,72)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,48,145)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,132,147)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,34,118)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,145,78)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,1,102)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,71,137)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,158,109)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,105,93)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,3,119)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,51,29)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,21,24)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,8,137)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,132,127)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,6,149)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,19,78)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,50,49)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,8,17)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,44,50)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,56,90)"
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
        chart_3f82f89123da49db8db55c1b255ace36.setOption(option_3f82f89123da49db8db55c1b255ace36);
    </script>
                <div id="b36926292a184ab69847614974cf2213" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b36926292a184ab69847614974cf2213 = echarts.init(
            document.getElementById('b36926292a184ab69847614974cf2213'), 'white', {renderer: 'canvas'});
            
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
    
        var option_b36926292a184ab69847614974cf2213 = {
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
                            "color": "rgb(115,152,141)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,29,153)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,52,107)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,31,144)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,149,75)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,11,77)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,113,68)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,100,7)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,122,7)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,113,83)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,31,6)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,31,112)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,130,10)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,88,42)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,30,160)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,64,78)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,45,7)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,160,35)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,117,78)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,38,29)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,3,127)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,138,23)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,8,48)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,24,19)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,10,82)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,3,86)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,29,106)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,98,149)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,19,60)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,133,12)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,156,42)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,0,31)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,32,139)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,85,88)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,112,160)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,25,150)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,31,136)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,116,144)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,111,4)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,52,72)"
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
        chart_b36926292a184ab69847614974cf2213.setOption(option_b36926292a184ab69847614974cf2213);
    </script>
                <div id="f221c72473914f4e9e9050f1599ce72a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_f221c72473914f4e9e9050f1599ce72a = echarts.init(
            document.getElementById('f221c72473914f4e9e9050f1599ce72a'), 'white', {renderer: 'canvas'});
            
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
    
        var option_f221c72473914f4e9e9050f1599ce72a = {
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
                            "color": "rgb(5,129,146)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,40,98)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,112,28)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,105,113)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,146,61)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,77,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,82,99)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,146,51)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,122,135)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,5,101)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,110,153)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,56,90)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,97,98)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,24,160)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,35,105)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,102,114)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,28,110)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,105,85)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,80,138)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,41,14)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,22,117)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,154,83)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,37,133)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,120,119)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,142,102)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,15,120)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,35,94)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,107,20)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,139,43)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,11,15)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,74,45)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,139,136)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,76,113)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,56,13)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,69,38)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,1,84)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,66,90)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,80,25)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,113,28)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,40,117)"
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
        chart_f221c72473914f4e9e9050f1599ce72a.setOption(option_f221c72473914f4e9e9050f1599ce72a);
    </script>
                <div id="01571d26d71e4521a608fade45b084be" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_01571d26d71e4521a608fade45b084be = echarts.init(
            document.getElementById('01571d26d71e4521a608fade45b084be'), 'white', {renderer: 'canvas'});
            
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
    
        var option_01571d26d71e4521a608fade45b084be = {
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
                            "color": "rgb(56,127,119)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,92,154)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,103,83)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,106,18)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,114,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,136,135)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,82,33)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,131,24)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,60,108)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,41,81)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,157,62)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,45,82)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,1,52)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,100,16)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,125,156)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,74,1)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,160,45)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,66,133)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,44,146)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,91,146)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,113,7)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,133,132)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,120,21)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,50,88)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,153,86)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,32,50)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,58,5)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,124,53)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,110,142)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,91,134)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,95,107)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,119,25)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,31,127)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,1,72)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,37,103)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,15,151)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,70,67)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,28,94)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,129,157)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,61,72)"
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
        chart_01571d26d71e4521a608fade45b084be.setOption(option_01571d26d71e4521a608fade45b084be);
    </script>
                <div id="695f8f2331d44fa1bdc6dcb0ead2bcb7" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_695f8f2331d44fa1bdc6dcb0ead2bcb7 = echarts.init(
            document.getElementById('695f8f2331d44fa1bdc6dcb0ead2bcb7'), 'white', {renderer: 'canvas'});
            
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
    
        var option_695f8f2331d44fa1bdc6dcb0ead2bcb7 = {
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
                            "color": "rgb(99,1,30)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,16,24)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,6,149)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,120,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,131,105)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,53,82)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,16,61)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,127,85)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,109,41)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,81,130)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,142,104)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,24,2)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,70,46)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,153,57)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,112,104)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,82,136)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,139,61)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,15,12)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,91,26)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,61,78)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,31,33)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,25,3)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,129,30)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,118,94)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,76,32)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,33,133)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,139,14)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,2,77)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,37,130)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,24,114)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,19,16)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,13,123)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,149,128)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,82,155)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,99,73)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,71,135)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,71,104)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,47,23)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,128,49)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,40,92)"
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
        chart_695f8f2331d44fa1bdc6dcb0ead2bcb7.setOption(option_695f8f2331d44fa1bdc6dcb0ead2bcb7);
    </script>
                <div id="1311f507fbd241fc939fd5c1455ac78d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1311f507fbd241fc939fd5c1455ac78d = echarts.init(
            document.getElementById('1311f507fbd241fc939fd5c1455ac78d'), 'white', {renderer: 'canvas'});
            
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
    
        var option_1311f507fbd241fc939fd5c1455ac78d = {
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
                            "color": "rgb(26,42,135)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,34,95)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,84,42)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,19,136)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,67,140)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,158,95)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,24,143)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,104,159)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,93,124)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,67,131)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,73,47)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,9,109)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,113,131)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,130,148)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,102,147)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,42,46)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,29,31)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,74,64)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,152,122)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,90,117)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,98,90)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,51,125)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,95,100)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,83,102)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,50,124)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,37,115)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,19,25)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,5,0)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,106,32)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,146,42)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,32,111)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,39,114)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,136,64)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,80,60)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,155,110)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,86,138)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,109,52)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,2,53)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,6,142)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,69,8)"
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
        chart_1311f507fbd241fc939fd5c1455ac78d.setOption(option_1311f507fbd241fc939fd5c1455ac78d);
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
