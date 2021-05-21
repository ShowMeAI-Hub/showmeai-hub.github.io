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

<h2>（2021-05-21更新）</h2>

<h2>点击按钮查看招聘数据分析详情</h2>
    
<a href="https://showmeai-hub.github.io/2021/05/21/job_data_anlysis.html">
    <button class="button">看薪资</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/21/job_anlysis_company.html">
    <button class="button">看公司</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/21/job_anlysis_skills.html">
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
            <button class="tablinks" onclick="showChart(event, '4083cc24dcd24698ad09aa0c9d434059')">关键词</button>
            <button class="tablinks" onclick="showChart(event, '13084467cbc247d8a8b0a3c40b837a90')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, '7bbb983c6b0f4213af2c4da3d58409fb')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, '03b966ab214648bfab16873edd6eae3e')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '3167b6499483455280f9f6fbb177bb37')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'fb1bd25732fc428ab6d02b88f00afd30')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, '1c07659828de4c76be582cecc0ee9e7a')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'ce81376714b04d80aff1961264869400')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, '00bc692e8e694a1295c2a1e4e718a55f')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'cabdfcf8cb114258baeb8dcf7f007f88')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="4083cc24dcd24698ad09aa0c9d434059" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_4083cc24dcd24698ad09aa0c9d434059 = echarts.init(
            document.getElementById('4083cc24dcd24698ad09aa0c9d434059'), 'white', {renderer: 'canvas'});
            
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
    
        var option_4083cc24dcd24698ad09aa0c9d434059 = {
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
                562,
                277,
                229,
                190,
                162,
                154,
                152
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
                    "value": 562,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,94,66)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 277,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,73,68)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 229,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,148,53)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 190,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,131,54)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 162,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,65,91)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 154,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,99,61)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 152,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,111,41)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 150,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,30,4)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 150,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,6,55)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,108,156)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,68,67)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,119,121)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,63,12)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,109,4)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,54,50)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,21,30)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,102,50)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,70,117)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 57,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,86,2)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,62,82)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,79,67)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,140,56)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 48,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,92,110)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,31,139)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,150,51)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,34,104)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,68,66)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,15,86)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,16,144)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,59,112)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,147,89)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,155,67)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,63,105)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,75,3)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,84,11)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,11,135)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,83,127)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,48,35)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,100,59)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,104,0)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,60,29)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,65,106)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,66,52)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,0,110)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,134,123)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,56,98)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,89,62)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,12,156)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,145,61)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,138,89)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,154,81)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,24,154)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,147,9)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,57,101)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,116,30)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,84,60)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,24,133)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,26,87)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,139,79)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,38,53)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,131,47)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,16,126)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,144,42)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,71,128)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,18,109)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,156,118)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,45,95)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,126,49)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,84,69)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,100,51)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,157,1)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,66,1)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,44,144)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,130,141)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,45,79)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,111,73)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,14,160)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,5,118)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,104,142)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,2,64)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,40,75)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,43,14)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,110,67)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,57,74)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,84,100)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,156,21)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,91,17)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,154,50)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,17,37)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,47,93)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,64,120)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,138,135)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,121,124)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,60,135)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,75,123)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,128,149)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,110,148)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,22,129)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,101,134)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,68,62)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,37,142)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,91,46)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,7,11)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,145,76)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,11,95)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,69,14)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,3,75)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,6)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,139,121)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,7,113)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,109,108)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,67,108)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,52,4)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,80,114)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,22,93)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,101,152)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,119,38)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,38,22)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,8,151)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,141,83)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,81,114)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,142,3)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,16,71)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,140,130)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,143,16)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,87,1)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,78,97)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,84,27)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,116,92)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,39,67)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,84,68)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,80,110)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,80,80)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,132,153)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,17,126)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,133,97)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,66,149)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,141,128)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,62,130)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,75,37)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,108,156)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,64,23)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,126,135)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,120,76)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,15,48)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,16,92)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,115,114)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,139,8)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,12,74)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,137,150)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,134,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,39,27)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,7,15)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,160,6)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,14,73)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,8,124)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,96,81)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,106,100)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,59,141)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,137,51)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,135,36)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,37,2)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,93,2)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,154,101)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,57,158)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,118,17)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,38,4)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,132,48)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,24,157)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,63,30)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,111,38)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,92,74)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,142,115)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,26,91)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,52,18)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,54,108)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,155,70)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,18,86)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,2,111)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,101,10)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,4,121)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,37,46)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,87,54)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,31,140)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,153,71)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,14,19)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,134,53)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,1,5)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,21,159)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,128,94)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,20,35)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,77,117)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,103,127)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,64,66)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,118,2)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,75,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,64,141)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,76,17)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,117,2)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,123,31)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,67,143)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,152,153)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,13,46)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,7,17)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,60,45)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,116,149)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,152,22)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,129,30)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,85,43)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,67,54)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,53,32)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,109,54)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,86,144)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,49,47)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,45,109)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,8,45)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,17,78)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,39,124)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,28,95)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,53,57)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,12,144)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,54,126)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,147,32)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,11,23)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,136,71)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,47,26)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,135,49)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,149,156)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,15,138)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,142,113)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,36,68)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,134,141)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,123,117)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,154,2)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,61,9)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,96,46)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,152,89)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,70,132)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,60,30)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,16,159)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,28,26)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,57,13)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,63,155)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,64,88)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,55,95)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,141)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,131,63)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,101,48)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,156,15)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,9,130)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,159,96)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,6,159)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,2,43)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,15,129)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,114,69)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,64,156)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,93,55)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,52,57)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,132,47)"
                        }
                    }
                },
                {
                    "name": "go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,0,38)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,11,30)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,52,142)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,72,113)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,41,75)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,114,94)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,145,57)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,145,88)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,29,99)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,12,111)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,104,95)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,139,63)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,35,134)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,50,80)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,91,104)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,81,158)"
                        }
                    }
                },
                {
                    "name": "JavaScript",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,115,108)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,2,151)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,144,51)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,21,153)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,87,22)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,23,104)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,36,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,6,107)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,51,138)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6001\u89c4\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,32,17)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,152,135)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,119,140)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,11,124)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,55,97)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,47,143)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,19,44)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,51,102)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,41,97)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,146,42)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,110,26)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,60,81)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,3)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,65,156)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,157,148)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,25,107)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,112,111)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,16,38)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,78,80)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,2,14)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,83,137)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,139,74)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,25,15)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,98,72)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,120,105)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,40,125)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,36,120)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,48,83)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,82,21)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,63,146)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,107,129)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,72,14)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,151,36)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,88,41)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,100,102)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,128,60)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,7,56)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,6,74)"
                        }
                    }
                },
                {
                    "name": "Sox",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,154,69)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,79,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,24,4)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,47,7)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,4,81)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,93,82)"
                        }
                    }
                },
                {
                    "name": "Oracle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,100,0)"
                        }
                    }
                },
                {
                    "name": "\u5373\u65f6\u901a\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,1,0)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,74,80)"
                        }
                    }
                },
                {
                    "name": "\u5341\u70b9\u5f00\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,100,17)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,132,128)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,43,1)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,15,135)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,31,150)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,98,74)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,74,4)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,46,7)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,71,88)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,55,135)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,109,28)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,104,19)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,6,91)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u9884\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,24,110)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,121,117)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,54,23)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,131,33)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u63d0\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,19,133)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,104,43)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,68,60)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,26,157)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,113,95)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,133,147)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,32,57)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,102,43)"
                        }
                    }
                },
                {
                    "name": "HQRank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,52,30)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,79,148)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,121,114)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,117,8)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,50,125)"
                        }
                    }
                },
                {
                    "name": "BFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,158,159)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,38,79)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,9,79)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,95,153)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,153,106)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,133,129)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,98,115)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,4,7)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,143,65)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,103,41)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,89,43)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,86,140)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,87,7)"
                        }
                    }
                },
                {
                    "name": "automak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,65,102)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,46,139)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,121,30)"
                        }
                    }
                },
                {
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,82,159)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,33,51)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,3,36)"
                        }
                    }
                },
                {
                    "name": "IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,56,50)"
                        }
                    }
                },
                {
                    "name": "caffe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,33,30)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,89,99)"
                        }
                    }
                },
                {
                    "name": "labview",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,138,23)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,147,56)"
                        }
                    }
                },
                {
                    "name": "\u6807\u5b9a\u7f16\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,1,75)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,70,38)"
                        }
                    }
                },
                {
                    "name": "O2O",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,80,43)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,41,95)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u8fd0\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,148,4)"
                        }
                    }
                },
                {
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,73,88)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,147,4)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,52,39)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,152,137)"
                        }
                    }
                },
                {
                    "name": "\u914d\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,38,39)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,44,85)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,12,5)"
                        }
                    }
                },
                {
                    "name": "\u591a\u65b9\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,7,85)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,26,67)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,5,108)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,54,106)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u9002\u5e94",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,101,157)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,87,130)"
                        }
                    }
                },
                {
                    "name": "DICOM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,159,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,15,138)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,131,87)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,104,108)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,35,8)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,87,81)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee/\u53cc\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,9,140)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,1,38)"
                        }
                    }
                },
                {
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,87,6)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,87,124)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,121,61)"
                        }
                    }
                },
                {
                    "name": "VO/VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,150,69)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,133,99)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,96,159)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,44,109)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,16,52)"
                        }
                    }
                },
                {
                    "name": "NR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,48,137)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6cca\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,86,17)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,160,55)"
                        }
                    }
                },
                {
                    "name": "\u6c42\u89e3\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,107,7)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u8fd0\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,66,129)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,12,128)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,89,63)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,52,17)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,116,11)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,9,24)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,7,157)"
                        }
                    }
                },
                {
                    "name": "\u70df\u96fe\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,56,138)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u89c6\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,84,128)"
                        }
                    }
                },
                {
                    "name": "\u4f3a\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,5,3)"
                        }
                    }
                },
                {
                    "name": "\u9a71\u52a8\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,67,141)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,12,1)"
                        }
                    }
                },
                {
                    "name": "\u8499\u7279\u5361\u6d1b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,26,91)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,70,97)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,83,115)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,21,17)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,60,110)"
                        }
                    }
                },
                {
                    "name": "\u9009\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,6,134)"
                        }
                    }
                },
                {
                    "name": "rank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,47,108)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,90,37)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,34,106)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,115,150)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u94a5\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,98,160)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,18,127)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,76,26)"
                        }
                    }
                },
                {
                    "name": "FPGA\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,12,13)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,24,1)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,36,143)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,73,1)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,1,7)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,118,96)"
                        }
                    }
                },
                {
                    "name": "rpc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,7,55)"
                        }
                    }
                },
                {
                    "name": "AEC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,41,44)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,102,114)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,7,139)"
                        }
                    }
                },
                {
                    "name": "\u60ef\u6027\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,139,83)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,48,9)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,8,25)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,92,135)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,11,98)"
                        }
                    }
                },
                {
                    "name": "torch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,131,40)"
                        }
                    }
                },
                {
                    "name": "react",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,72,8)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,110,128)"
                        }
                    }
                },
                {
                    "name": "vSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,109,65)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,95,83)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,154,85)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,82,129)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,139,40)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u51c6\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,34,81)"
                        }
                    }
                },
                {
                    "name": "\u540e\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,121,38)"
                        }
                    }
                },
                {
                    "name": "Cortex-M\u6838",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,138,51)"
                        }
                    }
                },
                {
                    "name": "Avatar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,119,93)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,155,28)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,154,3)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,4,7)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,15,66)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,41,79)"
                        }
                    }
                },
                {
                    "name": "PSENET",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,56,67)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,16,77)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,154,9)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,58,153)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,83,127)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,158,145)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,68,30)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,32,50)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,51,133)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,87,18)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,129,18)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,134,94)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,37,93)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,13,155)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,149,38)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,146,40)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,103,26)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,86,123)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,57,135)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,159,13)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u98de\u51cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,147,34)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,153,100)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u5b58\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,10,86)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,64,75)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,34,36)"
                        }
                    }
                },
                {
                    "name": "filnk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,69,7)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,39,56)"
                        }
                    }
                },
                {
                    "name": "AB\u5206\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,38,115)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,142,101)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,50,92)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,125,46)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,44,49)"
                        }
                    }
                },
                {
                    "name": "hive",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,153,131)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,128,32)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,86,95)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7a7f\u6234",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,152,116)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,87,78)"
                        }
                    }
                },
                {
                    "name": "\u8fb9\u7f18\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,96,43)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,3,28)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,9,67)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,103,24)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,42,26)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,113,131)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,150,35)"
                        }
                    }
                },
                {
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,88,41)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,63,119)"
                        }
                    }
                },
                {
                    "name": "ranking",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,134,20)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,29,106)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,20,86)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,27,148)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,101,79)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,11,30)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,119,35)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51+",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,114,47)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,111,123)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,159,17)"
                        }
                    }
                },
                {
                    "name": "pytroch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,120,28)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,99,0)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,157,82)"
                        }
                    }
                },
                {
                    "name": "isp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,160,32)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,15,133)"
                        }
                    }
                },
                {
                    "name": "\u7535\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,149,42)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,113,33)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,130,81)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,159,79)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,16,49)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7f8e\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,15,45)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,138,118)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,120,25)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,39,86)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,35,68)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,152,16)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,108,132)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,156,44)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,158,91)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u66fe\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,68,76)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,62,69)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,58,30)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5316\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,28,79)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,37,38)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,59,91)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,81,57)"
                        }
                    }
                },
                {
                    "name": "LiDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,121,125)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,24,41)"
                        }
                    }
                },
                {
                    "name": "dl4j",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,97,64)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,104,48)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,140,121)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,65,99)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,40,106)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,20,141)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,61,47)"
                        }
                    }
                },
                {
                    "name": "shell",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,46,7)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,25,126)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,54,156)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,82,54)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,67,4)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,62,138)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,153,62)"
                        }
                    }
                },
                {
                    "name": "OpenMesh",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,76,95)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,145,93)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,121,46)"
                        }
                    }
                },
                {
                    "name": "Pthon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,35,133)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,33,121)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,22,141)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,85,32)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,73,111)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,63,112)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,101,137)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,139,51)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,53,100)"
                        }
                    }
                },
                {
                    "name": "LIDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,134,77)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,113,85)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,130,1)"
                        }
                    }
                },
                {
                    "name": "\u98de\u884c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,132,50)"
                        }
                    }
                },
                {
                    "name": "FPGA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,118,40)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,120,37)"
                        }
                    }
                },
                {
                    "name": "WIFI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,57,72)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,157)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,115,96)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,10,141)"
                        }
                    }
                },
                {
                    "name": "AGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,43,60)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5b89\u9632",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,12,119)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,90,70)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,38,74)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,93,18)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,44,82)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,157,103)"
                        }
                    }
                },
                {
                    "name": "ensorFlow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,154,45)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,36,126)"
                        }
                    }
                },
                {
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,73,141)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,2,46)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,59,7)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,75,68)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,7,90)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,41,16)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,85,55)"
                        }
                    }
                },
                {
                    "name": "\u914d\u9001\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,64,61)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,17,131)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,9,14)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,142,34)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,112,147)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,25,145)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,46,44)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,26,144)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,61,47)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,19,17)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,90,145)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,127,5)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,56,35)"
                        }
                    }
                },
                {
                    "name": "openGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,144,108)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,154,68)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,156,15)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,35,100)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,145,106)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,8,113)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,46,108)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,83,145)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,62,94)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,62,59)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,89,30)"
                        }
                    }
                },
                {
                    "name": "\u62a0\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,116,49)"
                        }
                    }
                },
                {
                    "name": "PUSH\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,69,154)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,104,147)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,22,84)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,114,139)"
                        }
                    }
                },
                {
                    "name": "\u8272\u8c31\u5149\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,85,16)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u6210\u7535\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,4,154)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,42,155)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,96,119)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,134,29)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,91,122)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,46,16)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,7,71)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4fe1\u606f\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,56,141)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,126,137)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,17,23)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,147,136)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,115,61)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,6,77)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,84,139)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,19,77)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,79,12)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,43,30)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,27,75)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,85,148)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,51,29)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u7167\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,123,68)"
                        }
                    }
                },
                {
                    "name": "CGAL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,134,36)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,12,0)"
                        }
                    }
                },
                {
                    "name": "cmake",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,45,50)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,18,86)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,104,11)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,56,47)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,118,120)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,90,125)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,67,16)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,93,70)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,60,158)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,151,14)"
                        }
                    }
                },
                {
                    "name": "\u4eea\u5668\u4eea\u8868",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,46,119)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,148,157)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,38,14)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,88,125)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,52,27)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,30,151)"
                        }
                    }
                },
                {
                    "name": "\u6821\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,39,113)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,152,82)"
                        }
                    }
                },
                {
                    "name": "AI\u8d85\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,32,12)"
                        }
                    }
                },
                {
                    "name": "3d\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,143,150)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,90,33)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,6,160)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u7259",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,65,156)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,25,77)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,106,23)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,117,79)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,68,5)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,111,49)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5377\u79ef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,103,46)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,65,150)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,72,145)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,108,44)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,20,24)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u7ed8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,126,67)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,61,3)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,153,8)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,135,120)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,68,59)"
                        }
                    }
                },
                {
                    "name": "DSP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,112,6)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,28,104)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,6,7)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,93,98)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,112,69)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,143,73)"
                        }
                    }
                },
                {
                    "name": "NRI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,41,93)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,64,54)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,59,116)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,98,46)"
                        }
                    }
                },
                {
                    "name": "5G",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,49,80)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,13,22)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,141,4)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,111,53)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,15,57)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,9,56)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,158,130)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,83,55)"
                        }
                    }
                },
                {
                    "name": "MDP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,131,114)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,153,63)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,6,131)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,107,0)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,77,141)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,105,31)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,96,97)"
                        }
                    }
                },
                {
                    "name": "\u5ba4\u5185\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,48,53)"
                        }
                    }
                },
                {
                    "name": "MIMO\u96f7\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,153,124)"
                        }
                    }
                },
                {
                    "name": "vivado",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,18,69)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,68,76)"
                        }
                    }
                },
                {
                    "name": "SQLServer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,85,54)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,95,21)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,115,0)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,74,57)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,134,115)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,3,107)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,28)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,96,126)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,160,65)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,129,108)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,133,111)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,98,76)"
                        }
                    }
                },
                {
                    "name": "\u753b\u50cf\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,126,4)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,141,114)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,101,64)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,10,41)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,109,57)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,128,141)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,121,109)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,40,91)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,91,111)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,78,38)"
                        }
                    }
                },
                {
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,17,30)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b\u53d8\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,86,92)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,33,85)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,50,25)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,14,159)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,151,35)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,17,6)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,30,124)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,147,58)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,59,87)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,153,52)"
                        }
                    }
                },
                {
                    "name": "AlphaGo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,50,56)"
                        }
                    }
                },
                {
                    "name": "hbase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,74,62)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,63,138)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,82)"
                        }
                    }
                },
                {
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,15,16)"
                        }
                    }
                },
                {
                    "name": "CRNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,26,122)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,136,76)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,142,84)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,137,74)"
                        }
                    }
                },
                {
                    "name": "\u9891\u8c31\u76d1\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,98,64)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,118,160)"
                        }
                    }
                },
                {
                    "name": "\u79bb\u6563\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,54,147)"
                        }
                    }
                },
                {
                    "name": "Fliter",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,28,135)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,156,92)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,76,35)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,77,23)"
                        }
                    }
                },
                {
                    "name": "\u7edf\u8ba1\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,107,33)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,149,151)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,84,130)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,133,132)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,52,42)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,16,145)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,61,136)"
                        }
                    }
                },
                {
                    "name": "\u6846\u67b6\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,75,21)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,30,20)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,155,127)"
                        }
                    }
                },
                {
                    "name": "\u524d\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,6,0)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,79,108)"
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
        chart_4083cc24dcd24698ad09aa0c9d434059.setOption(option_4083cc24dcd24698ad09aa0c9d434059);
    </script>
                <div id="13084467cbc247d8a8b0a3c40b837a90" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_13084467cbc247d8a8b0a3c40b837a90 = echarts.init(
            document.getElementById('13084467cbc247d8a8b0a3c40b837a90'), 'white', {renderer: 'canvas'});
        var option_13084467cbc247d8a8b0a3c40b837a90 = {
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
                    "value": 562,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 277,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 229,
                    "name": "Python"
                },
                {
                    "value": 190,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 162,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 154,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 152,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 150,
                    "name": "C/C++"
                },
                {
                    "value": 150,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 90,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 87,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 76,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 74,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 69,
                    "name": "Java"
                },
                {
                    "value": 68,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 64,
                    "name": "C++"
                },
                {
                    "value": 63,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 60,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 57,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 53,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 52,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 48,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 48,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 47,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 45,
                    "name": "TensoFlow"
                },
                {
                    "value": 44,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 44,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 42,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 41,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 38,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 37,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 37,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 36,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 35,
                    "name": "NLP"
                },
                {
                    "value": 35,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 33,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 32,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 32,
                    "name": "PyTorch"
                },
                {
                    "value": 31,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 31,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 31,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 31,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 30,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 30,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 29,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 29,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 28,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 28,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 27,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 27,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 27,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 27,
                    "name": "\u6e38\u620f"
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
                    "value": 23,
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
                    "name": "SLAM"
                },
                {
                    "value": 17,
                    "name": "C"
                },
                {
                    "value": 17,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 17,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 17,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 17,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
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
                    "value": 16,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 16,
                    "name": "MATLAB"
                },
                {
                    "value": 16,
                    "name": "Hadoop"
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
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 15,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 15,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 14,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 14,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 14,
                    "name": "\u5e7f\u544a\u8425\u9500"
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
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 13,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 13,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 13,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 12,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 12,
                    "name": "\u4e13\u9879\u5956\u91d1"
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
                    "name": "CNN"
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
                    "name": "Keras"
                },
                {
                    "value": 11,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 11,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 10,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 10,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
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
                    "name": "Scala"
                },
                {
                    "value": 10,
                    "name": "ROS"
                },
                {
                    "value": 10,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 10,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
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
                    "name": "XGBoost"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 9,
                    "name": "SQL"
                },
                {
                    "value": 9,
                    "name": "AI"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 9,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 9,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 9,
                    "name": "Spark"
                },
                {
                    "value": 8,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 8,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 8,
                    "name": "Caffe"
                },
                {
                    "value": 8,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 8,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 8,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 8,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 8,
                    "name": "tensorflow"
                },
                {
                    "value": 8,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 8,
                    "name": "RNN"
                },
                {
                    "value": 7,
                    "name": "\u6c7d\u8f66"
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
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 7,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 7,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 7,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 7,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 7,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 7,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 7,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 7,
                    "name": "\u56fe\u50cf\u5206\u5272"
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
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 6,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 6,
                    "name": "Golang"
                },
                {
                    "value": 6,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 6,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u89c6\u89c9"
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
                    "name": "MySQL"
                },
                {
                    "value": 5,
                    "name": "opencv"
                },
                {
                    "value": 5,
                    "name": "\u5236\u9020\u4e1a"
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
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 5,
                    "name": "Shell"
                },
                {
                    "value": 5,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 5,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 5,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 5,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 5,
                    "name": "linux"
                },
                {
                    "value": 5,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 5,
                    "name": "Linux"
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
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 5,
                    "name": "TensorFlow"
                },
                {
                    "value": 4,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 4,
                    "name": "nlp"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 4,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 4,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 4,
                    "name": "matlab"
                },
                {
                    "value": 4,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 4,
                    "name": "3D"
                },
                {
                    "value": 4,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
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
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
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
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 4,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 4,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 4,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 3,
                    "name": "OpenGL"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 3,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 3,
                    "name": "HALCON"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 3,
                    "name": "GAN"
                },
                {
                    "value": 3,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 3,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 3,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 3,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 3,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 3,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "MXNet"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "salm"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "CV"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "DSP"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
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
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 2,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "Go"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "LTE"
                },
                {
                    "value": 2,
                    "name": "opengl"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe"
                },
                {
                    "value": 2,
                    "name": "ETA"
                },
                {
                    "value": 2,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u7814\u7a76"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u7b56\u7565\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "go"
                },
                {
                    "value": 2,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
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
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 2,
                    "name": "AI\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 2,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 2,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 2,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 2,
                    "name": "JavaScript"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 2,
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 2,
                    "name": "\u52a8\u6001\u89c4\u5212"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 2,
                    "name": "OCR"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 2,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u6458\u8981"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
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
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 2,
                    "name": "SFM"
                },
                {
                    "value": 2,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 2,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 2,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
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
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "ETL"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "Sox"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "Oracle"
                },
                {
                    "value": 1,
                    "name": "\u5373\u65f6\u901a\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u5341\u70b9\u5f00\u5de5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u5e95\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u5e8f\u5217\u9884\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u63d0\u53d6"
                },
                {
                    "value": 1,
                    "name": "SLAM\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u67b6\u6784"
                },
                {
                    "value": 1,
                    "name": "ACM"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "HQRank"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u5176\u4ed6"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "BFM"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u5fae\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "Lucene"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "automak"
                },
                {
                    "value": 1,
                    "name": "docker"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u5b66"
                },
                {
                    "value": 1,
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "IMU"
                },
                {
                    "value": 1,
                    "name": "caffe"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "labview"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u6807\u5b9a\u7f16\u7801"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "O2O"
                },
                {
                    "value": 1,
                    "name": "POI"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u8fd0\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "PCL"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "\u914d\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u591a\u65b9\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u9002\u5e94"
                },
                {
                    "value": 1,
                    "name": "\u77e5\u8bc6\u5e93"
                },
                {
                    "value": 1,
                    "name": "DICOM"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee/\u53cc\u6444"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad"
                },
                {
                    "value": 1,
                    "name": "ElasticSearch"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "VO/VIO"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "NR"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u6cca\u8f66"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u6c42\u89e3\u5668"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u8fd0\u8425"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u70df\u96fe\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u89c6\u5316"
                },
                {
                    "value": 1,
                    "name": "\u4f3a\u670d"
                },
                {
                    "value": 1,
                    "name": "\u9a71\u52a8\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u8499\u7279\u5361\u6d1b"
                },
                {
                    "value": 1,
                    "name": "AI\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u725b\u4eba\u5206\u4eab"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u5e76\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u9009\u578b"
                },
                {
                    "value": 1,
                    "name": "rank"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u94a5\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "FPGA\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u7b51\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u5149"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "rpc"
                },
                {
                    "value": 1,
                    "name": "AEC"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u60ef\u6027\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "SNN"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "torch"
                },
                {
                    "value": 1,
                    "name": "react"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "vSLAM"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u51c6\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u540e\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "Cortex-M\u6838"
                },
                {
                    "value": 1,
                    "name": "Avatar"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "PSENET"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u5916\u5e02\u573a"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u8f7b\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "\u82f1\u98de\u51cc"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u5e93\u5b58\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u822a\u5929"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "filnk"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "AB\u5206\u6d41"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "hive"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u79d1\u6280"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u7a7f\u6234"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u8fb9\u7f18\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "ranking"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5ba2\u670d"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51+"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "pytroch"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "isp"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7535\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "\u7f8e\u989c\u7f8e\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u66fe\u5f3a"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8f6c\u5316\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "LiDAR"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "dl4j"
                },
                {
                    "value": 1,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "shell"
                },
                {
                    "value": 1,
                    "name": "MCU"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5149"
                },
                {
                    "value": 1,
                    "name": "OpenMesh"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "Pthon"
                },
                {
                    "value": 1,
                    "name": "Pytorch"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "LIDAR"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "\u98de\u884c\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "FPGA"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "WIFI"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u5668"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "AGC"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5b89\u9632"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "ensorFlow"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2"
                },
                {
                    "value": 1,
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u914d\u9001\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "openGL"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
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
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u62a0\u56fe"
                },
                {
                    "value": 1,
                    "name": "PUSH\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "hadoop"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u8272\u8c31\u5149\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u96c6\u6210\u7535\u8def"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u671f\u6743\u6fc0\u52b1"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
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
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6"
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
                    "name": "\u56fe\u5f62\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u65e5\u7167\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "CGAL"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "cmake"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "JAVA"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u4eea\u5668\u4eea\u8868"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "VIO"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "\u6821\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "AI\u8d85\u7b97"
                },
                {
                    "value": 1,
                    "name": "3d\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u90e8\u95e8\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u84dd\u7259"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4ef7"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5377\u79ef"
                },
                {
                    "value": 1,
                    "name": "GIS"
                },
                {
                    "value": 1,
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u7ed8"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "DSP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "NRI"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "5G"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "MDP"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5ba4\u5185\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "MIMO\u96f7\u8fbe"
                },
                {
                    "value": 1,
                    "name": "vivado"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "SQLServer"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "GBDT"
                },
                {
                    "value": 1,
                    "name": "\u51b3\u7b56\u6811"
                },
                {
                    "value": 1,
                    "name": "\u4fdd\u9669"
                },
                {
                    "value": 1,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u753b\u50cf\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u8d37\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "RTK"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u52aa\u529b\u53d8\u5927\u725b"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6"
                },
                {
                    "value": 1,
                    "name": "AlphaGo"
                },
                {
                    "value": 1,
                    "name": "hbase"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165"
                },
                {
                    "value": 1,
                    "name": "CRNN"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u9891\u8c31\u76d1\u6d4b"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u79bb\u6563\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "Fliter"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7edf\u8ba1\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6846\u67b6\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u524d\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "android"
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
        chart_13084467cbc247d8a8b0a3c40b837a90.setOption(option_13084467cbc247d8a8b0a3c40b837a90);
    </script>
                <div id="7bbb983c6b0f4213af2c4da3d58409fb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_7bbb983c6b0f4213af2c4da3d58409fb = echarts.init(
            document.getElementById('7bbb983c6b0f4213af2c4da3d58409fb'), 'white', {renderer: 'canvas'});
        var option_7bbb983c6b0f4213af2c4da3d58409fb = {
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
                1205,
                556,
                105,
                89,
                42,
                19,
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
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "\u672c\u79d1",
                    "value": 1205
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 556
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 105
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 89
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 42
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 10
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
                    "value": 1205
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 556
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 105
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 89
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 42
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 19
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 10
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
        chart_7bbb983c6b0f4213af2c4da3d58409fb.setOption(option_7bbb983c6b0f4213af2c4da3d58409fb);
    </script>
                <div id="03b966ab214648bfab16873edd6eae3e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_03b966ab214648bfab16873edd6eae3e = echarts.init(
            document.getElementById('03b966ab214648bfab16873edd6eae3e'), 'white', {renderer: 'canvas'});
        var option_03b966ab214648bfab16873edd6eae3e = {
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
                825,
                419,
                333,
                242,
                209,
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
                    "value": 825
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 419
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 333
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 242
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 209
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
                    "value": 825
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 419
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 333
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 242
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 209
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
        chart_03b966ab214648bfab16873edd6eae3e.setOption(option_03b966ab214648bfab16873edd6eae3e);
    </script>
                <div id="3167b6499483455280f9f6fbb177bb37" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_3167b6499483455280f9f6fbb177bb37 = echarts.init(
            document.getElementById('3167b6499483455280f9f6fbb177bb37'), 'white', {renderer: 'canvas'});
            
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
    
        var option_3167b6499483455280f9f6fbb177bb37 = {
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
                            "color": "rgb(108,94,15)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,9,15)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,98,8)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,71,7)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,69,141)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,61,59)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,40,141)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,86,125)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,132,120)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,5,59)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,72,29)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,56,80)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,6,118)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,100,17)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,56,77)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,147,17)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,93,4)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,58,59)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,10,26)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,80,8)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,103,52)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,93,39)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,83,93)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,49,53)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,117,152)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,122,87)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,10,42)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,134,142)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,72,13)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,51,129)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,8,45)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,142,135)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,150,152)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,71,160)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,29,124)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,76,21)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,20,7)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,28,73)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,68,7)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,118,96)"
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
        chart_3167b6499483455280f9f6fbb177bb37.setOption(option_3167b6499483455280f9f6fbb177bb37);
    </script>
                <div id="fb1bd25732fc428ab6d02b88f00afd30" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_fb1bd25732fc428ab6d02b88f00afd30 = echarts.init(
            document.getElementById('fb1bd25732fc428ab6d02b88f00afd30'), 'white', {renderer: 'canvas'});
            
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
    
        var option_fb1bd25732fc428ab6d02b88f00afd30 = {
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
                            "color": "rgb(78,138,60)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,65,153)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,15,120)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,134,103)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,159,95)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,121,64)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,129,124)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,152,70)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,153,7)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,43,24)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,99,26)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,10,46)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,117,86)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,32,85)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,89,130)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,62,14)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,15,116)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,88,93)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,15,135)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,113,81)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,133,2)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,35,83)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,148,147)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,112,6)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,7,148)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,53,148)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,124,74)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,34,89)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,59,104)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,115,31)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,85,7)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,152,118)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,153,96)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,122,64)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,120,5)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,110,81)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,96,29)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,58,153)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,6,119)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,51,97)"
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
        chart_fb1bd25732fc428ab6d02b88f00afd30.setOption(option_fb1bd25732fc428ab6d02b88f00afd30);
    </script>
                <div id="1c07659828de4c76be582cecc0ee9e7a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_1c07659828de4c76be582cecc0ee9e7a = echarts.init(
            document.getElementById('1c07659828de4c76be582cecc0ee9e7a'), 'white', {renderer: 'canvas'});
            
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
    
        var option_1c07659828de4c76be582cecc0ee9e7a = {
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
                            "color": "rgb(135,35,101)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,153,99)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,12,80)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,132,38)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,100,126)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,105,105)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,17,47)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,126,129)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,24,34)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,75,27)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,70,79)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,67,153)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,148,152)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,67,10)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,32,71)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,79,79)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,99,20)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,140,125)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,86,117)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,144,36)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,120,16)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,50,100)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,58,77)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,3,63)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,124,54)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,134,87)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,103,73)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,92,79)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,64,49)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,59,82)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,88,6)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,40,47)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,154,125)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,102,14)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,37,143)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,101,62)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,70,79)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,71,8)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,43,145)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,43,153)"
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
        chart_1c07659828de4c76be582cecc0ee9e7a.setOption(option_1c07659828de4c76be582cecc0ee9e7a);
    </script>
                <div id="ce81376714b04d80aff1961264869400" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ce81376714b04d80aff1961264869400 = echarts.init(
            document.getElementById('ce81376714b04d80aff1961264869400'), 'white', {renderer: 'canvas'});
            
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
    
        var option_ce81376714b04d80aff1961264869400 = {
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
                            "color": "rgb(151,9,16)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,124,153)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,159,5)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,57,67)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,35,78)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,69,59)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,42,73)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,135,58)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,15,63)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,24,144)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,122,62)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,41,10)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,33,91)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,92,93)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,92,54)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,158,69)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,61,8)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,47,114)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,77,49)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,144,66)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,57,101)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,96,96)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,152,14)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,28,154)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,150,26)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,15,140)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,66,20)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,91,138)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,31,74)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,16,10)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,155,129)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,154,3)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,120,43)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,115,119)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,81)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,14,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,122,76)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,39,156)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,100,140)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,17,154)"
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
        chart_ce81376714b04d80aff1961264869400.setOption(option_ce81376714b04d80aff1961264869400);
    </script>
                <div id="00bc692e8e694a1295c2a1e4e718a55f" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_00bc692e8e694a1295c2a1e4e718a55f = echarts.init(
            document.getElementById('00bc692e8e694a1295c2a1e4e718a55f'), 'white', {renderer: 'canvas'});
            
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
    
        var option_00bc692e8e694a1295c2a1e4e718a55f = {
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
                            "color": "rgb(65,49,76)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,51,139)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,82,79)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,129,29)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,100,160)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,54,112)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,25,58)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,1,145)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,36,87)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,83,114)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,151,110)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,54,37)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,22,47)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,85,122)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,12,57)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,137,95)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,102,16)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,21,43)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,45,50)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,82,156)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,141,37)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,17,76)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,66,48)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,38,123)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,155,63)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,31,138)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,38,9)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,153,96)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,36,114)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,43,38)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,50,79)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,86,52)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,128,33)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,48,48)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,38,86)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,118,3)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,147,107)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,146,121)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,0,153)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,76,12)"
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
        chart_00bc692e8e694a1295c2a1e4e718a55f.setOption(option_00bc692e8e694a1295c2a1e4e718a55f);
    </script>
                <div id="cabdfcf8cb114258baeb8dcf7f007f88" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_cabdfcf8cb114258baeb8dcf7f007f88 = echarts.init(
            document.getElementById('cabdfcf8cb114258baeb8dcf7f007f88'), 'white', {renderer: 'canvas'});
            
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
    
        var option_cabdfcf8cb114258baeb8dcf7f007f88 = {
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
                            "color": "rgb(144,142,92)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,13,69)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,46,10)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,31,74)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,16,16)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,73,90)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,132,83)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,5,14)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,112,42)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,9,64)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,60,116)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,150,156)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,39,30)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,109,131)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,4,159)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,46,136)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,79,148)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,94,52)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,87,139)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,53,105)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,38,29)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,134,13)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,1,86)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,99,45)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,119,138)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,33,14)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,82,139)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,11,64)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,103,13)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,97,149)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,134,71)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,3,31)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,87,126)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,45,8)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,49,39)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,144,159)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,105,97)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,62,6)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,16,149)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,58,65)"
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
        chart_cabdfcf8cb114258baeb8dcf7f007f88.setOption(option_cabdfcf8cb114258baeb8dcf7f007f88);
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
