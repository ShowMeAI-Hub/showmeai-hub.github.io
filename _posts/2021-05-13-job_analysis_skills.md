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

<h2>（2021-06-08更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, '00126836fd3e4d98b0be4f9d83f4faae')">关键词</button>
            <button class="tablinks" onclick="showChart(event, 'af6b1345ea3346b892fcfddf7f7c3283')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, '164ae0db96874b47af74ad064b096823')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, '804422a2fb18472994b35e40e26be36a')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '12862ce4b1e74e52b9068ac6fe0b9e06')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '4659f16188ec421abb058dd41d48082e')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'a0bdbec0ee3342b8ae7236b42b3d9780')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '67a98595bc664e43b4d6d20fd2118c03')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, '6b926fa90a1a42bc8317f0c74b6c0ada')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'b439a2503efd4ed1b95f59fdd1ee1c8d')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="00126836fd3e4d98b0be4f9d83f4faae" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_00126836fd3e4d98b0be4f9d83f4faae = echarts.init(
            document.getElementById('00126836fd3e4d98b0be4f9d83f4faae'), 'white', {renderer: 'canvas'});
            
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
    
        var option_00126836fd3e4d98b0be4f9d83f4faae = {
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
                485,
                278,
                202,
                156,
                127,
                120,
                115
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
                    "value": 485,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,120,118)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 278,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,119,1)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 202,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,124,147)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 156,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,0,3)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 127,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,35,115)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 120,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,84,60)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 115,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,78,151)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 110,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,22,56)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 104,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,99,134)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,109,0)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,60,125)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,96,60)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,160,143)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,133,122)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,7,62)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,133,74)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,135,32)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,155,128)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,25,56)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,38,30)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,104,26)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,8,68)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,116,17)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,79,130)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,49,32)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,7,9)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,48,64)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,12,41)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,1,92)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,55,149)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,77,117)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,17,113)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,65,92)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,72,50)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,151,130)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,135,101)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,64,78)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,49,9)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,155,1)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,12,0)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,37,7)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,126,9)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,116,87)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,40,97)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,43,84)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,90,9)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,118,30)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,115,36)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,159,57)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,120,2)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,68,132)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,130,151)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,22,152)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,44,91)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,86,66)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,78,159)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,37,1)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,43,143)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,70,70)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,12,48)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,143,83)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,71,87)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,19,131)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,45,79)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,57,13)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,64,71)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,34,108)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,128,139)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,8,110)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,127,117)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,31,68)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,1,137)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,18,93)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,122,64)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,151,144)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,106,50)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,71,62)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,57,45)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,5,148)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,9,54)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,1,123)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,81,34)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,64,130)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,141,107)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,76,112)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,156,155)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,55,148)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,139,22)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,23,116)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,41,39)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,120,118)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,85,136)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,136,143)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,24,129)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,112,56)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,108,150)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,12,144)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,30,89)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,88,36)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,8,153)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,94,41)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,103,32)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,112,132)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,115,12)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,100,43)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,9,16)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,71,58)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,145,95)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,102,3)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,60,22)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,105,4)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,67,13)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,124,141)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,122,32)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,85,69)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,69,81)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,9,76)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,140,52)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,134,104)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,74,79)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,94,79)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,92,28)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,148,15)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,22,35)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,137,74)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,99,148)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,14,141)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,149,101)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,76,155)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,59,133)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,131,108)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,12,141)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,157,11)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,112,57)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,107,18)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,17,102)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,17,14)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,151,94)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,61,69)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,18,94)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,13,4)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,114,135)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,1,135)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,54,122)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,50,29)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,8,20)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,126,151)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,57,73)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,56,16)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,67,58)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,122,145)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,92,121)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,136,120)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,43,52)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,84)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,88,97)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,13,42)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,133,120)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,131,63)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,137,158)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,82,8)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,81,19)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,144,67)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,75,44)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,98,111)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,13,59)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,92,56)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,122,125)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,12,134)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,28,56)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,88,1)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,108,147)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,14,47)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,59,116)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,53,89)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,2,20)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,117,32)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,105,11)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,32,124)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,101,20)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,106,12)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,44,115)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,67,31)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,97,44)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,113,16)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,151,73)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,4)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,5,49)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,135,46)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,148,66)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,124,11)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,134,55)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,146,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,5,27)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,7,39)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u9884\u6d4b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,13,86)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,57,97)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,73,83)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,37,58)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,51,96)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,89,22)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,154,25)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,149,41)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,57,75)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,72,52)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,85,20)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,160,136)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,42,17)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,0,114)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,16,33)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,16,128)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,87,132)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,116,140)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,138,129)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,152,35)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,78,122)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,26,77)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,24,156)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,75,29)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,62,70)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,86,50)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,78,50)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,60,9)"
                        }
                    }
                },
                {
                    "name": "\u529f\u80fd\u6d4b\u8bd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,77,152)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,33,24)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,106,132)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,79,18)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,123,141)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,54,129)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,110,37)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,78,83)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,68,79)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,83,97)"
                        }
                    }
                },
                {
                    "name": "\u56e0\u679c\u63a8\u65ad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,57,45)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,149,121)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,113,27)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,133,158)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,15,60)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,17,147)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,21,38)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,56,2)"
                        }
                    }
                },
                {
                    "name": "gnss",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,99,107)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,55,33)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,85,136)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,74,64)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,127,91)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,156,28)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,127,119)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,21,158)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,77,77)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,9,133)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,82,81)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,137,122)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,88,28)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,1,100)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,73,68)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,14,5)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,141,49)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,100,17)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,34,22)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,82,38)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,50,4)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,53,133)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,7,84)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,93,127)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,25,105)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,123,69)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,146,0)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,114,136)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,26,77)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,62,22)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,26,155)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,102,49)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,58,47)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,23,124)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,127,158)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,155,84)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,101,42)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,125,109)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,27,157)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,40,11)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,93,122)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,137,73)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,25,144)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,89,141)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,105,89)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,50,92)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,130,77)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,117,60)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,140,144)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,130,82)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,104,70)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,99,95)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,58,72)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,125,141)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u65e5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,48,109)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,47,88)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,75,11)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,12,136)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,96,142)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,90,153)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,50,82)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,51,5)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,74,133)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,94,24)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,121,60)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,58,158)"
                        }
                    }
                },
                {
                    "name": "Linux/Unix",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,67,105)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,153,14)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,67,4)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,138,58)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,84,11)"
                        }
                    }
                },
                {
                    "name": "CTR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,69,33)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,45,70)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u76d8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,99,30)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,81,93)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,8,55)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,44,29)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,127,32)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,95,94)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,96,59)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,64,11)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,1,149)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,156,92)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,57,104)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,7,97)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,51,83)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,114,48)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,154,86)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,40,84)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,62,35)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,3,154)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,126,8)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,5,160)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,126,104)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,12,139)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,49,153)"
                        }
                    }
                },
                {
                    "name": "hybrid/end2end",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,68,135)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,29,96)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,12,146)"
                        }
                    }
                },
                {
                    "name": "SSD\u3001Faster",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,63,90)"
                        }
                    }
                },
                {
                    "name": "\u6df7\u54cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,96,75)"
                        }
                    }
                },
                {
                    "name": "\u5e95\u5c42\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,126,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,13,79)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,70,58)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,126,158)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u62fc\u63a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,84,123)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,16,48)"
                        }
                    }
                },
                {
                    "name": "ocr",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,26,71)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,133,9)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,6,32)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,57,7)"
                        }
                    }
                },
                {
                    "name": "Cplex",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,10,1)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,110,159)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,30,16)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u7406\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,125,31)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,80,101)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,132,120)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,118,135)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,139,129)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,74,88)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,138,89)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,111,87)"
                        }
                    }
                },
                {
                    "name": "R\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,128,18)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,60,141)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u7fa4\u5206\u7c7b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,81,16)"
                        }
                    }
                },
                {
                    "name": "TF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,52,94)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,149,106)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,95,137)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,156,160)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,117,106)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,143,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,12,74)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,65,71)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,76,47)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,143,127)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,112,35)"
                        }
                    }
                },
                {
                    "name": "golang",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,100,63)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,40,76)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,21,125)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,59,50)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,9,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,43,83)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,76,132)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,135,137)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,147,108)"
                        }
                    }
                },
                {
                    "name": "ROS\uff0cGazebo\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,110,158)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,61,129)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,56,1)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,126,141)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,14,55)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,121,75)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,75,120)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u6b3a\u8bc8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,73,66)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,34,158)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,82,20)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,91,109)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,0,103)"
                        }
                    }
                },
                {
                    "name": "\u8bba\u6587\u5199\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,23,11)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,39,5)"
                        }
                    }
                },
                {
                    "name": "NPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,115,47)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,79,55)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,55,138)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,29)"
                        }
                    }
                },
                {
                    "name": "Pyspark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,107,25)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,90,15)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,127,85)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,8,18)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,117,83)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,1,74)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,46,130)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,86,36)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,160,157)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,139,39)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,100,149)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,156,134)"
                        }
                    }
                },
                {
                    "name": "RCNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,136,125)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,107,10)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,114,46)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,42,104)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,82,75)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,151,41)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,43,63)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,63,15)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,59,156)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,134,62)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,9,22)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,67,70)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,107,37)"
                        }
                    }
                },
                {
                    "name": "\u6709\u524d\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,110,17)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,66,143)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,1,53)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,118,158)"
                        }
                    }
                },
                {
                    "name": "PP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,115,0)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,33,13)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,29,73)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,57,143)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,6,64)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,73,159)"
                        }
                    }
                },
                {
                    "name": "\u865a\u5047\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,6,28)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,42,138)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,45,122)"
                        }
                    }
                },
                {
                    "name": "SSD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,116,108)"
                        }
                    }
                },
                {
                    "name": "query",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,107,160)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,160,80)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,118,75)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,0,91)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,26,125)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,9,10)"
                        }
                    }
                },
                {
                    "name": "MTL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,68,137)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,107,24)"
                        }
                    }
                },
                {
                    "name": "\u804c\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,14,25)"
                        }
                    }
                },
                {
                    "name": "Gurobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,36,56)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,57,74)"
                        }
                    }
                },
                {
                    "name": "MatLab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,117,142)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,154,35)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,145,37)"
                        }
                    }
                },
                {
                    "name": "\u7279\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,14,8)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,123,90)"
                        }
                    }
                },
                {
                    "name": "Pulp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,98,73)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,127,58)"
                        }
                    }
                },
                {
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,61,37)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,155,18)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,88,11)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,93,62)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,22,58)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,63,36)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,111,156)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9SLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,19,5)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,72,23)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,97,128)"
                        }
                    }
                },
                {
                    "name": "CCF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,135,56)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,5,61)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,51,0)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,158,104)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,29,59)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,28,46)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,100,40)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,101,159)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,62,24)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,160,110)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,45,159)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6837\u672c\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,87,66)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,54,64)"
                        }
                    }
                },
                {
                    "name": "RCN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,67,36)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,28,129)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,129,49)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,40,6)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb/\u51fa\u7248",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,34,152)"
                        }
                    }
                },
                {
                    "name": "sfm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,103,23)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,3,124)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,28,0)"
                        }
                    }
                },
                {
                    "name": "\u7535\u673a\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,78,20)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,125,35)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,94,134)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,21,67)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,25,10)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,72,98)"
                        }
                    }
                },
                {
                    "name": "kalman",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,11,38)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,155,13)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,99,89)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,81,42)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,80,39)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,28,118)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,123,56)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,0,113)"
                        }
                    }
                },
                {
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,109,28)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,100,13)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,27,42)"
                        }
                    }
                },
                {
                    "name": "AR/VR/MR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,114,132)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,128,71)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,125,0)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,125,92)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,7,54)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,27,91)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,152,21)"
                        }
                    }
                },
                {
                    "name": "FLINK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,159,78)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,137,74)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,44,56)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,35,152)"
                        }
                    }
                },
                {
                    "name": "CPU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,71,74)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,47,57)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u51e0\u4f55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,11,15)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,71,115)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,116,100)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,147,104)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,53,71)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,149,8)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,152,95)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,148,11)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,75,104)"
                        }
                    }
                },
                {
                    "name": "hive",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,98,54)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,145,114)"
                        }
                    }
                },
                {
                    "name": "AutoML",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,16,66)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,131,68)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u5238",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,151,115)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,133,37)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,153,146)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,156,114)"
                        }
                    }
                },
                {
                    "name": "PID",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,153,157)"
                        }
                    }
                },
                {
                    "name": "C++/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,65,33)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,93,81)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,16,97)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,120,37)"
                        }
                    }
                },
                {
                    "name": "CRF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,126,77)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,99,113)"
                        }
                    }
                },
                {
                    "name": "rtk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,102,16)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,55,101)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,67,66)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,31,107)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,130,35)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,72,63)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,61,95)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,143,146)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,104,122)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,8,115)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,53,70)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,29,54)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,71,35)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,91,12)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,26,66)"
                        }
                    }
                },
                {
                    "name": "KALDI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,29,18)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,42,126)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,151,9)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,83,49)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,134,20)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,10,28)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,125,38)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,21,135)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,49,29)"
                        }
                    }
                },
                {
                    "name": "NPL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,123,46)"
                        }
                    }
                },
                {
                    "name": "AEB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,113,41)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,35,72)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,28,55)"
                        }
                    }
                },
                {
                    "name": "/Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,71,126)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,33,112)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,145,112)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,4,147)"
                        }
                    }
                },
                {
                    "name": "PPP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,9,127)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,64,115)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,8,49)"
                        }
                    }
                },
                {
                    "name": "Database",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,111,16)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,83,49)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,111,64)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,18,106)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,83,92)"
                        }
                    }
                },
                {
                    "name": "TypeScript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,87,141)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,128,9)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,116,67)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,16,24)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,113,138)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,5,30)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,139,131)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,94,138)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,151,97)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,4,76)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,140,150)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,40,124)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,123,125)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,77,8)"
                        }
                    }
                },
                {
                    "name": "Linux\u3001C+\u3001Pyth",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,47,85)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,146,66)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,56,53)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,6,122)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,110,43)"
                        }
                    }
                },
                {
                    "name": "NLP/CV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,8,61)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,129,45)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,5,60)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,130,146)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,2,126)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,59,144)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,66,44)"
                        }
                    }
                },
                {
                    "name": "\u9700\u6c42\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,101,116)"
                        }
                    }
                },
                {
                    "name": "\u589e\u957f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,125,40)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,11,141)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,137,49)"
                        }
                    }
                },
                {
                    "name": "GNSS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,9,58)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,112,57)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,84,19)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,80,15)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,55,73)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,143,108)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6295\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,101,58)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,144,132)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,151,0)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,106,96)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,79,79)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,95,33)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,52,54)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,35,50)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,20,129)"
                        }
                    }
                },
                {
                    "name": "Linux\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,50,85)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,53,89)"
                        }
                    }
                },
                {
                    "name": "\u624b\u52bf\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,73,114)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,123,146)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,106,123)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,102,149)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,144,83)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,27,86)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,64,33)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,85,41)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,77,154)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,83,17)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,81,63)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,149,42)"
                        }
                    }
                },
                {
                    "name": "\u5149\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,110,123)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,5,132)"
                        }
                    }
                },
                {
                    "name": "DeepFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,40,129)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,53,95)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,132,45)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,81,103)"
                        }
                    }
                },
                {
                    "name": "Ackerma",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,31,61)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,15,124)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,100,148)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,73,109)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,22,67)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,64,25)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,40,31)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,117,33)"
                        }
                    }
                },
                {
                    "name": "mapreduce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,56,67)"
                        }
                    }
                },
                {
                    "name": "SOA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,148,142)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,50,59)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,87,66)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,12,47)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,142,115)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,87,99)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,104,115)"
                        }
                    }
                },
                {
                    "name": "\u5730\u4ea7\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,153,42)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,59,86)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,110,160)"
                        }
                    }
                },
                {
                    "name": "AIOPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,14,54)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,64,10)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,2,146)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,72,107)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,11,26)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,111,103)"
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
                "\u56fe\u7247\u8bc6\u522b"
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
        chart_00126836fd3e4d98b0be4f9d83f4faae.setOption(option_00126836fd3e4d98b0be4f9d83f4faae);
    </script>
                <div id="af6b1345ea3346b892fcfddf7f7c3283" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_af6b1345ea3346b892fcfddf7f7c3283 = echarts.init(
            document.getElementById('af6b1345ea3346b892fcfddf7f7c3283'), 'white', {renderer: 'canvas'});
        var option_af6b1345ea3346b892fcfddf7f7c3283 = {
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
                    "value": 485,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 278,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 202,
                    "name": "Python"
                },
                {
                    "value": 156,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 127,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 120,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 115,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 110,
                    "name": "C/C++"
                },
                {
                    "value": 104,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 93,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 83,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 83,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 70,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 66,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 64,
                    "name": "Java"
                },
                {
                    "value": 62,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 62,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 62,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 58,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 56,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 52,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 49,
                    "name": "C++"
                },
                {
                    "value": 47,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 43,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 43,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 41,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 38,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 37,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 37,
                    "name": "TensoFlow"
                },
                {
                    "value": 37,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 37,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 37,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 37,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 36,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 36,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 32,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 32,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 31,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 31,
                    "name": "OpenCV"
                },
                {
                    "value": 30,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 30,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 29,
                    "name": "PyTorch"
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
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 28,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 27,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 27,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 25,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 25,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 24,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 23,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 23,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 23,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 23,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 21,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 21,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 21,
                    "name": "\u4e94\u9669\u4e00\u91d1"
                },
                {
                    "value": 21,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 21,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 20,
                    "name": "Hadoop"
                },
                {
                    "value": 20,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 19,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 19,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 19,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 19,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 17,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 17,
                    "name": "nan"
                },
                {
                    "value": 17,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 17,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 16,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 15,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 15,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 15,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 14,
                    "name": "Scala"
                },
                {
                    "value": 14,
                    "name": "MATLAB"
                },
                {
                    "value": 14,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 14,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 13,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 12,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 12,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 12,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 12,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 12,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 12,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 12,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 12,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 11,
                    "name": "CNN"
                },
                {
                    "value": 11,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 11,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 11,
                    "name": "\u95ee\u7b54\u7cfb\u7edf"
                },
                {
                    "value": 11,
                    "name": "C"
                },
                {
                    "value": 11,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 11,
                    "name": "SLAM"
                },
                {
                    "value": 10,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 10,
                    "name": "Spark"
                },
                {
                    "value": 10,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 10,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 10,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 10,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 10,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 10,
                    "name": "XGBoost"
                },
                {
                    "value": 9,
                    "name": "AI"
                },
                {
                    "value": 9,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 9,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 9,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 9,
                    "name": "Caffe"
                },
                {
                    "value": 8,
                    "name": "SQL"
                },
                {
                    "value": 8,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 8,
                    "name": "RNN"
                },
                {
                    "value": 8,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 8,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 8,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 8,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 8,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 8,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 8,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 8,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 8,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 8,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 8,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 7,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 7,
                    "name": "python"
                },
                {
                    "value": 7,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 7,
                    "name": "TensorFlow"
                },
                {
                    "value": 7,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 7,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 7,
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 7,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 6,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 6,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 6,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 6,
                    "name": "Shell"
                },
                {
                    "value": 6,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 6,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 6,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 6,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 6,
                    "name": "Linux"
                },
                {
                    "value": 6,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 6,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 6,
                    "name": "Keras"
                },
                {
                    "value": 6,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 6,
                    "name": "Golang"
                },
                {
                    "value": 5,
                    "name": "ROS"
                },
                {
                    "value": 5,
                    "name": "GAN"
                },
                {
                    "value": 5,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 5,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 5,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 5,
                    "name": "spark"
                },
                {
                    "value": 5,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 5,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 5,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 5,
                    "name": "tensorflow"
                },
                {
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 4,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 4,
                    "name": "CV"
                },
                {
                    "value": 4,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 4,
                    "name": "linux"
                },
                {
                    "value": 4,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 4,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 4,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 4,
                    "name": "\u6210\u957f\u7a7a\u95f4"
                },
                {
                    "value": 4,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 4,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 4,
                    "name": "nlp"
                },
                {
                    "value": 4,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 4,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 4,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 4,
                    "name": "ARM"
                },
                {
                    "value": 4,
                    "name": "MySQL"
                },
                {
                    "value": 4,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 4,
                    "name": "\u5546\u4e1a\u822a\u5929"
                },
                {
                    "value": 3,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 3,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 3,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "C#"
                },
                {
                    "value": 3,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "matlab"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 3,
                    "name": "Flink"
                },
                {
                    "value": 3,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 3,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 3,
                    "name": "CAD"
                },
                {
                    "value": 3,
                    "name": "\u65f6\u5e8f\u9884\u6d4b"
                },
                {
                    "value": 3,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "OCR"
                },
                {
                    "value": 3,
                    "name": "Pytorch"
                },
                {
                    "value": 3,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 3,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 3,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 3,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 3,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 3,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 3,
                    "name": "Tensorflow"
                },
                {
                    "value": 3,
                    "name": "GBDT"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u7cbe\u82f1\u56e2\u961f"
                },
                {
                    "value": 3,
                    "name": "\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 3,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 3,
                    "name": "HALCON"
                },
                {
                    "value": 3,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 3,
                    "name": "RTK"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u529f\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 2,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 2,
                    "name": "Go"
                },
                {
                    "value": 2,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 2,
                    "name": "\u786c\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u56e0\u679c\u63a8\u65ad"
                },
                {
                    "value": 2,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "ElasticSearch"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 2,
                    "name": "gnss"
                },
                {
                    "value": 2,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5316"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5a92\u4f53"
                },
                {
                    "value": 2,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 2,
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "SNN"
                },
                {
                    "value": 2,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 2,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 2,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "hadoop"
                },
                {
                    "value": 2,
                    "name": "Lucene"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "VIO"
                },
                {
                    "value": 2,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "LR"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 2,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 2,
                    "name": "opengl"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "ACM"
                },
                {
                    "value": 2,
                    "name": "AGV"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u5730\u56fe"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 2,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 2,
                    "name": "Node.js"
                },
                {
                    "value": 2,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 2,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u8fd0\u52a8\u65e5"
                },
                {
                    "value": 2,
                    "name": "3D"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Linux/Unix"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "CTR"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u76d8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u5c42"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38"
                },
                {
                    "value": 1,
                    "name": "hybrid/end2end"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "\u6ee4\u955c"
                },
                {
                    "value": 1,
                    "name": "SSD\u3001Faster"
                },
                {
                    "value": 1,
                    "name": "\u6df7\u54cd"
                },
                {
                    "value": 1,
                    "name": "\u5e95\u5c42\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u62fc\u63a5"
                },
                {
                    "value": 1,
                    "name": "\u8f6f\u4ef6\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "ocr"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 1,
                    "name": "Cplex"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u7406\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "R\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5ba2\u7fa4\u5206\u7c7b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "TF"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "golang"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u5f3a\u608d\u7684\u521b\u59cb\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "ROS\uff0cGazebo\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "pytorch"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u6b3a\u8bc8"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u540d\u6821\u540d\u4f01\u80cc\u666f"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8bba\u6587\u5199\u4f5c"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "NPU"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "Pyspark"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "RCNN"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6709\u524d\u9014"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u7b51\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "PP"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4f18\u5148\u4e0a\u6d77\u843d\u6237"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u865a\u5047\u6d41\u91cf"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "SSD"
                },
                {
                    "value": 1,
                    "name": "query"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5956\u91d1\u591a\u591a\u591a"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "MTL"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u804c\u80fd\u5236\u9020"
                },
                {
                    "value": 1,
                    "name": "Gurobi"
                },
                {
                    "value": 1,
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a"
                },
                {
                    "value": 1,
                    "name": "MatLab"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "\u7279\u6548"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Pulp"
                },
                {
                    "value": 1,
                    "name": "MXNet"
                },
                {
                    "value": 1,
                    "name": "\u9690\u79d8\u8ba1\u7b97\u672f"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u4f533D\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9SLAM"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u884c\u4e3a\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "CCF"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u793e\u4ea4\u4ea7\u54c1"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "JAVA"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u6837\u672c\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u9886\u57df"
                },
                {
                    "value": 1,
                    "name": "RCN"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u95fb/\u51fa\u7248"
                },
                {
                    "value": 1,
                    "name": "sfm"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "\u7535\u673a\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "kalman"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
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
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5065\u5eb7"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "AR/VR/MR"
                },
                {
                    "value": 1,
                    "name": "DSP"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 1,
                    "name": "FLINK"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "CPU"
                },
                {
                    "value": 1,
                    "name": "\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u51e0\u4f55"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "\u4e16\u754c500\u5f3a"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "hive"
                },
                {
                    "value": 1,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "AutoML"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8bc1\u5238"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "PID"
                },
                {
                    "value": 1,
                    "name": "C++/go"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "CRF"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "rtk"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "SFM"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u6784"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "KALDI"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "nlp\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4fe1"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "NPL"
                },
                {
                    "value": 1,
                    "name": "AEB"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "/Pytorch"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "PPP"
                },
                {
                    "value": 1,
                    "name": "\u5305\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Database"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u4f17\u591a"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u77e5\u8bc6\u5e93"
                },
                {
                    "value": 1,
                    "name": "TypeScript"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5065\u5eb7"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u80fd\u6e90"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "salm"
                },
                {
                    "value": 1,
                    "name": "Linux\u3001C+\u3001Pyth"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 1,
                    "name": "NLP/CV"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "opencv"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u9700\u6c42\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u589e\u957f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "GNSS"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u7814\u7a76"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u6295\u653e"
                },
                {
                    "value": 1,
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "Linux\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u624b\u52bf\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "\u5149\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "DeepFM"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "Ackerma"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u7a0b\u80fd\u529b"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Storm"
                },
                {
                    "value": 1,
                    "name": "LTE"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "mapreduce"
                },
                {
                    "value": 1,
                    "name": "SOA"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "POI"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "\u5730\u4ea7\u79d1\u6280"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "AIOPS"
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
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
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
        chart_af6b1345ea3346b892fcfddf7f7c3283.setOption(option_af6b1345ea3346b892fcfddf7f7c3283);
    </script>
                <div id="164ae0db96874b47af74ad064b096823" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_164ae0db96874b47af74ad064b096823 = echarts.init(
            document.getElementById('164ae0db96874b47af74ad064b096823'), 'white', {renderer: 'canvas'});
        var option_164ae0db96874b47af74ad064b096823 = {
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
                1044,
                500,
                104,
                91,
                54,
                21,
                16,
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
                    "name": "\u672c\u79d1",
                    "value": 1044
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 500
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 104
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 91
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 54
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 21
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 16
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
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
                    "name": "\u672c\u79d1",
                    "value": 1044
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 500
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 104
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 91
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 54
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 21
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 16
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
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
        chart_164ae0db96874b47af74ad064b096823.setOption(option_164ae0db96874b47af74ad064b096823);
    </script>
                <div id="804422a2fb18472994b35e40e26be36a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_804422a2fb18472994b35e40e26be36a = echarts.init(
            document.getElementById('804422a2fb18472994b35e40e26be36a'), 'white', {renderer: 'canvas'});
        var option_804422a2fb18472994b35e40e26be36a = {
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
                723,
                383,
                285,
                214,
                212,
                13,
                6
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
                    "value": 723
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 383
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 285
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 214
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 212
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 13
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 6
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
                    "value": 723
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 383
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 285
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 214
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 212
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 13
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 6
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
        chart_804422a2fb18472994b35e40e26be36a.setOption(option_804422a2fb18472994b35e40e26be36a);
    </script>
                <div id="12862ce4b1e74e52b9068ac6fe0b9e06" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_12862ce4b1e74e52b9068ac6fe0b9e06 = echarts.init(
            document.getElementById('12862ce4b1e74e52b9068ac6fe0b9e06'), 'white', {renderer: 'canvas'});
            
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
    
        var option_12862ce4b1e74e52b9068ac6fe0b9e06 = {
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
                            "color": "rgb(57,155,130)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,139,97)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,82,8)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,97,1)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,125,11)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,122,58)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,128,63)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,112,120)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,25,88)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,59,30)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,35,3)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,83,87)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,92,90)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,117,99)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,89,139)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,11,127)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,143,74)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,138,97)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,41,100)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,157,74)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,67,152)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,38,46)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,81,143)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,128,48)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,93,57)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,21,79)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,4,149)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,40,151)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,80,10)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,142,43)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,129,109)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,113,59)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,92,107)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,66,154)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,89,82)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,116,69)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,10,64)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,128,15)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,68,40)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,121,72)"
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
        chart_12862ce4b1e74e52b9068ac6fe0b9e06.setOption(option_12862ce4b1e74e52b9068ac6fe0b9e06);
    </script>
                <div id="4659f16188ec421abb058dd41d48082e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_4659f16188ec421abb058dd41d48082e = echarts.init(
            document.getElementById('4659f16188ec421abb058dd41d48082e'), 'white', {renderer: 'canvas'});
            
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
    
        var option_4659f16188ec421abb058dd41d48082e = {
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
                            "color": "rgb(7,156,82)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,79,44)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,47,34)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,54,139)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,46,59)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,87,15)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,152,12)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,108,35)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,124,56)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,106,119)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,73,133)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,123,10)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,96,59)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,96,66)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,141,119)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,153,108)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,14,121)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,142,146)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,130,101)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,106,31)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,82,90)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,111,115)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,41,115)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,16,38)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,66,153)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,17,80)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,158,0)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,36,116)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,106,124)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,10,89)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,90,121)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,37,138)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,58,42)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,59,112)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,52,115)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,7,116)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,106,64)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,53,34)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,157,119)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,120,20)"
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
        chart_4659f16188ec421abb058dd41d48082e.setOption(option_4659f16188ec421abb058dd41d48082e);
    </script>
                <div id="a0bdbec0ee3342b8ae7236b42b3d9780" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_a0bdbec0ee3342b8ae7236b42b3d9780 = echarts.init(
            document.getElementById('a0bdbec0ee3342b8ae7236b42b3d9780'), 'white', {renderer: 'canvas'});
            
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
    
        var option_a0bdbec0ee3342b8ae7236b42b3d9780 = {
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
                            "color": "rgb(154,94,77)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,111,18)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,147,95)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,60,150)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,135,46)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,102,0)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,61,30)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,24,16)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,13,16)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,118,28)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,15,13)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,116,27)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,2,131)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,54,62)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,84,128)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,85,133)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,115,8)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,109,18)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,30,112)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,53,85)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,49,137)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,41,121)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,51,31)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,152,20)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,82,134)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,131,125)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,43,109)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,107,82)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,26,52)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,22,37)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,70,88)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,0,32)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,27,99)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,106,46)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,54,22)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,137,52)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,79,38)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,32,97)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,40,59)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,20,21)"
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
        chart_a0bdbec0ee3342b8ae7236b42b3d9780.setOption(option_a0bdbec0ee3342b8ae7236b42b3d9780);
    </script>
                <div id="67a98595bc664e43b4d6d20fd2118c03" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_67a98595bc664e43b4d6d20fd2118c03 = echarts.init(
            document.getElementById('67a98595bc664e43b4d6d20fd2118c03'), 'white', {renderer: 'canvas'});
            
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
    
        var option_67a98595bc664e43b4d6d20fd2118c03 = {
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
                            "color": "rgb(15,146,100)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,81,50)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,156,73)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,59,50)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,8,14)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,0,112)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,74,126)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,32)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,133,152)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,96,152)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,123,132)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,20,35)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,3,70)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,50,7)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,137,104)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,80,152)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,41,144)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,80,156)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,0,49)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,80,111)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,50,114)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,127,113)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,81,34)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,91,62)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,125,57)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,55,97)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,77,52)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,70,19)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,22,57)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,78,77)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,135,42)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,29,112)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,5,70)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,15,63)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,120,72)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,152,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,154,66)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,151,39)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,33,22)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,138,9)"
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
        chart_67a98595bc664e43b4d6d20fd2118c03.setOption(option_67a98595bc664e43b4d6d20fd2118c03);
    </script>
                <div id="6b926fa90a1a42bc8317f0c74b6c0ada" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_6b926fa90a1a42bc8317f0c74b6c0ada = echarts.init(
            document.getElementById('6b926fa90a1a42bc8317f0c74b6c0ada'), 'white', {renderer: 'canvas'});
            
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
    
        var option_6b926fa90a1a42bc8317f0c74b6c0ada = {
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
                            "color": "rgb(100,76,98)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,102,72)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,46,117)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,80,32)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,118,123)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,7,45)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,23,142)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,158,13)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,24,72)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,5,131)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,95,90)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,86,79)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,80,138)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,30,102)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,86,149)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,131,9)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,153,30)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,26,115)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,147,145)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,100,14)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,24,58)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,59,28)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,70,112)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,30,65)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,8,94)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,105,142)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,114,31)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,87,77)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,94,57)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,36,48)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,40,113)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,41,13)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,95,40)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,112,101)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,155,3)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,45,159)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,44,122)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,147,122)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,76,158)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,131,33)"
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
        chart_6b926fa90a1a42bc8317f0c74b6c0ada.setOption(option_6b926fa90a1a42bc8317f0c74b6c0ada);
    </script>
                <div id="b439a2503efd4ed1b95f59fdd1ee1c8d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b439a2503efd4ed1b95f59fdd1ee1c8d = echarts.init(
            document.getElementById('b439a2503efd4ed1b95f59fdd1ee1c8d'), 'white', {renderer: 'canvas'});
            
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
    
        var option_b439a2503efd4ed1b95f59fdd1ee1c8d = {
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
                            "color": "rgb(67,108,118)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,108,33)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,143,122)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,115,47)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,136,121)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,147,82)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,43,101)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,103,93)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,54,113)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,69,117)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,10,59)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,40,83)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,6,68)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,85,134)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,49,26)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,20,20)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,71,133)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,126,35)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,21,19)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,157,131)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,66,125)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,42,151)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,137,160)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,53,53)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,21,92)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,101,33)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,113,13)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,62,107)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,137,157)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,9,158)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,16,18)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,7,15)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,142,137)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,109,81)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,112,98)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,111,77)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,25,50)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,87,140)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,56,12)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,45,94)"
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
        chart_b439a2503efd4ed1b95f59fdd1ee1c8d.setOption(option_b439a2503efd4ed1b95f59fdd1ee1c8d);
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
