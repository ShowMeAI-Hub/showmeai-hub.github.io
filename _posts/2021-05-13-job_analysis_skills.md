---
title: 算法招聘-技能与要求分析
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

<h2>(2021-05-15更新)</h2>
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
            <button class="tablinks" onclick="showChart(event, '5392bc623dee4b6e934d74c53f4b6060')">关键词</button>
            <button class="tablinks" onclick="showChart(event, '5a71413b3a294df290079447f2776acb')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, 'd764ec96bab0423b82258728b0cbc9b8')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, 'b5dcc54ba4bd48c8916ef29fa98c5acf')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '9521eb86ed5441ebbb89a8781a8da399')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '34e0428a8c9e46c09b6aa290e23924c6')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'ad9396680ddb4ec79c2f4cfb295fb0d4')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '3e03b6856f9849e38fbf4fabebb3764c')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, 'd6df3647875643899b357526955a80bc')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, 'b2df88ecd91e43b9b7eb916892f04636')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="5392bc623dee4b6e934d74c53f4b6060" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_5392bc623dee4b6e934d74c53f4b6060 = echarts.init(
            document.getElementById('5392bc623dee4b6e934d74c53f4b6060'), 'white', {renderer: 'canvas'});
        var option_5392bc623dee4b6e934d74c53f4b6060 = {
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
                368,
                181,
                152,
                126,
                110,
                103,
                103
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
                    "value": 368,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,68,91)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 181,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,90,85)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 152,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,132,131)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 126,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,29,61)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 110,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,77,48)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,132,130)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 103,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,25,76)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,155,61)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,75,33)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,22,40)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,3,32)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,72,111)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,103,109)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,133,56)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,33,95)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,151,107)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,124,149)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,39,136)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,27,68)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,123,49)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,17,29)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,61,32)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,160,81)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,156,57)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,38,51)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,45,117)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,59,86)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,61,55)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,22,93)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,54,41)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,86,80)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,126,74)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,147,30)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,15,12)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,156,97)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,139,18)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,128,117)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,69,89)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,122,160)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,62,121)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,123,9)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,31,36)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,29,101)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,71,149)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,99,77)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,125,141)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,107,6)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,147,29)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,67,83)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,7,81)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,73,153)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,127,27)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,107,91)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,69,91)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,59,13)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,70,38)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,157,18)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,110,123)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,5,47)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,124,12)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,137,35)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,28,68)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,23,55)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,62,80)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,54,90)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,133,147)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,12,3)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,121,130)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,10,105)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,142,158)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,93,126)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,85,127)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,105,103)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,153,27)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,154,133)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,76,141)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,68,91)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,0,70)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,39,55)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,118,6)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,120,70)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,123,31)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,8,80)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,98,103)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,154,84)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,138,123)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,158,111)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,14,149)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,46,73)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,66,88)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,147,96)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,44,115)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,130,89)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,149,115)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,39,154)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,12,127)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,4,38)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,75,30)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,148,30)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,40,101)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,137,70)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,159,0)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,122,49)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,68,103)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,55,66)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,134,73)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,139,21)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,44,62)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,123,118)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,47,135)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,51,23)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,11,13)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,83,101)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,17,10)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,84,81)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,40,147)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,157,66)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,29,45)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,151,150)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,71,106)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,127,32)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,43,31)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,45,52)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,2,38)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,137,1)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,93,128)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,60,91)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,60,123)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,153,32)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,108,75)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,145,113)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,113,153)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,34,95)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,96,66)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,85,130)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,51,78)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,135,81)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,159,126)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,18,144)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,97,143)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,47,157)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,74,53)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,147,132)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,113,62)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,116,26)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,20,90)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,20,152)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,86,92)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,63,65)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,34,43)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,24,65)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,14,81)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,147,117)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,2,58)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,13,146)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,7,135)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,77,149)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,120,93)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,103,72)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,34,50)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,1,10)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,1,16)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,118,34)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,109,139)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,155,10)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,135,49)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,36,48)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,49,148)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,92,102)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,67,95)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,2,150)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,151,5)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,150,4)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,54,37)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,36,20)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,154,125)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,55,114)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,90,153)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,93,62)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,154,71)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,51,99)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,74,53)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,15,144)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,102,87)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,102,101)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,91,27)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,148,72)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,62,61)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,55,7)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,83,110)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,8,59)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,9,14)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,121,125)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,93,131)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,48,88)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,28,10)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,147,134)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,84,81)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,72,136)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,81,158)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,8,158)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,40,71)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,125,52)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,113,103)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,150,153)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,51,117)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,39,140)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,39,43)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,43,125)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,54,114)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,24,23)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,60,13)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,30,84)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,119,105)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,19,23)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,110,124)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,7,68)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,27,77)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,136,132)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,74,77)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,65,24)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,128,98)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,18,104)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,123,146)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,80,145)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,125,59)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,92,30)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,144,39)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,120,63)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,106,34)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,76,37)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,72,9)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,78,113)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,110,12)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,105,110)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,98,51)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,74,85)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,50,92)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,82,73)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,129,104)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,140,31)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,140,63)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,82,109)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,102,143)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,121,147)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,152,54)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,147,22)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,38,78)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,92,32)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,137,18)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,18,6)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,58,88)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,74,47)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,111,102)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,124,33)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6001\u89c4\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,141,88)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,115,35)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,60,22)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,126,35)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,76,78)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,129,70)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,125,152)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,68,62)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,23,95)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,135,68)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,130,137)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,22,82)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,8,21)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,156,43)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,128,67)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,99,10)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,47,146)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,159,127)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,119,147)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,91,29)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,69,144)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,159,111)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,92,34)"
                        }
                    }
                },
                {
                    "name": "\u98de\u884c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,61,153)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,133,32)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,160,27)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,33,156)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,15,123)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,18,138)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,79,19)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,33,144)"
                        }
                    }
                },
                {
                    "name": "MDP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,98,39)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,53,155)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,156,11)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,62,22)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,44,89)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,103,105)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,12,124)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,153,96)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,99,40)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,24,41)"
                        }
                    }
                },
                {
                    "name": "\u8fb9\u7f18\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,43,19)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,91,159)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,145,48)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,35,144)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,99,113)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,79,97)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,53,113)"
                        }
                    }
                },
                {
                    "name": "AB\u5206\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,33,2)"
                        }
                    }
                },
                {
                    "name": "cmake",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,91,155)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,13,147)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,140,87)"
                        }
                    }
                },
                {
                    "name": "\u79bb\u6563\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,40,28)"
                        }
                    }
                },
                {
                    "name": "BFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,117,74)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,134,101)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,144,158)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,74,97)"
                        }
                    }
                },
                {
                    "name": "IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,136,2)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,108,61)"
                        }
                    }
                },
                {
                    "name": "\u524d\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,2,131)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,92,93)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,59,97)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,18,86)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,6,7)"
                        }
                    }
                },
                {
                    "name": "\u4eea\u5668\u4eea\u8868",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,128,70)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,132,110)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,155,75)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,86,113)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,36,16)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,18,136)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,111,95)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,122,21)"
                        }
                    }
                },
                {
                    "name": "go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,131,155)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,74,50)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,133,43)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,110,56)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,141,121)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,82,52)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,137,51)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,31,114)"
                        }
                    }
                },
                {
                    "name": "automak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,75,75)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,68,118)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,112,159)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,118,118)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,142,37)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,152,155)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,54,151)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,108,146)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,123,66)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,158,122)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,157,74)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,27,3)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,67,151)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,119,32)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,39,109)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,86,108)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,6,20)"
                        }
                    }
                },
                {
                    "name": "PSENET",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,96,25)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,47,115)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u7ed8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,115,150)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,7,97)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,103,9)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,18,83)"
                        }
                    }
                },
                {
                    "name": "DICOM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,101,144)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,9,154)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,43,18)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u94a5\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,118,160)"
                        }
                    }
                },
                {
                    "name": "JavaScript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,125,128)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,37,75)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,10,60)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,24,15)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,152,156)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,56,124)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,111,123)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,155,137)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5377\u79ef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,104,79)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,2,45)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,155,28)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,119,135)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,148,132)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,38,36)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,68,60)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,6,117)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,27,114)"
                        }
                    }
                },
                {
                    "name": "\u6821\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,31,23)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,110,23)"
                        }
                    }
                },
                {
                    "name": "LIDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,103,109)"
                        }
                    }
                },
                {
                    "name": "labview",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,80,100)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,135,141)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,143,69)"
                        }
                    }
                },
                {
                    "name": "Pthon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,81,2)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,69,119)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,44,9)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,34,58)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,45,112)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,2,1)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,154,7)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,154,53)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,125,27)"
                        }
                    }
                },
                {
                    "name": "\u5ba4\u5185\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,66,71)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7a7f\u6234",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,75,12)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,113,148)"
                        }
                    }
                },
                {
                    "name": "SQLServer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,88,11)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,127,93)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,53,96)"
                        }
                    }
                },
                {
                    "name": "filnk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,82,115)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u5b58\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,33,145)"
                        }
                    }
                },
                {
                    "name": "WIFI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,18,23)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,13,58)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,134,8)"
                        }
                    }
                },
                {
                    "name": "rpc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,46,142)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,159,85)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,110,49)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,105,141)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,53,92)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,23,36)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,36,30)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,38,126)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,26,19)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,128,80)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,55,63)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,119,81)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,113,111)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,40,101)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,110,98)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,7,78)"
                        }
                    }
                },
                {
                    "name": "hbase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,102,150)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,144,104)"
                        }
                    }
                },
                {
                    "name": "AlphaGo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,50,71)"
                        }
                    }
                },
                {
                    "name": "Sox",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,65,0)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,124,151)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,0,101)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,96,26)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,104,126)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,154,92)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,112,66)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,82,76)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,103,115)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,49,68)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,80,129)"
                        }
                    }
                },
                {
                    "name": "torch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,62,28)"
                        }
                    }
                },
                {
                    "name": "CRNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,2,4)"
                        }
                    }
                },
                {
                    "name": "ensorFlow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,67,115)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,40,149)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,46,31)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,14,75)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,146,12)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,100,155)"
                        }
                    }
                },
                {
                    "name": "\u6807\u5b9a\u7f16\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,101,146)"
                        }
                    }
                },
                {
                    "name": "\u6c42\u89e3\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,104,111)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,143,57)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,24,22)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,28,66)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,10,79)"
                        }
                    }
                },
                {
                    "name": "caffe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,63,135)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,79,27)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,150,73)"
                        }
                    }
                },
                {
                    "name": "NRI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,93,35)"
                        }
                    }
                },
                {
                    "name": "\u8272\u8c31\u5149\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,76,148)"
                        }
                    }
                },
                {
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,117,118)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,157,66)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,136,149)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,30,22)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u9002\u5e94",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,145,127)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,46,120)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,4,4)"
                        }
                    }
                },
                {
                    "name": "rank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,138,92)"
                        }
                    }
                },
                {
                    "name": "FPGA\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,41,13)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u8fd0\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,57,98)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,131,77)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,97,48)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,150,149)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,2,80)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,113,113)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,64,1)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,83,70)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,154,5)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,159,156)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,36,117)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,12,0)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,45,15)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,110,158)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,38,113)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,62,75)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,51,51)"
                        }
                    }
                },
                {
                    "name": "\u540e\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,132,100)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,3,18)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,76,69)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,37,41)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,52,69)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,2,69)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,84,134)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,93,59)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,39,39)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,95,49)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,98,61)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,144,152)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,1,141)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,101,2)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,156,45)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,82,97)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,83,54)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,57,113)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,144,79)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,57,46)"
                        }
                    }
                },
                {
                    "name": "\u60ef\u6027\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,128,26)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,82,150)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,17,17)"
                        }
                    }
                },
                {
                    "name": "Avatar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,44,128)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,35,18)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,90,110)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,56,110)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,115,12)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,58,81)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,132,138)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,3)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,120,97)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,55,56)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,148,65)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,47,20)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,23,160)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,92,18)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,10,118)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,46,101)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,4,45)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,49,36)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,79,7)"
                        }
                    }
                },
                {
                    "name": "3d\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,115,75)"
                        }
                    }
                },
                {
                    "name": "\u753b\u50cf\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,41,83)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,87,26)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,159,23)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,148,106)"
                        }
                    }
                },
                {
                    "name": "HQRank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,75,18)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,72,157)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,55,149)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,110,62)"
                        }
                    }
                },
                {
                    "name": "vSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,70,137)"
                        }
                    }
                },
                {
                    "name": "FPGA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,54,79)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,103,137)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,148,32)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,99,82)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,50,95)"
                        }
                    }
                },
                {
                    "name": "pytroch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,80,72)"
                        }
                    }
                },
                {
                    "name": "\u8499\u7279\u5361\u6d1b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,87,3)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,45,116)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,72,138)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,37,31)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,118,57)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,19,119)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,80,70)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,60,83)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,2,48)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,147,85)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,64,36)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,71,70)"
                        }
                    }
                },
                {
                    "name": "\u7535\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,17,157)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,49,127)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,27,15)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,15,79)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,106,107)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,126,20)"
                        }
                    }
                },
                {
                    "name": "\u914d\u9001\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,111,44)"
                        }
                    }
                },
                {
                    "name": "PUSH\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,88,73)"
                        }
                    }
                },
                {
                    "name": "Fliter",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,120,28)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,86,50)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,24,94)"
                        }
                    }
                },
                {
                    "name": "Oracle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,120,144)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,65,78)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,84,111)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,84,155)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,22,35)"
                        }
                    }
                },
                {
                    "name": "VO/VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,157,76)"
                        }
                    }
                },
                {
                    "name": "LiDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,61,150)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,142,81)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,79,158)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,95,77)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,13,52)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,77,130)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,22,99)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4fe1\u606f\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,52,98)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u7259",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,104,128)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,75,48)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,127,87)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,83,39)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,112,16)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,100,50)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,5,80)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,62,37)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5316\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,122,160)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,73,104)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,145,5)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,15,14)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,106,79)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,101,12)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,52,52)"
                        }
                    }
                },
                {
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,151,43)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,27,27)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,24,132)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,138,85)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,18,5)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,148,20)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,53,69)"
                        }
                    }
                },
                {
                    "name": "DSP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,83,145)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,95,121)"
                        }
                    }
                },
                {
                    "name": "\u70df\u96fe\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,16,131)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,3,2)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,24,34)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,149,147)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,8,37)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,60,155)"
                        }
                    }
                },
                {
                    "name": "vivado",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,133,103)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,123,141)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,121,137)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,158,78)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,82,146)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,123,17)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u7167\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,159,62)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,21,160)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,62,5)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,133,147)"
                        }
                    }
                },
                {
                    "name": "\u591a\u65b9\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,145,37)"
                        }
                    }
                },
                {
                    "name": "O2O",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,12,76)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,52,8)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,39,85)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,110,105)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,57,101)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,14,63)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,5,101)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u89c6\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,66,125)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,37,149)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,79,14)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,21,148)"
                        }
                    }
                },
                {
                    "name": "\u914d\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,78,1)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,13,66)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,19,102)"
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
                "\u56fe\u7247\u8bc6\u522b",
                "\u56fe\u50cf\u7b97\u6cd5"
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
        chart_5392bc623dee4b6e934d74c53f4b6060.setOption(option_5392bc623dee4b6e934d74c53f4b6060);
    </script>
                <div id="5a71413b3a294df290079447f2776acb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5a71413b3a294df290079447f2776acb = echarts.init(
            document.getElementById('5a71413b3a294df290079447f2776acb'), 'white', {renderer: 'canvas'});
        var option_5a71413b3a294df290079447f2776acb = {
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
                    "value": 368,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 181,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 152,
                    "name": "Python"
                },
                {
                    "value": 126,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 110,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 103,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 103,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 97,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 96,
                    "name": "C/C++"
                },
                {
                    "value": 59,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 55,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 55,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 51,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 51,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 45,
                    "name": "Java"
                },
                {
                    "value": 44,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 43,
                    "name": "C++"
                },
                {
                    "value": 41,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 36,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 35,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 34,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 33,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 31,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 31,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 30,
                    "name": "TensoFlow"
                },
                {
                    "value": 30,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 28,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 28,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 28,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 27,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 26,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 25,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 25,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 25,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 22,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 22,
                    "name": "PyTorch"
                },
                {
                    "value": 21,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 20,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 20,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 20,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 20,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 20,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 19,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 19,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 19,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 19,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 18,
                    "name": "NLP"
                },
                {
                    "value": 18,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 17,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 17,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 17,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 16,
                    "name": "OpenCV"
                },
                {
                    "value": 16,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 16,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 15,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 15,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 14,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 14,
                    "name": "SLAM"
                },
                {
                    "value": 14,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 14,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 14,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 14,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 14,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 13,
                    "name": "\u4e94\u9669\u4e00\u91d1"
                },
                {
                    "value": 13,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 13,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 13,
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 12,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 12,
                    "name": "nan"
                },
                {
                    "value": 12,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 11,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 11,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 11,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 10,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 10,
                    "name": "CNN"
                },
                {
                    "value": 10,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 10,
                    "name": "C"
                },
                {
                    "value": 10,
                    "name": "Hadoop"
                },
                {
                    "value": 10,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 10,
                    "name": "MATLAB"
                },
                {
                    "value": 9,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 9,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 9,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 9,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 9,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 9,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 8,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 8,
                    "name": "ROS"
                },
                {
                    "value": 8,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 8,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 8,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 8,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 8,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 8,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 8,
                    "name": "Caffe"
                },
                {
                    "value": 8,
                    "name": "Keras"
                },
                {
                    "value": 7,
                    "name": "\u7269\u6d41\u5e73\u53f0"
                },
                {
                    "value": 7,
                    "name": "\u5185\u5bb9\u8d44\u8baf"
                },
                {
                    "value": 7,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 7,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 7,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 7,
                    "name": "RNN"
                },
                {
                    "value": 7,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 7,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 7,
                    "name": "tensorflow"
                },
                {
                    "value": 7,
                    "name": "\u4fe1\u606f\u62bd\u53d6"
                },
                {
                    "value": 7,
                    "name": "Scala"
                },
                {
                    "value": 7,
                    "name": "AI"
                },
                {
                    "value": 6,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 6,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 6,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 6,
                    "name": "\u95ee\u7b54\u7cfb\u7edf"
                },
                {
                    "value": 6,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 6,
                    "name": "SQL"
                },
                {
                    "value": 6,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 6,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 6,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 6,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 6,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 6,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 6,
                    "name": "\u5730\u56fe"
                },
                {
                    "value": 6,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 6,
                    "name": "Spark"
                },
                {
                    "value": 6,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 5,
                    "name": "python"
                },
                {
                    "value": 5,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 5,
                    "name": "opencv"
                },
                {
                    "value": 5,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 5,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 5,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 5,
                    "name": "XGBoost"
                },
                {
                    "value": 5,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 5,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 5,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 5,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 5,
                    "name": "Golang"
                },
                {
                    "value": 5,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 5,
                    "name": "\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 5,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 4,
                    "name": "TensorFlow"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "MySQL"
                },
                {
                    "value": 4,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 4,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 4,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 4,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 4,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 4,
                    "name": "Linux"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u7ed3\u6784"
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
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 4,
                    "name": "Shell"
                },
                {
                    "value": 4,
                    "name": "Hive"
                },
                {
                    "value": 4,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 4,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 4,
                    "name": "ARM"
                },
                {
                    "value": 4,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 3,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 3,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 3,
                    "name": "pytorch"
                },
                {
                    "value": 3,
                    "name": "\u97f3\u9891\u5904\u7406"
                },
                {
                    "value": 3,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 3,
                    "name": "MXNet"
                },
                {
                    "value": 3,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 3,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 3,
                    "name": "slam"
                },
                {
                    "value": 3,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 3,
                    "name": "DSP"
                },
                {
                    "value": 3,
                    "name": "CV"
                },
                {
                    "value": 3,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 3,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 3,
                    "name": "nlp"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 3,
                    "name": "spark"
                },
                {
                    "value": 3,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 3,
                    "name": "GAN"
                },
                {
                    "value": 3,
                    "name": "\u6587\u672c\u8574\u6db5"
                },
                {
                    "value": 3,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
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
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 2,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 2,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 2,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 2,
                    "name": "\u7b56\u7565\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u6458\u8981"
                },
                {
                    "value": 2,
                    "name": "Flink"
                },
                {
                    "value": 2,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 2,
                    "name": "ETL"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 2,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 2,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 2,
                    "name": "matlab"
                },
                {
                    "value": 2,
                    "name": "salm"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "opengl"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 2,
                    "name": "ETA"
                },
                {
                    "value": 2,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 2,
                    "name": "SFM"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 2,
                    "name": "3D"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "linux"
                },
                {
                    "value": 2,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "C#"
                },
                {
                    "value": 2,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 2,
                    "name": "\u52a8\u6001\u89c4\u5212"
                },
                {
                    "value": 2,
                    "name": "OCR"
                },
                {
                    "value": 2,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 2,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 2,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 2,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 2,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u7814\u7a76"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "VIO"
                },
                {
                    "value": 1,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "\u98de\u884c\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "AI\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u51b3\u7b56\u6811"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "MDP"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "OpenCL"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u8fb9\u7f18\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 1,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "AB\u5206\u6d41"
                },
                {
                    "value": 1,
                    "name": "cmake"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "\u79bb\u6563\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "BFM"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42"
                },
                {
                    "value": 1,
                    "name": "IMU"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u524d\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "\u5176\u4ed6"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4eea\u5668\u4eea\u8868"
                },
                {
                    "value": 1,
                    "name": "OpenGL"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "HALCON"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "go"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "automak"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u5916\u5e02\u573a"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "ACM"
                },
                {
                    "value": 1,
                    "name": "PSENET"
                },
                {
                    "value": 1,
                    "name": "\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u7ed8"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "ElasticSearch"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "DICOM"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u94a5\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "JavaScript"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5377\u79ef"
                },
                {
                    "value": 1,
                    "name": "docker"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6821\u51c6"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "LIDAR"
                },
                {
                    "value": 1,
                    "name": "labview"
                },
                {
                    "value": 1,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "Pthon"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u5ba4\u5185\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u7a7f\u6234"
                },
                {
                    "value": 1,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 1,
                    "name": "SQLServer"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "filnk"
                },
                {
                    "value": 1,
                    "name": "\u5e93\u5b58\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "WIFI"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "rpc"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "Tensorflow"
                },
                {
                    "value": 1,
                    "name": "SNN"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "hbase"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "AlphaGo"
                },
                {
                    "value": 1,
                    "name": "Sox"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "SLAM\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66"
                },
                {
                    "value": 1,
                    "name": "CAD"
                },
                {
                    "value": 1,
                    "name": "torch"
                },
                {
                    "value": 1,
                    "name": "CRNN"
                },
                {
                    "value": 1,
                    "name": "ensorFlow"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u6807\u5b9a\u7f16\u7801"
                },
                {
                    "value": 1,
                    "name": "\u6c42\u89e3\u5668"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217"
                },
                {
                    "value": 1,
                    "name": "caffe"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "NRI"
                },
                {
                    "value": 1,
                    "name": "\u8272\u8c31\u5149\u8c31"
                },
                {
                    "value": 1,
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u9002\u5e94"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u89e3"
                },
                {
                    "value": 1,
                    "name": "rank"
                },
                {
                    "value": 1,
                    "name": "FPGA\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u8fd0\u8425"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "SSL/TLS"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u822a\u5929"
                },
                {
                    "value": 1,
                    "name": "\u540e\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "GIS"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u60ef\u6027\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "Avatar"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u667a\u80fd"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "3d\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u753b\u50cf\u5efa\u6a21"
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
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "HQRank"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "vSLAM"
                },
                {
                    "value": 1,
                    "name": "FPGA"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "pytroch"
                },
                {
                    "value": 1,
                    "name": "\u8499\u7279\u5361\u6d1b"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u7535\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u914d\u9001\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "PUSH\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "Fliter"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4ef7"
                },
                {
                    "value": 1,
                    "name": "Oracle"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "VO/VIO"
                },
                {
                    "value": 1,
                    "name": "LiDAR"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u53d1"
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
                    "name": "\u671f\u6743\u6fc0\u52b1"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u4fe1\u606f\u5316"
                },
                {
                    "value": 1,
                    "name": "\u84dd\u7259"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u8f6c\u5316\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "hadoop"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206"
                },
                {
                    "value": 1,
                    "name": "HADOOP"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4"
                },
                {
                    "value": 1,
                    "name": "DSP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u70df\u96fe\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "vivado"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u65e5\u7167\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "Pytorch"
                },
                {
                    "value": 1,
                    "name": "\u591a\u65b9\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "O2O"
                },
                {
                    "value": 1,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u89c6\u5316"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u914d\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u5206\u7c7b"
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
        chart_5a71413b3a294df290079447f2776acb.setOption(option_5a71413b3a294df290079447f2776acb);
    </script>
                <div id="d764ec96bab0423b82258728b0cbc9b8" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d764ec96bab0423b82258728b0cbc9b8 = echarts.init(
            document.getElementById('d764ec96bab0423b82258728b0cbc9b8'), 'white', {renderer: 'canvas'});
        var option_d764ec96bab0423b82258728b0cbc9b8 = {
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
                778,
                370,
                64,
                57,
                27,
                13,
                7,
                4
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
                    "value": 778
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 370
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 64
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 57
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 27
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 13
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 7
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
                    "value": 4
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
                    "value": 778
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 370
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 64
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 57
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 27
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 13
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 7
                },
                {
                    "name": "\u5e94\u5c4a / \u535a\u58eb",
                    "value": 4
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
        chart_d764ec96bab0423b82258728b0cbc9b8.setOption(option_d764ec96bab0423b82258728b0cbc9b8);
    </script>
                <div id="b5dcc54ba4bd48c8916ef29fa98c5acf" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b5dcc54ba4bd48c8916ef29fa98c5acf = echarts.init(
            document.getElementById('b5dcc54ba4bd48c8916ef29fa98c5acf'), 'white', {renderer: 'canvas'});
        var option_b5dcc54ba4bd48c8916ef29fa98c5acf = {
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
                553,
                275,
                211,
                146,
                132,
                6,
                1
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
                    "value": 553
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 275
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 211
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 146
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 132
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 6
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 1
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
                    "value": 553
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 275
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 211
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 146
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 132
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 6
                },
                {
                    "name": "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                    "value": 1
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
        chart_b5dcc54ba4bd48c8916ef29fa98c5acf.setOption(option_b5dcc54ba4bd48c8916ef29fa98c5acf);
    </script>
                <div id="9521eb86ed5441ebbb89a8781a8da399" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9521eb86ed5441ebbb89a8781a8da399 = echarts.init(
            document.getElementById('9521eb86ed5441ebbb89a8781a8da399'), 'white', {renderer: 'canvas'});
        var option_9521eb86ed5441ebbb89a8781a8da399 = {
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
                            "color": "rgb(56,68,65)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,25,92)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,30,39)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,27,107)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,91,98)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,83,91)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,17,92)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,133,27)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,114,0)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,144,80)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,141,68)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,95,116)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,73,115)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,49,156)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,21,23)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,148,54)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,19,26)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,4,8)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,25,143)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,79,113)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,23,118)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,18,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,120,25)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,152,23)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,103,109)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,18,127)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,130,132)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,63,61)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,159,6)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,25,156)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,53,109)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,74,29)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,73,88)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,68,86)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,154,44)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,122,110)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,16,38)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,71,132)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,113,115)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,98,118)"
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
        chart_9521eb86ed5441ebbb89a8781a8da399.setOption(option_9521eb86ed5441ebbb89a8781a8da399);
    </script>
                <div id="34e0428a8c9e46c09b6aa290e23924c6" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_34e0428a8c9e46c09b6aa290e23924c6 = echarts.init(
            document.getElementById('34e0428a8c9e46c09b6aa290e23924c6'), 'white', {renderer: 'canvas'});
        var option_34e0428a8c9e46c09b6aa290e23924c6 = {
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
                            "color": "rgb(75,13,142)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,15,23)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,84,156)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,64,60)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,93,149)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,76,69)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,79,139)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,11,153)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,139,88)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,88,156)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,110)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,13,82)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,10,84)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,85,29)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,95,63)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,141,156)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,158,104)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,151,53)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,111,80)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,69,29)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,156,75)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,88,15)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,117,79)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,89,61)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,142,115)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,129,50)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,120,105)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,114,133)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,145,52)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,141,10)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,4,94)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,114,46)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,28,62)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,43,11)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,50,54)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,152,53)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,96,128)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,11,154)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,30,118)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,154,63)"
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
        chart_34e0428a8c9e46c09b6aa290e23924c6.setOption(option_34e0428a8c9e46c09b6aa290e23924c6);
    </script>
                <div id="ad9396680ddb4ec79c2f4cfb295fb0d4" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ad9396680ddb4ec79c2f4cfb295fb0d4 = echarts.init(
            document.getElementById('ad9396680ddb4ec79c2f4cfb295fb0d4'), 'white', {renderer: 'canvas'});
        var option_ad9396680ddb4ec79c2f4cfb295fb0d4 = {
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
                            "color": "rgb(0,153,108)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,121,74)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,60,54)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,97,84)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,7,67)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,149,112)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,122,26)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,151,117)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,52,112)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,115,85)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,23,140)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,74,104)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,25,26)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,104,8)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,79,100)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,132,51)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,12,41)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,11,44)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,117,0)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,147,149)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,67,148)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,61,94)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,91,106)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,120,152)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,135,129)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,44,139)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,106,79)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,83,75)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,3,68)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,129,118)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,49,40)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,17,3)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,128,38)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,152,106)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,130,112)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,80,132)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,25,46)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,11,141)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,36,153)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,28,72)"
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
        chart_ad9396680ddb4ec79c2f4cfb295fb0d4.setOption(option_ad9396680ddb4ec79c2f4cfb295fb0d4);
    </script>
                <div id="3e03b6856f9849e38fbf4fabebb3764c" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_3e03b6856f9849e38fbf4fabebb3764c = echarts.init(
            document.getElementById('3e03b6856f9849e38fbf4fabebb3764c'), 'white', {renderer: 'canvas'});
        var option_3e03b6856f9849e38fbf4fabebb3764c = {
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
                            "color": "rgb(148,95,149)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,75,61)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,35,142)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,18,123)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,129,74)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,129,60)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,143,24)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,91,86)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,151,74)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,137,145)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,20,122)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,111,113)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,28,109)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,62,47)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,68,37)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,122,144)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,152,67)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,37,154)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,67,45)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,20,94)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,49,112)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,58,96)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,109,45)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,127,120)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,66,141)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,85,88)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,116,1)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,59,107)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,74,133)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,122,10)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,72,49)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,32,47)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,110,148)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,119,125)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,109,44)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,127,25)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,80,42)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,157,118)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,48,16)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,106,107)"
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
        chart_3e03b6856f9849e38fbf4fabebb3764c.setOption(option_3e03b6856f9849e38fbf4fabebb3764c);
    </script>
                <div id="d6df3647875643899b357526955a80bc" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d6df3647875643899b357526955a80bc = echarts.init(
            document.getElementById('d6df3647875643899b357526955a80bc'), 'white', {renderer: 'canvas'});
        var option_d6df3647875643899b357526955a80bc = {
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
                            "color": "rgb(15,53,4)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,71,37)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,21,116)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,31,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,120,136)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,36,141)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,120,100)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,37,16)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,114,147)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,47,80)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,139,70)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,142,9)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,35,160)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,93,22)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,89,35)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,129,58)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,105,129)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,106,40)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,126,120)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,9,155)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,114,82)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,131,18)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,142,147)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,78,107)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,14,120)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,107,35)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,111,15)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,141,149)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,160,106)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,14,112)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,114,56)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,31,106)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,96,2)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,70,22)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,63,18)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,128,95)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,118,37)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,54,27)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,66,88)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,80,154)"
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
        chart_d6df3647875643899b357526955a80bc.setOption(option_d6df3647875643899b357526955a80bc);
    </script>
                <div id="b2df88ecd91e43b9b7eb916892f04636" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b2df88ecd91e43b9b7eb916892f04636 = echarts.init(
            document.getElementById('b2df88ecd91e43b9b7eb916892f04636'), 'white', {renderer: 'canvas'});
        var option_b2df88ecd91e43b9b7eb916892f04636 = {
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
                            "color": "rgb(35,47,1)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,48,110)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,117,107)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,8,83)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,80,35)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,4,33)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,107,72)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,140,58)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,82,81)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,153,27)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,22,56)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,69,60)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,70,41)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,154,112)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,91,0)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,67,38)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,65,117)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,86,126)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,113,90)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,59,9)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,76,78)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,44,131)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,123,17)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,26,76)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,155,27)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,48,99)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,22,116)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,137,106)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,54,76)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,34,95)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,62,12)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,130,36)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,125,32)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,140,4)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,154,130)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,154,133)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,151,157)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,148,144)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,25,112)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,83,138)"
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
        chart_b2df88ecd91e43b9b7eb916892f04636.setOption(option_b2df88ecd91e43b9b7eb916892f04636);
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
