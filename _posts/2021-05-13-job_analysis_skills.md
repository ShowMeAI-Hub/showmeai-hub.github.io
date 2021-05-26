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

<h2>（2021-05-26更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, 'c2d96b3fc1d44f9383df9b3b45cbd901')">关键词</button>
            <button class="tablinks" onclick="showChart(event, '0db972f0daac45b89acf4e78aa794069')">关键词分布</button>
            <button class="tablinks" onclick="showChart(event, 'e4df0af1556b4b64b7712484143f6392')">学历要求</button>
            <button class="tablinks" onclick="showChart(event, '3b8363dbd241419bbfa34731338922eb')">经验要求</button>
            <button class="tablinks" onclick="showChart(event, '39e4e09c36544f2591ef3d7c9f0c178b')">NLP岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '7c8fe1e88fff48d28c862a609e202658')">NLP任职要求</button>
            <button class="tablinks" onclick="showChart(event, '8aebcb38de1b47208fe166602aa04082')">CV岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '99007c7d41e1496482dba07f69926f2e')">CV任职要求</button>
            <button class="tablinks" onclick="showChart(event, '49d375c0bb6f4699b66facabaab24089')">推荐算法岗位职责</button>
            <button class="tablinks" onclick="showChart(event, '9e2b27e3360943f49beae05acd64196f')">推荐算法任职要求</button>
    </div>

    <div class="box">
                <div id="c2d96b3fc1d44f9383df9b3b45cbd901" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_c2d96b3fc1d44f9383df9b3b45cbd901 = echarts.init(
            document.getElementById('c2d96b3fc1d44f9383df9b3b45cbd901'), 'white', {renderer: 'canvas'});
            
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
    
        var option_c2d96b3fc1d44f9383df9b3b45cbd901 = {
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
                657,
                342,
                270,
                213,
                182,
                175,
                169
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
                    "value": 657,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,141,160)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 342,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,67,88)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 270,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,113,107)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 213,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,91,93)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 182,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,156,7)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 175,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,33,35)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u8bc6\u522b",
                    "value": 169,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,86,81)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 169,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,69,125)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 169,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,119,100)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b",
                    "value": 101,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,19,75)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,87,112)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,43,153)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,2,136)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,44,17)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,93,15)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,92,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,34,11)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u5f0f\u8bc6\u522b",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,63,145)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,59,51)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,128,140)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,47,83)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,160,128)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,103,140)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 54,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,50,108)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,22,34)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,93,24)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,118,85)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,128,101)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b",
                    "value": 50,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,11,121)"
                        }
                    }
                },
                {
                    "name": "TensoFlow",
                    "value": 49,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,10,145)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,3,131)"
                        }
                    }
                },
                {
                    "name": "NLP",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,75,76)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,62,158)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,28,48)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,148,58)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,136,48)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,34,140)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,66,87)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,41,0)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,96,12)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,152,49)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,50,134)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,63,124)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,100,49)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,126,123)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,54,73)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5065\u5eb7",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,87,105)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,148,103)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,82,52)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,20,50)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 31,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,46,41)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u8bc6\u522b",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,95,41)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,145,42)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,31,76)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,27,82)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef\u5f00\u53d1",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,71,42)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u8bc6\u522b",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,140,27)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,46,39)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,69,79)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,27,7)"
                        }
                    }
                },
                {
                    "name": "nan",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,55,105)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u751f\u6210",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,115,102)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,120,69)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ba1\u7b97",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,65,31)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,136,145)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,34,3)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,144,83)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,101,131)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,140,56)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,47,154)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,122,63)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,137,13)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,112,148)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,157,109)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,31,152)"
                        }
                    }
                },
                {
                    "name": "C",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,111,33)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,125,91)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u673a\u5668\u4eba",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,122,15)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,49,31)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,31,18)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,81,52)"
                        }
                    }
                },
                {
                    "name": "MATLAB",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,152,54)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,8,17)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,1,77)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,160)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,11,142)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,120,47)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,136,24)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,73,138)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,114,38)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,33,49)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u9879\u5956\u91d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,76,64)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,152,15)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,67,75)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,128,97)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u6a21",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,49,70)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,109,104)"
                        }
                    }
                },
                {
                    "name": "SQL",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,147,115)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,17,99)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u670d\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,109,66)"
                        }
                    }
                },
                {
                    "name": "Scala",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,152,87)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,9,51)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,118,90)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,2,53)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,79,154)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,123,112)"
                        }
                    }
                },
                {
                    "name": "XGBoost",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,120,82)"
                        }
                    }
                },
                {
                    "name": "ROS",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,151,3)"
                        }
                    }
                },
                {
                    "name": "\u95ee\u7b54\u7cfb\u7edf",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,147,104)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,121,82)"
                        }
                    }
                },
                {
                    "name": "\u53e5\u6cd5\u5206\u6790",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,85,47)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,96,35)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,20,140)"
                        }
                    }
                },
                {
                    "name": "python",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,157,158)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,86,51)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,26,123)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,159,52)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,157,146)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u62bd\u53d6",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,65,60)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,102,107)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,97,4)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,96,126)"
                        }
                    }
                },
                {
                    "name": "\u8bcd\u6027\u6807\u6ce8",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,84,11)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,35,78)"
                        }
                    }
                },
                {
                    "name": "Caffe",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,128,71)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,53,139)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u6587\u5206\u8bcd",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,92,60)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,69,119)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,143,48)"
                        }
                    }
                },
                {
                    "name": "Golang",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,129,25)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,93,80)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,48,115)"
                        }
                    }
                },
                {
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,66,88)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,64,150)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,40,103)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u641c\u7d22",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,47,88)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u5efa\u6a21",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,87,55)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,39,66)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,153,75)"
                        }
                    }
                },
                {
                    "name": "MySQL",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,102,99)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,124,119)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,32,81)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,70,100)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,76,144)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,53,88)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u8ba1\u5212",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,75,1)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,34,107)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,117,89)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,13,103)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u8f6f\u4ef6",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,25,135)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4ea7\u5047",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,2,109)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5904\u7406",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,80,86)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,52,109)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,50,89)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,125,2)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,44,6)"
                        }
                    }
                },
                {
                    "name": "opencv",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,49,101)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,153,60)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,146,160)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,25,56)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u6d25\u8d34",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,89,98)"
                        }
                    }
                },
                {
                    "name": "Shell",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,112,147)"
                        }
                    }
                },
                {
                    "name": "spark",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,70,99)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,46,14)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,104,20)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,158,76)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,42,88)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,16,83)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,126,155)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,66,153)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,61,44)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,65,61)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,14,159)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u903c\u683c\u9ad8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,9,140)"
                        }
                    }
                },
                {
                    "name": "ARM",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,3,28)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,73,112)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u4e30\u539a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,97,149)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,19,39)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,57,89)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b\u4fe1\u606f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,6,101)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u5236\u9020",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,15,123)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,90,47)"
                        }
                    }
                },
                {
                    "name": "linux",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,53,28)"
                        }
                    }
                },
                {
                    "name": "Hive",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,147,152)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,31,76)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ed3\u6784",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,158,79)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,108,12)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,82,1)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,5,121)"
                        }
                    }
                },
                {
                    "name": "matlab",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,118,153)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,76,88)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,35,42)"
                        }
                    }
                },
                {
                    "name": "c++",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,21,140)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,49,2)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,153,47)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,20,124)"
                        }
                    }
                },
                {
                    "name": "slam",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,140,47)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u5904\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,30,154)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8574\u6db5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,48,100)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,3,38)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,67,59)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,133,84)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,2,92)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,62,111)"
                        }
                    }
                },
                {
                    "name": "nlp",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,44,65)"
                        }
                    }
                },
                {
                    "name": "3D",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,85,115)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5668\u68b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,131,118)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,135,102)"
                        }
                    }
                },
                {
                    "name": "\u540e\u7aef",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,41,22)"
                        }
                    }
                },
                {
                    "name": "Flink",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,44,46)"
                        }
                    }
                },
                {
                    "name": "salm",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,143,98)"
                        }
                    }
                },
                {
                    "name": "HALCON",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,9,64)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,49,68)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,34,71)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,5,89)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,104,26)"
                        }
                    }
                },
                {
                    "name": "CV",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,152,60)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,74,43)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,49,63)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,39,28)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5206",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,79,106)"
                        }
                    }
                },
                {
                    "name": "ROS\u7cfb\u7edf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,3,32)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u641c\u7d22",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,0,53)"
                        }
                    }
                },
                {
                    "name": "kaggle",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,80,22)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ed3\u5e93",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,22,92)"
                        }
                    }
                },
                {
                    "name": "SFM",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,99,123)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,132,4)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,158,146)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,114,11)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5973\u591a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,73,113)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,59,37)"
                        }
                    }
                },
                {
                    "name": "opengl",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,112,61)"
                        }
                    }
                },
                {
                    "name": "OpenGL",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,75,42)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,145,155)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,150,142)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,14,3)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,122,103)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,101,56)"
                        }
                    }
                },
                {
                    "name": "\u795e\u7ecf\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,133,156)"
                        }
                    }
                },
                {
                    "name": "\u8fea\u58eb\u5c3c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,154,130)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,60,91)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u67b6\u6784",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,148,85)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,24,79)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u6c42\u6781\u81f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,12,14)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,65,76)"
                        }
                    }
                },
                {
                    "name": "MXNet",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,109,45)"
                        }
                    }
                },
                {
                    "name": "DSP",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,39,107)"
                        }
                    }
                },
                {
                    "name": "C#",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,31,19)"
                        }
                    }
                },
                {
                    "name": "ETA",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,115,79)"
                        }
                    }
                },
                {
                    "name": "\u626b\u5730\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,89,131)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4f18\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,118,86)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,123,22)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,135,86)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,79,53)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,16,67)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,110,118)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u798f\u8ba1\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,76,51)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,152,17)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,62,11)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,67,129)"
                        }
                    }
                },
                {
                    "name": "go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,81,131)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,68,122)"
                        }
                    }
                },
                {
                    "name": "ETL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,36,130)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,22,52)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,63,68)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,132,48)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,49,76)"
                        }
                    }
                },
                {
                    "name": "GPU",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,51,86)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u54c1\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,109,147)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7b56\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,73,57)"
                        }
                    }
                },
                {
                    "name": "\u67b6\u6784\u5e08",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,53,101)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,119,47)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7406\u89e3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,128,72)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,140,28)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,155,136)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,26,132)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5efa\u6a21",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,82,93)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,29,12)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u95f4\u5e8f\u5217",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,152,158)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,29,12)"
                        }
                    }
                },
                {
                    "name": "RTK",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,160,102)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,125,3)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,41,1)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u5339\u914d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,53,118)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,80,104)"
                        }
                    }
                },
                {
                    "name": "SNN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,29,134)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,73,53)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,133,46)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,118,130)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,19,34)"
                        }
                    }
                },
                {
                    "name": "Pytorch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,58,118)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,18,5)"
                        }
                    }
                },
                {
                    "name": "\u9700\u6c42\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,71,32)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,111,107)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,88,50)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6293\u53d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,14,3)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,47,79)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,56,157)"
                        }
                    }
                },
                {
                    "name": "Go",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,64,113)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u8f85\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,77,100)"
                        }
                    }
                },
                {
                    "name": "\u539f\u578b\u8bbe\u8ba1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,75,101)"
                        }
                    }
                },
                {
                    "name": "docker",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,47,109)"
                        }
                    }
                },
                {
                    "name": "JAVA",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,85,19)"
                        }
                    }
                },
                {
                    "name": "\u8054\u90a6\u5b66\u4e60",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,20,105)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee\u89c6\u89c9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,109,80)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,35,117)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,2,91)"
                        }
                    }
                },
                {
                    "name": "Matlab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,118,109)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,25,92)"
                        }
                    }
                },
                {
                    "name": "LTE",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,127,70)"
                        }
                    }
                },
                {
                    "name": "PaddlePddle",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,71,127)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,125,93)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,94,24)"
                        }
                    }
                },
                {
                    "name": "GIS",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,20,71)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,8,95)"
                        }
                    }
                },
                {
                    "name": "JavaScript",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,47,29)"
                        }
                    }
                },
                {
                    "name": "\u672c\u5730\u751f\u6d3b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,116,130)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,130,38)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,76,27)"
                        }
                    }
                },
                {
                    "name": "\u6570\u4ed3\u67b6\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,25,57)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,22,13)"
                        }
                    }
                },
                {
                    "name": "\u7248\u9762\u5206\u6790",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,65,6)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,127,90)"
                        }
                    }
                },
                {
                    "name": "HADOOP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,42,67)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u7a0b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,38,12)"
                        }
                    }
                },
                {
                    "name": "\u964d\u566a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,102,26)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fAI\u7814\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,26,120)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,104,101)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,78,62)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6001\u89c4\u5212",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,73,89)"
                        }
                    }
                },
                {
                    "name": "AR",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,148,42)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,68,82)"
                        }
                    }
                },
                {
                    "name": "ACM",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,57,125)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,41,140)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,91,118)"
                        }
                    }
                },
                {
                    "name": "\u56de\u58f0\u6d88\u9664",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,90,146)"
                        }
                    }
                },
                {
                    "name": "\u8111\u673a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,73,132)"
                        }
                    }
                },
                {
                    "name": "\u9886\u519b\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,130,51)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,109,128)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,119,19)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,77,29)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u8ba1\u7b97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,62,120)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,3,157)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9slam",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,97,16)"
                        }
                    }
                },
                {
                    "name": "\u5e05\u54e5\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,35,117)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,5,134)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,43,82)"
                        }
                    }
                },
                {
                    "name": "CAD",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,105,31)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,38,41)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u8bd5\u5f00\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,14,137)"
                        }
                    }
                },
                {
                    "name": "OpenCL",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,159,140)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,39,120)"
                        }
                    }
                },
                {
                    "name": "AGV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,79,100)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,114,109)"
                        }
                    }
                },
                {
                    "name": "3D\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,129,128)"
                        }
                    }
                },
                {
                    "name": "c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,82,75)"
                        }
                    }
                },
                {
                    "name": "3D\u59ff\u6001\u91cd\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,16,27)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,127,45)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,51,95)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,157,36)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,141,67)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,0,3)"
                        }
                    }
                },
                {
                    "name": "\u6574\u6570\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,93,95)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,139,10)"
                        }
                    }
                },
                {
                    "name": "\u5149\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,102,29)"
                        }
                    }
                },
                {
                    "name": "\u7279\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,41,59)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,5,103)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,106,0)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u65b9\u5411\u7b97\u6cd5\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,30,44)"
                        }
                    }
                },
                {
                    "name": "FPGA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,105,113)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,18,138)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,158,7)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u66fe\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,32,149)"
                        }
                    }
                },
                {
                    "name": "labview",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,42,136)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,113,50)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,11,28)"
                        }
                    }
                },
                {
                    "name": "hbase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,96,66)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,82,68)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,43,85)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,113,29)"
                        }
                    }
                },
                {
                    "name": "CGAL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,104,149)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u5316\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,72,113)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,122,61)"
                        }
                    }
                },
                {
                    "name": "\u692d\u5706\u66f2\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,68,109)"
                        }
                    }
                },
                {
                    "name": "\u9057\u4f20\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,140,125)"
                        }
                    }
                },
                {
                    "name": "Sox",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,18,136)"
                        }
                    }
                },
                {
                    "name": "Oracle",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,144,132)"
                        }
                    }
                },
                {
                    "name": "AlphaGo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,79,11)"
                        }
                    }
                },
                {
                    "name": "ensorFlow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,154,15)"
                        }
                    }
                },
                {
                    "name": "\u7edf\u8ba1\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,13,79)"
                        }
                    }
                },
                {
                    "name": "\u914d\u9001\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,18,149)"
                        }
                    }
                },
                {
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,114,46)"
                        }
                    }
                },
                {
                    "name": "\u4f3a\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,12,20)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,40,38)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ea4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,155,78)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,35,55)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u98de\u51cc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,1,37)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u624b\u6218\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,126,31)"
                        }
                    }
                },
                {
                    "name": "ranking",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,155,155)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,104,60)"
                        }
                    }
                },
                {
                    "name": "neon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,108,88)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,18,131)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u5bbd\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,3,58)"
                        }
                    }
                },
                {
                    "name": "\u80a2\u4f53\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,114,151)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,98,160)"
                        }
                    }
                },
                {
                    "name": "h264\uff0ch265\uff0cav1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,152,9)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,58,20)"
                        }
                    }
                },
                {
                    "name": "numpy",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,121,16)"
                        }
                    }
                },
                {
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,60,26)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,65,98)"
                        }
                    }
                },
                {
                    "name": "C++/python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,99,33)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,88,140)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,91,83)"
                        }
                    }
                },
                {
                    "name": "\u836f\u7269\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,97,33)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,157,134)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,160,97)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,44,11)"
                        }
                    }
                },
                {
                    "name": "\u5730\u7406\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,56,48)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,24,130)"
                        }
                    }
                },
                {
                    "name": "\u5341\u70b9\u5f00\u5de5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,131,126)"
                        }
                    }
                },
                {
                    "name": "H.264/265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,54,75)"
                        }
                    }
                },
                {
                    "name": "rpc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,148,132)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,149,156)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,153,71)"
                        }
                    }
                },
                {
                    "name": "\u59ff\u6001\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,22,26)"
                        }
                    }
                },
                {
                    "name": "NRI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,46,122)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,104,137)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,30,71)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,71,44)"
                        }
                    }
                },
                {
                    "name": "AILab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,11,132)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,146,107)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,16,28)"
                        }
                    }
                },
                {
                    "name": "\u753b\u50cf\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,158,22)"
                        }
                    }
                },
                {
                    "name": "ORBSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,105,115)"
                        }
                    }
                },
                {
                    "name": "webGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,68,98)"
                        }
                    }
                },
                {
                    "name": "B2B",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,119,106)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,104,23)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,10,24)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,134,158)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,21,124)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,83,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,7,87)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,90,120)"
                        }
                    }
                },
                {
                    "name": "/Pytorch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,56,75)"
                        }
                    }
                },
                {
                    "name": "DSP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,39,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,128,24)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,150,33)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,101,99)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u8f6c\u6362",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,129,39)"
                        }
                    }
                },
                {
                    "name": "ECC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,12,52)"
                        }
                    }
                },
                {
                    "name": "GPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,144,35)"
                        }
                    }
                },
                {
                    "name": "ESMM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,153,124)"
                        }
                    }
                },
                {
                    "name": "PUSH\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,86,94)"
                        }
                    }
                },
                {
                    "name": "Cortex-M\u6838",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,50,62)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,112,27)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,119,111)"
                        }
                    }
                },
                {
                    "name": "flv\uff0cmp3\uff0cmp4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,118,41)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,137,44)"
                        }
                    }
                },
                {
                    "name": "NLP/CV",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,61,57)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u7ea2\u5916",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,95,93)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u79d1\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,32,53)"
                        }
                    }
                },
                {
                    "name": "\u4eea\u5668\u4eea\u8868",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,110,14)"
                        }
                    }
                },
                {
                    "name": "h264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,128,154)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,55,37)"
                        }
                    }
                },
                {
                    "name": "\u536b\u661f\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,48,14)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,109,80)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,77,103)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,47,146)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u62df\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,37,116)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,37,40)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,122,99)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,89,40)"
                        }
                    }
                },
                {
                    "name": "\u60ef\u6027\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,124,55)"
                        }
                    }
                },
                {
                    "name": "hadoop",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,8,1)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,75,63)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,94,53)"
                        }
                    }
                },
                {
                    "name": "LiDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,116,155)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,81,113)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,54,116)"
                        }
                    }
                },
                {
                    "name": "SVC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,132,71)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u9884\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,38,114)"
                        }
                    }
                },
                {
                    "name": "\u9891\u8c31\u76d1\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,143,14)"
                        }
                    }
                },
                {
                    "name": "\u901f\u5ea6\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,36,67)"
                        }
                    }
                },
                {
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,26,80)"
                        }
                    }
                },
                {
                    "name": "MIMO\u96f7\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,156,90)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,71,118)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,90,31)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,111,36)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,101,42)"
                        }
                    }
                },
                {
                    "name": "\u6c42\u89e3\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,87,21)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,25,117)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,84,151)"
                        }
                    }
                },
                {
                    "name": "\u62a0\u56fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,32,92)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,109,144)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,153,120)"
                        }
                    }
                },
                {
                    "name": "\u516c\u94a5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,107,36)"
                        }
                    }
                },
                {
                    "name": "\u7cfb\u7edf\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,111,12)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u989c\u7f8e\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,74,115)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,18,36)"
                        }
                    }
                },
                {
                    "name": "DICOM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,138,140)"
                        }
                    }
                },
                {
                    "name": "\u8499\u7279\u5361\u6d1b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,159,19)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,155,124)"
                        }
                    }
                },
                {
                    "name": "shell",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,22,129)"
                        }
                    }
                },
                {
                    "name": "SaaS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,6,60)"
                        }
                    }
                },
                {
                    "name": "SQLServer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,18,58)"
                        }
                    }
                },
                {
                    "name": "3d\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,6,116)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,13,34)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u57fa\u7840",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,83,32)"
                        }
                    }
                },
                {
                    "name": "python/go",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,21,126)"
                        }
                    }
                },
                {
                    "name": "query",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,152,93)"
                        }
                    }
                },
                {
                    "name": "ADAS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,34,50)"
                        }
                    }
                },
                {
                    "name": "webgl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,158,153)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5377\u79ef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,108,17)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,125,41)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,133,83)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,74,64)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,150,57)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Tensorfl",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,67,70)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,79,104)"
                        }
                    }
                },
                {
                    "name": "FPGA\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,90,86)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u7a7f\u6234",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,91,96)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,46,75)"
                        }
                    }
                },
                {
                    "name": "x265",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,130,137)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,41,52)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,52,160)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,141,37)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,141,98)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,45,139)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,0,62)"
                        }
                    }
                },
                {
                    "name": "android",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,152,67)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,95,2)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,105,84)"
                        }
                    }
                },
                {
                    "name": "libvpx",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,150,158)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,35,63)"
                        }
                    }
                },
                {
                    "name": "AB\u5206\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,90,136)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,34,119)"
                        }
                    }
                },
                {
                    "name": "O2O",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,147,114)"
                        }
                    }
                },
                {
                    "name": "KF/EKF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,128,73)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,138,12)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,59,86)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,11,103)"
                        }
                    }
                },
                {
                    "name": "pytroch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,93,88)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,19,152)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u62e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,122,1)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,68,148)"
                        }
                    }
                },
                {
                    "name": "ISP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,11,4)"
                        }
                    }
                },
                {
                    "name": "jaya",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,51,0)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u8c03\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,106,103)"
                        }
                    }
                },
                {
                    "name": "\u751f\u4ea7\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,86,56)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u63d0\u53d6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,49,48)"
                        }
                    }
                },
                {
                    "name": "AEC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,39,15)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,140,151)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6cca\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,51,124)"
                        }
                    }
                },
                {
                    "name": "3dmm",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,22,7)"
                        }
                    }
                },
                {
                    "name": "VTK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,74,154)"
                        }
                    }
                },
                {
                    "name": "CRNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,73,135)"
                        }
                    }
                },
                {
                    "name": "\u6c34\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,107,72)"
                        }
                    }
                },
                {
                    "name": "VINS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,58,159)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,27,139)"
                        }
                    }
                },
                {
                    "name": "automak",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,19,107)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,100,24)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,77,47)"
                        }
                    }
                },
                {
                    "name": "NR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,54,33)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,104,119)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,32,1)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,4,27)"
                        }
                    }
                },
                {
                    "name": "\u6216",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,151,145)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8fd0\u8f93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,120,150)"
                        }
                    }
                },
                {
                    "name": "\u70df\u96fe\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,51,158)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,64,52)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a9\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,14,143)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,53,100)"
                        }
                    }
                },
                {
                    "name": "PPP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,39,80)"
                        }
                    }
                },
                {
                    "name": "\u78c1\u529b\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,39,101)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,36,91)"
                        }
                    }
                },
                {
                    "name": "Windows",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,117,156)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,40,97)"
                        }
                    }
                },
                {
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,62,101)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,152,131)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,21,9)"
                        }
                    }
                },
                {
                    "name": "dl4j",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,7,63)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,28,85)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u793e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,45,26)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,85,68)"
                        }
                    }
                },
                {
                    "name": "rank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,134,135)"
                        }
                    }
                },
                {
                    "name": "SSL/TLS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,90,86)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,140,138)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,153,68)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u641c\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,133,65)"
                        }
                    }
                },
                {
                    "name": "\u591c\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,54,9)"
                        }
                    }
                },
                {
                    "name": "AIOPS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,20,122)"
                        }
                    }
                },
                {
                    "name": "vr\u3002ar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,47,43)"
                        }
                    }
                },
                {
                    "name": "\u9a71\u52a8\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,66,73)"
                        }
                    }
                },
                {
                    "name": "ERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,99,152)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,75,121)"
                        }
                    }
                },
                {
                    "name": "PHM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,34,35)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,142,144)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,50,67)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,7)"
                        }
                    }
                },
                {
                    "name": "\u8272\u8c31\u5149\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,148,135)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,73,12)"
                        }
                    }
                },
                {
                    "name": "JitterBuffer",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,147,69)"
                        }
                    }
                },
                {
                    "name": "rgbd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,98,6)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,132,153)"
                        }
                    }
                },
                {
                    "name": "pandas",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,2,130)"
                        }
                    }
                },
                {
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,95,13)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,122,92)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u6a21\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,82,106)"
                        }
                    }
                },
                {
                    "name": "\u6846\u67b6\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,49,92)"
                        }
                    }
                },
                {
                    "name": "IMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,156,20)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,32,46)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,130,61)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,91,150)"
                        }
                    }
                },
                {
                    "name": "\u6295\u8d44/\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,146,0)"
                        }
                    }
                },
                {
                    "name": "5G",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,64,88)"
                        }
                    }
                },
                {
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,35,86)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,67,143)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,144,70)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,24,18)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,144,157)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4fe1\u606f\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,15,152)"
                        }
                    }
                },
                {
                    "name": "\u773c\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,71,77)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,50,89)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,108,98)"
                        }
                    }
                },
                {
                    "name": "\u77e9\u9635\u5206\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,105,121)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,0,150)"
                        }
                    }
                },
                {
                    "name": "VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,110,103)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,81,27)"
                        }
                    }
                },
                {
                    "name": "\u57fa\u7840\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,50,147)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,82,154)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,149,115)"
                        }
                    }
                },
                {
                    "name": "AGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,40,48)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u98ce\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,103,119)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,157,153)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,27,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,8,76)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u4f5c\u6355\u6349",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,44,61)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,25,37)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u89c6\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,146,86)"
                        }
                    }
                },
                {
                    "name": "\u98de\u884c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,134,42)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,50,41)"
                        }
                    }
                },
                {
                    "name": "filnk",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,29,25)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,103,94)"
                        }
                    }
                },
                {
                    "name": "VO/VIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,82,160)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,56,35)"
                        }
                    }
                },
                {
                    "name": "isp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,1,11)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,6,99)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u8fd0\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,155,69)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,15,111)"
                        }
                    }
                },
                {
                    "name": "pil",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,158,55)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,153,22)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,120,88)"
                        }
                    }
                },
                {
                    "name": "Node.js",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,60,118)"
                        }
                    }
                },
                {
                    "name": "\u907f\u969c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,16,61)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,93,152)"
                        }
                    }
                },
                {
                    "name": "POI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,7,137)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,95,102)"
                        }
                    }
                },
                {
                    "name": "WIFI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,16,20)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,142,92)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,29,147)"
                        }
                    }
                },
                {
                    "name": "\u591a\u65b9\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,82,34)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,133,12)"
                        }
                    }
                },
                {
                    "name": "NPL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,125,60)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,19,18)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,32,150)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,130,87)"
                        }
                    }
                },
                {
                    "name": "ElasticSearch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,147,56)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,115,4)"
                        }
                    }
                },
                {
                    "name": "\u9009\u578b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,159,20)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,0,90)"
                        }
                    }
                },
                {
                    "name": "\u540e\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,64,66)"
                        }
                    }
                },
                {
                    "name": "\u7535\u63a7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,93,156)"
                        }
                    }
                },
                {
                    "name": "Tensor",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,106,59)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,141,113)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,77,86)"
                        }
                    }
                },
                {
                    "name": "HBase",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,78,35)"
                        }
                    }
                },
                {
                    "name": "\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,76,109)"
                        }
                    }
                },
                {
                    "name": "R",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,69,37)"
                        }
                    }
                },
                {
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,92,103)"
                        }
                    }
                },
                {
                    "name": "Fliter",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,143,137)"
                        }
                    }
                },
                {
                    "name": "nlp\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,0,42)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u6392\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,29,133)"
                        }
                    }
                },
                {
                    "name": "\u524d\u65b9\u4ea4\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,27,160)"
                        }
                    }
                },
                {
                    "name": "flow",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,144,56)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,14,157)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,40,145)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,111,52)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,55,101)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,155,137)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,94,93)"
                        }
                    }
                },
                {
                    "name": "\u624b\u52bf\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,43,58)"
                        }
                    }
                },
                {
                    "name": "UWB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,116,36)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,122,159)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u8bbe\u8ba1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,133,35)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,32,1)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u822a\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,85,57)"
                        }
                    }
                },
                {
                    "name": "\u6d4b\u7ed8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,31,139)"
                        }
                    }
                },
                {
                    "name": "\u8bad\u7ec3\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,140,51)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,37,30)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u5927\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,62,5)"
                        }
                    }
                },
                {
                    "name": "FLINK",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,33,151)"
                        }
                    }
                },
                {
                    "name": "\u52aa\u529b\u53d8\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,97,120)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,109,158)"
                        }
                    }
                },
                {
                    "name": "\u652f\u4ed8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,102,144)"
                        }
                    }
                },
                {
                    "name": "torch",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,59,67)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,110,46)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u524d\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,44,113)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,21,81)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,13,146)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,38,26)"
                        }
                    }
                },
                {
                    "name": "Rust",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,100,114)"
                        }
                    }
                },
                {
                    "name": "openGL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,157,58)"
                        }
                    }
                },
                {
                    "name": "react",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,104,120)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,101,63)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,117,109)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,126,20)"
                        }
                    }
                },
                {
                    "name": "\u6807\u5b9a\u7f16\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,35,45)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,32,133)"
                        }
                    }
                },
                {
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,118,81)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5b89\u9632",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,11,101)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544aCTR/CVR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,97,87)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u6d4b\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,23,56)"
                        }
                    }
                },
                {
                    "name": "DNN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,35,153)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u7167\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,84,43)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,36,151)"
                        }
                    }
                },
                {
                    "name": "MCU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,138,154)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u6210\u7535\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,126,31)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,142,55)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,97,132)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u6316\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,132,74)"
                        }
                    }
                },
                {
                    "name": "C/C++/Python",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,133,13)"
                        }
                    }
                },
                {
                    "name": "CTR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,138,33)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,4,95)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,43,54)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,107,95)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,74,122)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,150,138)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,127,42)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u91c7\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,51,134)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,80,86)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,31,132)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,65,7)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,153,93)"
                        }
                    }
                },
                {
                    "name": "TF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,120,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,67,60)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,111,136)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u56fe\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,95,63)"
                        }
                    }
                },
                {
                    "name": "cmake",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,30,68)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,60,102)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,104,10)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u9002\u5e94",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,111,27)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,49,56)"
                        }
                    }
                },
                {
                    "name": "\u8fb9\u7f18\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,93,85)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u7259",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,109,137)"
                        }
                    }
                },
                {
                    "name": "\u4e8c\u5206\u7c7b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,67,7)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,134,115)"
                        }
                    }
                },
                {
                    "name": "kalman",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,55,81)"
                        }
                    }
                },
                {
                    "name": "Lucene",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,8,46)"
                        }
                    }
                },
                {
                    "name": "XGB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,66,17)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u98ce\u63a7AI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,158,21)"
                        }
                    }
                },
                {
                    "name": "Caffe\u3001Pytorch\u3001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,75,90)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,16,105)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,108,39)"
                        }
                    }
                },
                {
                    "name": "LIDAR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,49,109)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,127,151)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,106,30)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,154,49)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,90,94)"
                        }
                    }
                },
                {
                    "name": "NLP\u5904\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,121,78)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5238\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,109,144)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u5f15\u64ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,91,72)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5206\u5272",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,113,40)"
                        }
                    }
                },
                {
                    "name": "CAD\u56fe\u7eb8\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,116,155)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,148,136)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,8,160)"
                        }
                    }
                },
                {
                    "name": "CCF",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,29,20)"
                        }
                    }
                },
                {
                    "name": "\u914d\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,56,156)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,53,70)"
                        }
                    }
                },
                {
                    "name": "\u3001Spark",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,72,7)"
                        }
                    }
                },
                {
                    "name": "java",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,73,79)"
                        }
                    }
                },
                {
                    "name": "Avatar",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,16,27)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,104,57)"
                        }
                    }
                },
                {
                    "name": "HIve",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,64,12)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,19,79)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u53ec\u56de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,36,135)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,54,58)"
                        }
                    }
                },
                {
                    "name": "BFM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,46,14)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,150,113)"
                        }
                    }
                },
                {
                    "name": "3DGIS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,153,43)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,136,1)"
                        }
                    }
                },
                {
                    "name": "vivado",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,93,19)"
                        }
                    }
                },
                {
                    "name": "ACC/AEB/LKA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,79,137)"
                        }
                    }
                },
                {
                    "name": "HQRank",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,65,116)"
                        }
                    }
                },
                {
                    "name": "OpenMesh",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,156,96)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u539f\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,35,36)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u94a5\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,21,32)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5bfc\u822a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,106,149)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,20,4)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,71,69)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,21,45)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,45,90)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,88,58)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,103,76)"
                        }
                    }
                },
                {
                    "name": "\u79bb\u6563\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,67,38)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,8,12)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,5,29)"
                        }
                    }
                },
                {
                    "name": "MDP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,64,121)"
                        }
                    }
                },
                {
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,42,46)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,128,26)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,3,79)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,94,134)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u8fd0\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,91,95)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,152,95)"
                        }
                    }
                },
                {
                    "name": "3DCAD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,41,24)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,34,117)"
                        }
                    }
                },
                {
                    "name": "cuda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,98,62)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6\u52a0\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,102,120)"
                        }
                    }
                },
                {
                    "name": "/",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,22,82)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,94,49)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,11,76)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u4f18\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,40,59)"
                        }
                    }
                },
                {
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,21,87)"
                        }
                    }
                },
                {
                    "name": "Javascript",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,75,33)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u5b58\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,132,121)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,131,52)"
                        }
                    }
                },
                {
                    "name": "AI\u8d85\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,51,155)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,156,50)"
                        }
                    }
                },
                {
                    "name": "GNSS\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,144,41)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,70,40)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,28,154)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u76ee/\u53cc\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,147,58)"
                        }
                    }
                },
                {
                    "name": "SOA",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,96,2)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,85,160)"
                        }
                    }
                },
                {
                    "name": "hive",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,7,67)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,90,57)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,41,17)"
                        }
                    }
                },
                {
                    "name": "Pthon",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,13,1)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u9884\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,86,48)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u6587\u5206\u6790",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,149,74)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u6784\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,43,116)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,108,104)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,60,85)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u751f\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,129,106)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,74,81)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,24,14)"
                        }
                    }
                },
                {
                    "name": "caffe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,120,61)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,157,136)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5e38\u8bca\u65ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,77,149)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u8f91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,63,137)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,136,160)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,8,48)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,143,2)"
                        }
                    }
                },
                {
                    "name": "\u6821\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,54,113)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u89c4\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,136,148)"
                        }
                    }
                },
                {
                    "name": "DSP\u7f16\u7a0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,91,36)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b66\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,143)"
                        }
                    }
                },
                {
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,116,12)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,101,35)"
                        }
                    }
                },
                {
                    "name": "VR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,96,131)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de\u7b56\u7565",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,38,87)"
                        }
                    }
                },
                {
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,81,126)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,105,51)"
                        }
                    }
                },
                {
                    "name": "BIM+3D",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,89,26)"
                        }
                    }
                },
                {
                    "name": "\u8def\u51b5\u8ba1\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,140,133)"
                        }
                    }
                },
                {
                    "name": "X264",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,62,22)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,155,148)"
                        }
                    }
                },
                {
                    "name": "\u5373\u65f6\u901a\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,77,106)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,39,106)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,127,137)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51+",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,47,56)"
                        }
                    }
                },
                {
                    "name": "\u5ba4\u5185\u5b9a\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,138,127)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,30,148)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,3,33)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u51c6\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,30,153)"
                        }
                    }
                },
                {
                    "name": "vSLAM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,17,15)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u6d4b\u8bc4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,40,52)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u7b79\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,25,56)"
                        }
                    }
                },
                {
                    "name": "3D\u6253\u5370",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,70,65)"
                        }
                    }
                },
                {
                    "name": "PSENET",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,104,70)"
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
                "\u63a8\u8350\u7b97\u6cd5",
                "\u56fe\u50cf\u7b97\u6cd5",
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
        chart_c2d96b3fc1d44f9383df9b3b45cbd901.setOption(option_c2d96b3fc1d44f9383df9b3b45cbd901);
    </script>
                <div id="0db972f0daac45b89acf4e78aa794069" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0db972f0daac45b89acf4e78aa794069 = echarts.init(
            document.getElementById('0db972f0daac45b89acf4e78aa794069'), 'white', {renderer: 'canvas'});
        var option_0db972f0daac45b89acf4e78aa794069 = {
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
                    "value": 657,
                    "name": "\u6df1\u5ea6\u5b66\u4e60"
                },
                {
                    "value": 342,
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1"
                },
                {
                    "value": 270,
                    "name": "Python"
                },
                {
                    "value": 213,
                    "name": "\u6570\u636e\u6316\u6398"
                },
                {
                    "value": 182,
                    "name": "\u63a8\u8350\u7b97\u6cd5"
                },
                {
                    "value": 175,
                    "name": "\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 169,
                    "name": "\u56fe\u7247\u8bc6\u522b"
                },
                {
                    "value": 169,
                    "name": "\u673a\u5668\u5b66\u4e60"
                },
                {
                    "value": 169,
                    "name": "C/C++"
                },
                {
                    "value": 101,
                    "name": "\u4eba\u8138\u8bc6\u522b"
                },
                {
                    "value": 97,
                    "name": "\u7535\u5546\u5e73\u53f0"
                },
                {
                    "value": 87,
                    "name": "\u4eba\u5de5\u667a\u80fd"
                },
                {
                    "value": 84,
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406"
                },
                {
                    "value": 81,
                    "name": "Java"
                },
                {
                    "value": 77,
                    "name": "C++"
                },
                {
                    "value": 74,
                    "name": "\u641c\u7d22\u7b97\u6cd5"
                },
                {
                    "value": 74,
                    "name": "\u5927\u6570\u636e"
                },
                {
                    "value": 69,
                    "name": "\u6a21\u5f0f\u8bc6\u522b"
                },
                {
                    "value": 67,
                    "name": "\u6570\u636e\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 65,
                    "name": "\u8f6f\u4ef6\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 63,
                    "name": "\u667a\u80fd\u786c\u4ef6"
                },
                {
                    "value": 61,
                    "name": "\u7ee9\u6548\u5956\u91d1"
                },
                {
                    "value": 56,
                    "name": "\u79d1\u6280\u91d1\u878d"
                },
                {
                    "value": 54,
                    "name": "\u6280\u80fd\u57f9\u8bad"
                },
                {
                    "value": 52,
                    "name": "\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 51,
                    "name": "\u5e26\u85aa\u5e74\u5047"
                },
                {
                    "value": 50,
                    "name": "\u7269\u8054\u7f51"
                },
                {
                    "value": 50,
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51"
                },
                {
                    "value": 50,
                    "name": "\u8bed\u97f3\u8bc6\u522b"
                },
                {
                    "value": 49,
                    "name": "TensoFlow"
                },
                {
                    "value": 45,
                    "name": "\u5f39\u6027\u5de5\u4f5c"
                },
                {
                    "value": 43,
                    "name": "NLP"
                },
                {
                    "value": 43,
                    "name": "\u5c97\u4f4d\u664b\u5347"
                },
                {
                    "value": 42,
                    "name": "\u6241\u5e73\u7ba1\u7406"
                },
                {
                    "value": 42,
                    "name": "\u6587\u672c\u5206\u7c7b"
                },
                {
                    "value": 41,
                    "name": "\u81ea\u52a8\u9a7e\u9a76"
                },
                {
                    "value": 38,
                    "name": "\u7535\u5546"
                },
                {
                    "value": 35,
                    "name": "\u9886\u5bfc\u597d"
                },
                {
                    "value": 35,
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9"
                },
                {
                    "value": 34,
                    "name": "PyTorch"
                },
                {
                    "value": 34,
                    "name": "\u63a8\u8350\u7cfb\u7edf"
                },
                {
                    "value": 34,
                    "name": "\u65b0\u96f6\u552e"
                },
                {
                    "value": 33,
                    "name": "IT\u6280\u672f\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 33,
                    "name": "\u5728\u7ebf\u6559\u80b2"
                },
                {
                    "value": 33,
                    "name": "\u4e09\u7ef4\u56fe\u50cf\u89c6\u89c9"
                },
                {
                    "value": 33,
                    "name": "\u7b97\u6cd5"
                },
                {
                    "value": 32,
                    "name": "\u533b\u7597\u5065\u5eb7"
                },
                {
                    "value": 32,
                    "name": "\u76ee\u6807\u68c0\u6d4b"
                },
                {
                    "value": 32,
                    "name": "OpenCV"
                },
                {
                    "value": 31,
                    "name": "\u80a1\u7968\u671f\u6743"
                },
                {
                    "value": 31,
                    "name": "\u6e38\u620f"
                },
                {
                    "value": 30,
                    "name": "\u6587\u5b57\u8bc6\u522b"
                },
                {
                    "value": 30,
                    "name": "\u4e94\u9669\u4e00\u91d1"
                },
                {
                    "value": 30,
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1"
                },
                {
                    "value": 29,
                    "name": "\u793e\u4ea4\u5e73\u53f0"
                },
                {
                    "value": 29,
                    "name": "\u540e\u7aef\u5f00\u53d1"
                },
                {
                    "value": 25,
                    "name": "\u610f\u56fe\u8bc6\u522b"
                },
                {
                    "value": 24,
                    "name": "\u516d\u9669\u4e00\u91d1"
                },
                {
                    "value": 23,
                    "name": "\u97f3\u9891\uff5c\u89c6\u9891\u5a92\u4f53"
                },
                {
                    "value": 23,
                    "name": "\u641c\u7d22"
                },
                {
                    "value": 23,
                    "name": "nan"
                },
                {
                    "value": 22,
                    "name": "\u6587\u672c\u751f\u6210"
                },
                {
                    "value": 22,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u68c0\u6d4b"
                },
                {
                    "value": 21,
                    "name": "\u4e91\u8ba1\u7b97"
                },
                {
                    "value": 21,
                    "name": "\u5c31\u8fd1\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 20,
                    "name": "\u5b9a\u671f\u4f53\u68c0"
                },
                {
                    "value": 20,
                    "name": "\u6570\u636e\u670d\u52a1"
                },
                {
                    "value": 20,
                    "name": "\u8282\u65e5\u793c\u7269"
                },
                {
                    "value": 20,
                    "name": "Hadoop"
                },
                {
                    "value": 20,
                    "name": "\u514d\u8d39\u73ed\u8f66"
                },
                {
                    "value": 20,
                    "name": "\u97f3\u9891\u7b97\u6cd5"
                },
                {
                    "value": 19,
                    "name": "\u91d1\u878d"
                },
                {
                    "value": 19,
                    "name": "\u89c6\u9891/\u76d1\u63a7\u5206\u6790"
                },
                {
                    "value": 19,
                    "name": "\u5e74\u5e95\u53cc\u85aa"
                },
                {
                    "value": 19,
                    "name": "SLAM"
                },
                {
                    "value": 18,
                    "name": "C"
                },
                {
                    "value": 18,
                    "name": "\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 18,
                    "name": "\u670d\u52a1\u673a\u5668\u4eba"
                },
                {
                    "value": 17,
                    "name": "\u6559\u80b2"
                },
                {
                    "value": 17,
                    "name": "\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 16,
                    "name": "CNN"
                },
                {
                    "value": 16,
                    "name": "MATLAB"
                },
                {
                    "value": 16,
                    "name": "\u4fe1\u606f\u5b89\u5168"
                },
                {
                    "value": 16,
                    "name": "\u5728\u7ebf\u533b\u7597"
                },
                {
                    "value": 16,
                    "name": "\u5e7f\u544a\u8425\u9500"
                },
                {
                    "value": 15,
                    "name": "\u65c5\u6e38\uff5c\u51fa\u884c"
                },
                {
                    "value": 15,
                    "name": "\u4f01\u4e1a\u670d\u52a1"
                },
                {
                    "value": 14,
                    "name": "\u8bed\u97f3\u5408\u6210"
                },
                {
                    "value": 14,
                    "name": "\u6d88\u8d39\u751f\u6d3b"
                },
                {
                    "value": 14,
                    "name": "\u533b\u7597\u5f71\u50cf\u8bca\u65ad"
                },
                {
                    "value": 14,
                    "name": "\u8f85\u52a9/\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 13,
                    "name": "\u4e13\u9879\u5956\u91d1"
                },
                {
                    "value": 13,
                    "name": "\u77ed\u89c6\u9891"
                },
                {
                    "value": 13,
                    "name": "\u63a8\u8350"
                },
                {
                    "value": 12,
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020"
                },
                {
                    "value": 12,
                    "name": "\u5efa\u6a21"
                },
                {
                    "value": 12,
                    "name": "\u5185\u5bb9\u793e\u533a"
                },
                {
                    "value": 12,
                    "name": "SQL"
                },
                {
                    "value": 12,
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d"
                },
                {
                    "value": 12,
                    "name": "\u5e7f\u544a\u670d\u52a1"
                },
                {
                    "value": 12,
                    "name": "Scala"
                },
                {
                    "value": 11,
                    "name": "Keras"
                },
                {
                    "value": 11,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 11,
                    "name": "\u8425\u9500\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 11,
                    "name": "\u8def\u5f84\u89c4\u5212"
                },
                {
                    "value": 11,
                    "name": "\u7269\u6d41\uff5c\u8fd0\u8f93"
                },
                {
                    "value": 11,
                    "name": "XGBoost"
                },
                {
                    "value": 11,
                    "name": "ROS"
                },
                {
                    "value": 11,
                    "name": "\u95ee\u7b54\u7cfb\u7edf"
                },
                {
                    "value": 11,
                    "name": "\u533b\u7597\uff5c\u4fdd\u5065\uff5c\u7f8e\u5bb9"
                },
                {
                    "value": 11,
                    "name": "\u53e5\u6cd5\u5206\u6790"
                },
                {
                    "value": 11,
                    "name": "\u7f51\u7edc\u901a\u4fe1"
                },
                {
                    "value": 11,
                    "name": "\u673a\u5668\u4eba"
                },
                {
                    "value": 10,
                    "name": "python"
                },
                {
                    "value": 10,
                    "name": "Spark"
                },
                {
                    "value": 10,
                    "name": "RNN"
                },
                {
                    "value": 10,
                    "name": "\u7269\u6d41\u5e73\u53f0"
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
                    "value": 9,
                    "name": "\u6ef4\u6ef4"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 9,
                    "name": "\u793e\u4ea4"
                },
                {
                    "value": 9,
                    "name": "\u8bcd\u6027\u6807\u6ce8"
                },
                {
                    "value": 9,
                    "name": "\u4fe1\u606f\u68c0\u7d22"
                },
                {
                    "value": 9,
                    "name": "Caffe"
                },
                {
                    "value": 9,
                    "name": "\u77e5\u8bc6\u56fe\u8c31"
                },
                {
                    "value": 9,
                    "name": "\u4e2d\u6587\u5206\u8bcd"
                },
                {
                    "value": 9,
                    "name": "AI"
                },
                {
                    "value": 8,
                    "name": "\u91d1\u878d\u4e1a"
                },
                {
                    "value": 8,
                    "name": "Golang"
                },
                {
                    "value": 8,
                    "name": "\u533a\u5757\u94fe"
                },
                {
                    "value": 8,
                    "name": "\u7269\u6d41"
                },
                {
                    "value": 8,
                    "name": "MCN\uff5c\u76f4\u64ad\u5e73\u53f0"
                },
                {
                    "value": 8,
                    "name": "\u6c7d\u8f66"
                },
                {
                    "value": 8,
                    "name": "\u667a\u80fd\u5bb6\u5c45"
                },
                {
                    "value": 8,
                    "name": "\u5782\u76f4\u641c\u7d22"
                },
                {
                    "value": 8,
                    "name": "\u6570\u4ed3\u5efa\u6a21"
                },
                {
                    "value": 8,
                    "name": "tensorflow"
                },
                {
                    "value": 7,
                    "name": "\u56fe\u50cf\u5206\u5272"
                },
                {
                    "value": 7,
                    "name": "MySQL"
                },
                {
                    "value": 7,
                    "name": "\u7ba1\u7406\u89c4\u8303"
                },
                {
                    "value": 7,
                    "name": "\u5730\u56fe"
                },
                {
                    "value": 7,
                    "name": "\u667a\u80fd\u91d1\u878d"
                },
                {
                    "value": 7,
                    "name": "\u8fd0\u7b79\u4f18\u5316"
                },
                {
                    "value": 7,
                    "name": "\u89c6\u9891\u7b97\u6cd5"
                },
                {
                    "value": 7,
                    "name": "\u5b89\u5c45\u8ba1\u5212"
                },
                {
                    "value": 7,
                    "name": "\u4e92\u8054\u7f51"
                },
                {
                    "value": 7,
                    "name": "\u7528\u6237\u753b\u50cf"
                },
                {
                    "value": 7,
                    "name": "\u9910\u8865"
                },
                {
                    "value": 7,
                    "name": "\u5de5\u5177\u8f6f\u4ef6"
                },
                {
                    "value": 7,
                    "name": "\u798f\u5229\u4ea7\u5047"
                },
                {
                    "value": 6,
                    "name": "\u8bed\u97f3\u5904\u7406"
                },
                {
                    "value": 6,
                    "name": "\u94f6\u884c"
                },
                {
                    "value": 6,
                    "name": "\u76f4\u64ad"
                },
                {
                    "value": 6,
                    "name": "\u793e\u4ea4\u5a92\u4f53"
                },
                {
                    "value": 6,
                    "name": "\u6570\u636e\u5e93"
                },
                {
                    "value": 6,
                    "name": "opencv"
                },
                {
                    "value": 6,
                    "name": "\u5f3a\u5316\u5b66\u4e60"
                },
                {
                    "value": 6,
                    "name": "TensorFlow"
                },
                {
                    "value": 6,
                    "name": "Linux"
                },
                {
                    "value": 6,
                    "name": "\u901a\u8baf\u6d25\u8d34"
                },
                {
                    "value": 6,
                    "name": "Shell"
                },
                {
                    "value": 6,
                    "name": "spark"
                },
                {
                    "value": 6,
                    "name": "\u751f\u6d3b\u670d\u52a1"
                },
                {
                    "value": 5,
                    "name": "\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 5,
                    "name": "\u8bed\u97f3\u7b97\u6cd5"
                },
                {
                    "value": 5,
                    "name": "\u5206\u5e03\u5f0f\u641c\u7d22"
                },
                {
                    "value": 5,
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0"
                },
                {
                    "value": 5,
                    "name": "\u8fd0\u7b79\u5b66"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u89c6\u89c9"
                },
                {
                    "value": 5,
                    "name": "\u5236\u9020\u4e1a"
                },
                {
                    "value": 5,
                    "name": "\u56fe\u50cf\u8bc6\u522b"
                },
                {
                    "value": 5,
                    "name": "\u673a\u5668\u7ffb\u8bd1"
                },
                {
                    "value": 5,
                    "name": "\u529e\u516c\u903c\u683c\u9ad8"
                },
                {
                    "value": 5,
                    "name": "ARM"
                },
                {
                    "value": 5,
                    "name": "\u5b9a\u4f4d"
                },
                {
                    "value": 5,
                    "name": "\u671f\u6743\u4e30\u539a"
                },
                {
                    "value": 5,
                    "name": "\u5927\u725b\u56e2\u961f"
                },
                {
                    "value": 5,
                    "name": "\u4f20\u611f\u5668"
                },
                {
                    "value": 5,
                    "name": "\u5206\u7c7b\u4fe1\u606f"
                },
                {
                    "value": 5,
                    "name": "\u786c\u4ef6\u5236\u9020"
                },
                {
                    "value": 5,
                    "name": "\u70b9\u4e91"
                },
                {
                    "value": 5,
                    "name": "linux"
                },
                {
                    "value": 5,
                    "name": "Hive"
                },
                {
                    "value": 5,
                    "name": "\u667a\u6167\u57ce\u5e02"
                },
                {
                    "value": 4,
                    "name": "\u6570\u636e\u7ed3\u6784"
                },
                {
                    "value": 4,
                    "name": "\u5348\u9910\u8865\u52a9"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u56fe\u5f62"
                },
                {
                    "value": 4,
                    "name": "matlab"
                },
                {
                    "value": 4,
                    "name": "\u89c6\u9891"
                },
                {
                    "value": 4,
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 4,
                    "name": "c++"
                },
                {
                    "value": 4,
                    "name": "Tensorflow"
                },
                {
                    "value": 4,
                    "name": "\u6392\u5e8f"
                },
                {
                    "value": 4,
                    "name": "\u97f3\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 4,
                    "name": "slam"
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
                    "name": "\u5de5\u4e1a\u4e92\u8054\u7f51"
                },
                {
                    "value": 4,
                    "name": "nlp\u7b97\u6cd5\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 4,
                    "name": "\u7acb\u4f53\u89c6\u89c9"
                },
                {
                    "value": 4,
                    "name": "\u9ad8\u7ea7\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 4,
                    "name": "\u901a\u4fe1/\u7f51\u7edc\u8bbe\u5907"
                },
                {
                    "value": 4,
                    "name": "nlp"
                },
                {
                    "value": 4,
                    "name": "3D"
                },
                {
                    "value": 4,
                    "name": "\u533b\u7597\u5668\u68b0"
                },
                {
                    "value": 4,
                    "name": "CTR\u9884\u4f30"
                },
                {
                    "value": 4,
                    "name": "\u540e\u7aef"
                },
                {
                    "value": 4,
                    "name": "Flink"
                },
                {
                    "value": 4,
                    "name": "salm"
                },
                {
                    "value": 4,
                    "name": "HALCON"
                },
                {
                    "value": 4,
                    "name": "\u4e13\u4e1a\u670d\u52a1\uff5c\u54a8\u8be2"
                },
                {
                    "value": 4,
                    "name": "\u6559\u80b2\uff5c\u57f9\u8bad"
                },
                {
                    "value": 4,
                    "name": "\u5bfc\u822a"
                },
                {
                    "value": 3,
                    "name": "\u4e30\u539a\u5e74\u7ec8"
                },
                {
                    "value": 3,
                    "name": "CV"
                },
                {
                    "value": 3,
                    "name": "\u7528\u6237\u589e\u957f"
                },
                {
                    "value": 3,
                    "name": "\u5e74\u5ea6\u65c5\u6e38"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 3,
                    "name": "\u672c\u5206"
                },
                {
                    "value": 3,
                    "name": "ROS\u7cfb\u7edf"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u9891\u641c\u7d22"
                },
                {
                    "value": 3,
                    "name": "kaggle"
                },
                {
                    "value": 3,
                    "name": "\u6570\u636e\u4ed3\u5e93"
                },
                {
                    "value": 3,
                    "name": "SFM"
                },
                {
                    "value": 3,
                    "name": "3D\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "\u7b97\u6cd5\u8bbe\u8ba1"
                },
                {
                    "value": 3,
                    "name": "\u5d4c\u5165\u5f0f"
                },
                {
                    "value": 3,
                    "name": "\u7f8e\u5973\u591a"
                },
                {
                    "value": 3,
                    "name": "\u5c45\u4f4f\u670d\u52a1"
                },
                {
                    "value": 3,
                    "name": "opengl"
                },
                {
                    "value": 3,
                    "name": "OpenGL"
                },
                {
                    "value": 3,
                    "name": "\u8fd0\u7b79"
                },
                {
                    "value": 3,
                    "name": "OCR"
                },
                {
                    "value": 3,
                    "name": "\u6587\u5316\u4f20\u5a92"
                },
                {
                    "value": 3,
                    "name": "\u7279\u5f81\u5de5\u7a0b"
                },
                {
                    "value": 3,
                    "name": "\u6d41\u5a92\u4f53"
                },
                {
                    "value": 3,
                    "name": "\u795e\u7ecf\u7f51\u7edc"
                },
                {
                    "value": 3,
                    "name": "\u8fea\u58eb\u5c3c"
                },
                {
                    "value": 3,
                    "name": "\u65e0\u4eba\u8f66"
                },
                {
                    "value": 3,
                    "name": "\u7cfb\u7edf\u67b6\u6784"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u7ef4\u91cd\u5efa"
                },
                {
                    "value": 3,
                    "name": "\u8ffd\u6c42\u6781\u81f4"
                },
                {
                    "value": 3,
                    "name": "\u89c6\u89c9"
                },
                {
                    "value": 3,
                    "name": "MXNet"
                },
                {
                    "value": 3,
                    "name": "DSP"
                },
                {
                    "value": 3,
                    "name": "C#"
                },
                {
                    "value": 3,
                    "name": "ETA"
                },
                {
                    "value": 3,
                    "name": "\u626b\u5730\u673a\u5668\u4eba"
                },
                {
                    "value": 3,
                    "name": "\u7b97\u6cd5\u4f18\u5316"
                },
                {
                    "value": 3,
                    "name": "pytorch"
                },
                {
                    "value": 3,
                    "name": "\u8f6f\u4ef6\u5f00\u53d1"
                },
                {
                    "value": 3,
                    "name": "\u5de5\u4e1a\u81ea\u52a8\u5316"
                },
                {
                    "value": 3,
                    "name": "GAN"
                },
                {
                    "value": 2,
                    "name": "\u7b97\u6cd5\u7814\u7a76"
                },
                {
                    "value": 2,
                    "name": "\u4f4f\u798f\u8ba1\u5212"
                },
                {
                    "value": 2,
                    "name": "\u97f3\u4e50"
                },
                {
                    "value": 2,
                    "name": "\u5de5\u4e1a\u68c0\u6d4b"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u7ef4\u56fe\u5f62"
                },
                {
                    "value": 2,
                    "name": "go"
                },
                {
                    "value": 2,
                    "name": "\u611f\u77e5\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "ETL"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee"
                },
                {
                    "value": 2,
                    "name": "\u4e03\u9669\u4e00\u91d1"
                },
                {
                    "value": 2,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u534f\u540c\u8fc7\u6ee4"
                },
                {
                    "value": 2,
                    "name": "GPU"
                },
                {
                    "value": 2,
                    "name": "\u7ade\u54c1\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u4ea7\u54c1\u7b56\u5212"
                },
                {
                    "value": 2,
                    "name": "\u67b6\u6784\u5e08"
                },
                {
                    "value": 2,
                    "name": "\u98ce\u63a7"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7406\u89e3"
                },
                {
                    "value": 2,
                    "name": "\u4ea7\u54c1\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5e93\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u5efa\u6a21"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u8425\u9500"
                },
                {
                    "value": 2,
                    "name": "\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 2,
                    "name": "\u5e74\u7ec8\u5206\u7ea2"
                },
                {
                    "value": 2,
                    "name": "RTK"
                },
                {
                    "value": 2,
                    "name": "\u65e0\u4eba\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "\u641c\u7d22\u5f15\u64ce"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u4f53\u5339\u914d"
                },
                {
                    "value": 2,
                    "name": "\u805a\u7c7b"
                },
                {
                    "value": 2,
                    "name": "SNN"
                },
                {
                    "value": 2,
                    "name": "\u623f\u5730\u4ea7\uff5c\u5efa\u7b51\uff5c\u7269\u4e1a"
                },
                {
                    "value": 2,
                    "name": "\u70b9\u4e91\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "Pytorch"
                },
                {
                    "value": 2,
                    "name": "\u56fe\u50cf\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "\u9700\u6c42\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u59ff\u6001\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "AI\u533b\u7597"
                },
                {
                    "value": 2,
                    "name": "\u6570\u636e\u6293\u53d6"
                },
                {
                    "value": 2,
                    "name": "\u6280\u672f\u7ba1\u7406"
                },
                {
                    "value": 2,
                    "name": "\u81ea\u52a8\u6458\u8981"
                },
                {
                    "value": 2,
                    "name": "Go"
                },
                {
                    "value": 2,
                    "name": "\u6559\u80b2\u8f85\u5bfc"
                },
                {
                    "value": 2,
                    "name": "\u539f\u578b\u8bbe\u8ba1"
                },
                {
                    "value": 2,
                    "name": "docker"
                },
                {
                    "value": 2,
                    "name": "JAVA"
                },
                {
                    "value": 2,
                    "name": "\u8054\u90a6\u5b66\u4e60"
                },
                {
                    "value": 2,
                    "name": "\u53cc\u76ee\u89c6\u89c9"
                },
                {
                    "value": 2,
                    "name": "\u6279\u53d1\uff5c\u96f6\u552e"
                },
                {
                    "value": 2,
                    "name": "\u793e\u4ea4\u5a92\u4f53\u5e73\u53f0"
                },
                {
                    "value": 2,
                    "name": "Matlab"
                },
                {
                    "value": 2,
                    "name": "\u5206\u7c7b"
                },
                {
                    "value": 2,
                    "name": "LTE"
                },
                {
                    "value": 2,
                    "name": "PaddlePddle"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u878d\u79d1\u6280"
                },
                {
                    "value": 2,
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe"
                },
                {
                    "value": 2,
                    "name": "GIS"
                },
                {
                    "value": 2,
                    "name": "GBDT"
                },
                {
                    "value": 2,
                    "name": "JavaScript"
                },
                {
                    "value": 2,
                    "name": "\u672c\u5730\u751f\u6d3b"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u878d\u98ce\u63a7"
                },
                {
                    "value": 2,
                    "name": "\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 2,
                    "name": "\u6570\u4ed3\u67b6\u6784"
                },
                {
                    "value": 2,
                    "name": "\u80fd\u6e90\uff5c\u77ff\u4ea7\uff5c\u73af\u4fdd"
                },
                {
                    "value": 2,
                    "name": "\u7248\u9762\u5206\u6790"
                },
                {
                    "value": 2,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u5b66"
                },
                {
                    "value": 2,
                    "name": "HADOOP"
                },
                {
                    "value": 2,
                    "name": "\u7f16\u7a0b"
                },
                {
                    "value": 2,
                    "name": "\u964d\u566a"
                },
                {
                    "value": 2,
                    "name": "\u6e38\u620fAI\u7814\u53d1"
                },
                {
                    "value": 2,
                    "name": "\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5e02\u516c\u53f8"
                },
                {
                    "value": 2,
                    "name": "\u52a8\u6001\u89c4\u5212"
                },
                {
                    "value": 2,
                    "name": "AR"
                },
                {
                    "value": 2,
                    "name": "\u667a\u80fd\u9a7e\u9a76"
                },
                {
                    "value": 2,
                    "name": "ACM"
                },
                {
                    "value": 2,
                    "name": "\u6570\u5b57\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "\u7528\u6237\u5339\u914d\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u56de\u58f0\u6d88\u9664"
                },
                {
                    "value": 2,
                    "name": "\u8111\u673a"
                },
                {
                    "value": 2,
                    "name": "\u9886\u519b\u4f01\u4e1a"
                },
                {
                    "value": 2,
                    "name": "\u5f71\u89c6\uff5c\u52a8\u6f2b"
                },
                {
                    "value": 2,
                    "name": "\u5168\u7403\u5316"
                },
                {
                    "value": 2,
                    "name": "\u7b56\u7565\u7b97\u6cd5"
                },
                {
                    "value": 2,
                    "name": "\u7c7b\u8111\u8ba1\u7b97"
                },
                {
                    "value": 2,
                    "name": "\u53ec\u56de"
                },
                {
                    "value": 2,
                    "name": "\u89c6\u89c9slam"
                },
                {
                    "value": 2,
                    "name": "\u5e05\u54e5\u591a"
                },
                {
                    "value": 2,
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3"
                },
                {
                    "value": 2,
                    "name": "\u533b\u5b66\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 2,
                    "name": "CAD"
                },
                {
                    "value": 2,
                    "name": "\u4eff\u771f"
                },
                {
                    "value": 2,
                    "name": "\u6d4b\u8bd5\u5f00\u53d1"
                },
                {
                    "value": 2,
                    "name": "OpenCL"
                },
                {
                    "value": 2,
                    "name": "\u96f6\u77e5\u8bc6\u8bc1\u660e"
                },
                {
                    "value": 1,
                    "name": "AGV"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "3D\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "c"
                },
                {
                    "value": 1,
                    "name": "3D\u59ff\u6001\u91cd\u5efa"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u7a0b\u80fd\u529b"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u7f51\u683c/\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1"
                },
                {
                    "value": 1,
                    "name": "\u6574\u6570\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u4e3b\u664b\u5347\u8ba1\u5212"
                },
                {
                    "value": 1,
                    "name": "\u5149\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u7279\u6548"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6570\u636e\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u65b9\u5411\u7b97\u6cd5\u5de5"
                },
                {
                    "value": 1,
                    "name": "FPGA"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u843d\u5730"
                },
                {
                    "value": 1,
                    "name": "\u5185\u5bb9\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u66fe\u5f3a"
                },
                {
                    "value": 1,
                    "name": "labview"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u611f\u77e5\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "hbase"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u4eff\u771f\u4eba"
                },
                {
                    "value": 1,
                    "name": "CGAL"
                },
                {
                    "value": 1,
                    "name": "\u8f6c\u5316\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u5b66\u8005\u660e\u661f\u6d3b\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u692d\u5706\u66f2\u7ebf"
                },
                {
                    "value": 1,
                    "name": "\u9057\u4f20\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Sox"
                },
                {
                    "value": 1,
                    "name": "Oracle"
                },
                {
                    "value": 1,
                    "name": "AlphaGo"
                },
                {
                    "value": 1,
                    "name": "ensorFlow"
                },
                {
                    "value": 1,
                    "name": "\u7edf\u8ba1\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "\u914d\u9001\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u8bbe\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4f3a\u670d"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u5149\u7ea4\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u82f1\u98de\u51cc"
                },
                {
                    "value": 1,
                    "name": "\u4e70\u624b\u6218\u7565"
                },
                {
                    "value": 1,
                    "name": "ranking"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u4e91\u5206\u5272\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "neon"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5e26\u5bbd\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u80a2\u4f53\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u5173\u952e\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "h264\uff0ch265\uff0cav1"
                },
                {
                    "value": 1,
                    "name": "\u5b8c\u6210E\u8f6e\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "numpy"
                },
                {
                    "value": 1,
                    "name": "\u9aa8\u79d1\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "C++/python"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u5176\u4ed6"
                },
                {
                    "value": 1,
                    "name": "\u836f\u7269\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u5668\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u5149"
                },
                {
                    "value": 1,
                    "name": "\u5730\u7406\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u9ed1\u76d2\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u5341\u70b9\u5f00\u5de5"
                },
                {
                    "value": 1,
                    "name": "H.264/265"
                },
                {
                    "value": 1,
                    "name": "rpc"
                },
                {
                    "value": 1,
                    "name": "\u53cd\u6d17\u94b1\u53cd\u4f5c\u5f0a"
                },
                {
                    "value": 1,
                    "name": "\u9a6c\u5c14\u514b\u592b\u968f\u673a\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u59ff\u6001\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "NRI"
                },
                {
                    "value": 1,
                    "name": "\u5efa\u7b51\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5206\u7c7b\uff0c"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u5b66"
                },
                {
                    "value": 1,
                    "name": "AILab"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5feb\u901f\u6210\u957f"
                },
                {
                    "value": 1,
                    "name": "\u753b\u50cf\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "ORBSLAM"
                },
                {
                    "value": 1,
                    "name": "webGL"
                },
                {
                    "value": 1,
                    "name": "B2B"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u52a8\u529b\u5b66\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u9000\u706b\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u8054\u7f51"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u5b66"
                },
                {
                    "value": 1,
                    "name": "/Pytorch"
                },
                {
                    "value": 1,
                    "name": "DSP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u7cbe\u5ea6\u5730\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u8f6c\u6362"
                },
                {
                    "value": 1,
                    "name": "ECC"
                },
                {
                    "value": 1,
                    "name": "GPS"
                },
                {
                    "value": 1,
                    "name": "ESMM"
                },
                {
                    "value": 1,
                    "name": "PUSH\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "Cortex-M\u6838"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "flv\uff0cmp3\uff0cmp4"
                },
                {
                    "value": 1,
                    "name": "\u573a\u666f\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "NLP/CV"
                },
                {
                    "value": 1,
                    "name": "\u8fd1\u7ea2\u5916"
                },
                {
                    "value": 1,
                    "name": "\u4e34\u5e8a\u79d1\u7814"
                },
                {
                    "value": 1,
                    "name": "\u4eea\u5668\u4eea\u8868"
                },
                {
                    "value": 1,
                    "name": "h264"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u536b\u661f\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u7136\u8bed\u8a00"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u62df\u5668"
                },
                {
                    "value": 1,
                    "name": "\u6df1\u5ea6\u4f30\u8ba1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u8d85\u957f\u5e26\u85aa\u5047\u671f"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u60ef\u6027\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "hadoop"
                },
                {
                    "value": 1,
                    "name": "\u6027\u80fd\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u7269\u4f53\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "LiDAR"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "SVC"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u9884\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u9891\u8c31\u76d1\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u901f\u5ea6\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "AI\u56fe\u50cf\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "MIMO\u96f7\u8fbe"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u5168\u5458\u51fa\u56fd\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u7ecf\u5178\u63a7\u5236\u7406\u8bba"
                },
                {
                    "value": 1,
                    "name": "\u6c42\u89e3\u5668"
                },
                {
                    "value": 1,
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336"
                },
                {
                    "value": 1,
                    "name": "\u62a0\u56fe"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u89c4\u5219\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u516c\u94a5"
                },
                {
                    "value": 1,
                    "name": "\u7cfb\u7edf\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u7f8e\u989c\u7f8e\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u878d\u5408\u611f\u77e5"
                },
                {
                    "value": 1,
                    "name": "DICOM"
                },
                {
                    "value": 1,
                    "name": "\u8499\u7279\u5361\u6d1b"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "shell"
                },
                {
                    "value": 1,
                    "name": "SaaS"
                },
                {
                    "value": 1,
                    "name": "SQLServer"
                },
                {
                    "value": 1,
                    "name": "3d\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u884c\u4e1a"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u57fa\u7840"
                },
                {
                    "value": 1,
                    "name": "python/go"
                },
                {
                    "value": 1,
                    "name": "query"
                },
                {
                    "value": 1,
                    "name": "ADAS"
                },
                {
                    "value": 1,
                    "name": "webgl"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5377\u79ef"
                },
                {
                    "value": 1,
                    "name": "\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u5fae\u670d\u52a1"
                },
                {
                    "value": 1,
                    "name": "\u5d4c\u5165\u5f0f\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Tensorfl"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "FPGA\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u7a7f\u6234"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u4ea7\u54c1\u7ecf\u9a8c"
                },
                {
                    "value": 1,
                    "name": "x265"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316"
                },
                {
                    "value": 1,
                    "name": "\u5173\u7cfb\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u5956\u91d1"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u5927\u725b\u516c\u53f8"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u5de5\u667a\u80fd\u673a\u5668\u4eba"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "android"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7b79\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5956\u91d1\u591a\u591a\u591a"
                },
                {
                    "value": 1,
                    "name": "libvpx"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "AB\u5206\u6d41"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "O2O"
                },
                {
                    "value": 1,
                    "name": "KF/EKF"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u4eff\u771f"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408IMU"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "pytroch"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u79fb\u690d\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u62e8"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "ISP"
                },
                {
                    "value": 1,
                    "name": "jaya"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u8c03\u7814"
                },
                {
                    "value": 1,
                    "name": "\u751f\u4ea7\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u63d0\u53d6"
                },
                {
                    "value": 1,
                    "name": "AEC"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u6cca\u8f66"
                },
                {
                    "value": 1,
                    "name": "3dmm"
                },
                {
                    "value": 1,
                    "name": "VTK"
                },
                {
                    "value": 1,
                    "name": "CRNN"
                },
                {
                    "value": 1,
                    "name": "\u6c34\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "VINS"
                },
                {
                    "value": 1,
                    "name": "\u70b9\u51fb\u7387\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "automak"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "NR"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08"
                },
                {
                    "value": 1,
                    "name": "\u6216"
                },
                {
                    "value": 1,
                    "name": "\u4ea4\u901a\u8fd0\u8f93"
                },
                {
                    "value": 1,
                    "name": "\u70df\u96fe\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u51b3\u7b56\u6811"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a9\u4e09\u9910"
                },
                {
                    "value": 1,
                    "name": "NLP\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "PPP"
                },
                {
                    "value": 1,
                    "name": "\u78c1\u529b\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u53d1"
                },
                {
                    "value": 1,
                    "name": "Windows"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u5168\u94fe\u8defSaaS\u5e73\u53f0"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4e09\u7ef4"
                },
                {
                    "value": 1,
                    "name": "dl4j"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u4eba\u667a\u80fd"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u5177\u793e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "rank"
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
                    "name": "\u6ee4\u955c"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u641c\u7d22"
                },
                {
                    "value": 1,
                    "name": "\u591c\u62cd"
                },
                {
                    "value": 1,
                    "name": "AIOPS"
                },
                {
                    "value": 1,
                    "name": "vr\u3002ar"
                },
                {
                    "value": 1,
                    "name": "\u9a71\u52a8\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "ERP"
                },
                {
                    "value": 1,
                    "name": "\u5348\u9910\u4ea4\u901a\u8865\u52a9"
                },
                {
                    "value": 1,
                    "name": "PHM"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u8f7b\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u4e66\u89c6\u89c9"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u5316\u6d4b\u8bd5"
                },
                {
                    "value": 1,
                    "name": "\u8272\u8c31\u5149\u8c31"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u6d3b\u8dc3\u5ea6"
                },
                {
                    "value": 1,
                    "name": "JitterBuffer"
                },
                {
                    "value": 1,
                    "name": "rgbd"
                },
                {
                    "value": 1,
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350"
                },
                {
                    "value": 1,
                    "name": "pandas"
                },
                {
                    "value": 1,
                    "name": "\u68c0\u6d4b\u3001\u8bc6\u522b\u3001\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5546\u54c1\u6a21\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6846\u67b6\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "IMU"
                },
                {
                    "value": 1,
                    "name": "\u5305\u5348\u9910\u665a\u9910"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "\u73af\u5883\u611f\u77e5\u4e0e\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "\u6295\u8d44/\u878d\u8d44"
                },
                {
                    "value": 1,
                    "name": "5G"
                },
                {
                    "value": 1,
                    "name": "C\\C++\u8bed\u8a00\u5d4c\u5165"
                },
                {
                    "value": 1,
                    "name": "\u5468\u672b\u53cc\u4f11"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4f53\u80b2"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u533b\u7597\u4fe1\u606f\u5316"
                },
                {
                    "value": 1,
                    "name": "\u773c\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u77e9\u9635\u5206\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u725b\u4eba\u5206\u4eab"
                },
                {
                    "value": 1,
                    "name": "VIO"
                },
                {
                    "value": 1,
                    "name": "\u9ea6\u514b\u98ce\u9635\u5217"
                },
                {
                    "value": 1,
                    "name": "\u57fa\u7840\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u6570\u636e\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5e03\u5f0f"
                },
                {
                    "value": 1,
                    "name": "AGC"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u8d37\u98ce\u63a7"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5ba2\u670d"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u4f5c\u6355\u6349"
                },
                {
                    "value": 1,
                    "name": "\u519c\u6797\u7267\u6e14"
                },
                {
                    "value": 1,
                    "name": "\u53ef\u89c6\u5316"
                },
                {
                    "value": 1,
                    "name": "\u98de\u884c\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "filnk"
                },
                {
                    "value": 1,
                    "name": "\u77e5\u8bc6\u5e93"
                },
                {
                    "value": 1,
                    "name": "VO/VIO"
                },
                {
                    "value": 1,
                    "name": "\u8d44\u8baf"
                },
                {
                    "value": 1,
                    "name": "isp"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u8fd0\u52a8"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u7ec8\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "pil"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u8c03\u5ea6"
                },
                {
                    "value": 1,
                    "name": "Node.js"
                },
                {
                    "value": 1,
                    "name": "\u907f\u969c"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "POI"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "WIFI"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u7ef4"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9"
                },
                {
                    "value": 1,
                    "name": "\u591a\u65b9\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "NPL"
                },
                {
                    "value": 1,
                    "name": "\u533b\u5b66\u5f71\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u8c31"
                },
                {
                    "value": 1,
                    "name": "ElasticSearch"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168"
                },
                {
                    "value": 1,
                    "name": "\u9009\u578b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u67b6\u6784"
                },
                {
                    "value": 1,
                    "name": "\u540e\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "\u7535\u63a7"
                },
                {
                    "value": 1,
                    "name": "Tensor"
                },
                {
                    "value": 1,
                    "name": "SLAM\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "AI\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "HBase"
                },
                {
                    "value": 1,
                    "name": "\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "R"
                },
                {
                    "value": 1,
                    "name": "\u542f\u53d1\u5f0f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "Fliter"
                },
                {
                    "value": 1,
                    "name": "nlp\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u6392\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u524d\u65b9\u4ea4\u4f1a"
                },
                {
                    "value": 1,
                    "name": "flow"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u7f51\u7edc\u4f20\u8f93\u534f\u8bae"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u5355\u76ee"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u4ef7"
                },
                {
                    "value": 1,
                    "name": "\u624b\u52bf\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "UWB"
                },
                {
                    "value": 1,
                    "name": "\u9ad8\u5e76\u53d1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u8bbe\u8ba1"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u822a\u5929"
                },
                {
                    "value": 1,
                    "name": "\u6d4b\u7ed8"
                },
                {
                    "value": 1,
                    "name": "\u8bad\u7ec3\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f\u56fe\u50cf"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5168\u5927\u6570\u636e"
                },
                {
                    "value": 1,
                    "name": "FLINK"
                },
                {
                    "value": 1,
                    "name": "\u52aa\u529b\u53d8\u5927\u725b"
                },
                {
                    "value": 1,
                    "name": "\u8282\u65e5\u798f\u5229"
                },
                {
                    "value": 1,
                    "name": "\u652f\u4ed8\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "torch"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u606f\u4e2d\u95f4\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u524d\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a/\u6570\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u52a8\u529b\u5b66\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u7ebf\u4fe1\u53f7\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "Rust"
                },
                {
                    "value": 1,
                    "name": "openGL"
                },
                {
                    "value": 1,
                    "name": "react"
                },
                {
                    "value": 1,
                    "name": "\u5b9e\u65f6\u8def\u51b5"
                },
                {
                    "value": 1,
                    "name": "\u4f20\u611f\u5668\u6216\u70b9\u4e91"
                },
                {
                    "value": 1,
                    "name": "\u51fa\u56fd\u65c5\u6e38"
                },
                {
                    "value": 1,
                    "name": "\u6807\u5b9a\u7f16\u7801"
                },
                {
                    "value": 1,
                    "name": "\u878d\u5408"
                },
                {
                    "value": 1,
                    "name": "PID\u3001\u6700\u4f18\u3001\u81ea\u9002"
                },
                {
                    "value": 1,
                    "name": "\u667a\u80fd\u5b89\u9632"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544aCTR/CVR"
                },
                {
                    "value": 1,
                    "name": "\u5927\u5730\u6d4b\u91cf"
                },
                {
                    "value": 1,
                    "name": "DNN"
                },
                {
                    "value": 1,
                    "name": "\u65e5\u7167\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4f11\u95f2\uff5c\u5a31\u4e50"
                },
                {
                    "value": 1,
                    "name": "MCU"
                },
                {
                    "value": 1,
                    "name": "\u96c6\u6210\u7535\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u8f6f\u4ef6"
                },
                {
                    "value": 1,
                    "name": "\u8ba1\u7b97\u673a\u56fe\u50cf\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u7279\u5f81\u6316\u6398"
                },
                {
                    "value": 1,
                    "name": "C/C++/Python"
                },
                {
                    "value": 1,
                    "name": "CTR"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5f62\u56fe\u50cf\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "\u6e32\u67d3"
                },
                {
                    "value": 1,
                    "name": "\u8def\u5f84\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u8fde\u7eed\u521b\u4e1a\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u80fd\u6e90"
                },
                {
                    "value": 1,
                    "name": "\u4e50\u5668"
                },
                {
                    "value": 1,
                    "name": "\u4fe1\u53f7\u91c7\u96c6"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u63a8\u8350\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u97f3\u89c6\u9891\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "TF"
                },
                {
                    "value": 1,
                    "name": "\u5927\u6570\u636e\u5904\u7406\u6280\u672f"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u5e7f\u544a"
                },
                {
                    "value": 1,
                    "name": "\u51e0\u4f55\u56fe\u5f62"
                },
                {
                    "value": 1,
                    "name": "cmake"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u5916\u5e02\u573a"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u529b\u8d44\u6e90\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u9002\u5e94"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u7801\u5b66"
                },
                {
                    "value": 1,
                    "name": "\u8fb9\u7f18\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "\u84dd\u7259"
                },
                {
                    "value": 1,
                    "name": "\u4e8c\u5206\u7c7b"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u65b9\u7f8e\u5b66\u57f9\u8bad"
                },
                {
                    "value": 1,
                    "name": "kalman"
                },
                {
                    "value": 1,
                    "name": "Lucene"
                },
                {
                    "value": 1,
                    "name": "XGB"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u98ce\u63a7AI"
                },
                {
                    "value": 1,
                    "name": "Caffe\u3001Pytorch\u3001"
                },
                {
                    "value": 1,
                    "name": "\u9879\u76ee\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1"
                },
                {
                    "value": 1,
                    "name": "LIDAR"
                },
                {
                    "value": 1,
                    "name": "\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u4e49\u7406\u89e3"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b57\u97f3\u9891\u6c34\u5370"
                },
                {
                    "value": 1,
                    "name": "NLP\u5904\u7406"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u5238\u5546"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u5f15\u64ce"
                },
                {
                    "value": 1,
                    "name": "\u76ee\u6807\u5206\u5272"
                },
                {
                    "value": 1,
                    "name": "CAD\u56fe\u7eb8\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u79df\u623f\u8865\u8d34"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "CCF"
                },
                {
                    "value": 1,
                    "name": "\u914d\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u7269\u7406\u5c42"
                },
                {
                    "value": 1,
                    "name": "\u3001Spark"
                },
                {
                    "value": 1,
                    "name": "java"
                },
                {
                    "value": 1,
                    "name": "Avatar"
                },
                {
                    "value": 1,
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5\u673a"
                },
                {
                    "value": 1,
                    "name": "HIve"
                },
                {
                    "value": 1,
                    "name": "\u6280\u672f\u5927\u725b\u591a"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u544a\u53ec\u56de"
                },
                {
                    "value": 1,
                    "name": "\u641c\u7d22\u6392\u5e8f"
                },
                {
                    "value": 1,
                    "name": "BFM"
                },
                {
                    "value": 1,
                    "name": "\u6d88\u8d39\u91d1\u878d"
                },
                {
                    "value": 1,
                    "name": "3DGIS"
                },
                {
                    "value": 1,
                    "name": "PCL"
                },
                {
                    "value": 1,
                    "name": "vivado"
                },
                {
                    "value": 1,
                    "name": "ACC/AEB/LKA"
                },
                {
                    "value": 1,
                    "name": "HQRank"
                },
                {
                    "value": 1,
                    "name": "OpenMesh"
                },
                {
                    "value": 1,
                    "name": "\u901a\u4fe1\u539f\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5bc6\u94a5\u7cfb\u7edf"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5bfc\u822a"
                },
                {
                    "value": 1,
                    "name": "\u65f6\u5e8f\u6570\u636e\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u548c\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u4f18\u5316\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u9065\u611f"
                },
                {
                    "value": 1,
                    "name": "\u98ce\u63a7\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u6587\u672c\u68c0\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u79bb\u6563\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "\u7528\u6237\u7814\u7a76"
                },
                {
                    "value": 1,
                    "name": "\u671f\u6743\u6fc0\u52b1"
                },
                {
                    "value": 1,
                    "name": "MDP"
                },
                {
                    "value": 1,
                    "name": "\u6709\u821e\u53f0\u7ed9\u60a8\u8df3"
                },
                {
                    "value": 1,
                    "name": "\u5730\u56fe\u7f51\u7edc\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "\u7535\u5546\u5e7f\u544a\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u5de5\u4e1a\u9886\u57df"
                },
                {
                    "value": 1,
                    "name": "\u6570\u636e\u8fd0\u8425"
                },
                {
                    "value": 1,
                    "name": "\u8f68\u8ff9\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "3DCAD"
                },
                {
                    "value": 1,
                    "name": "\u6fc0\u60c5\u7684\u56e2\u961f"
                },
                {
                    "value": 1,
                    "name": "cuda"
                },
                {
                    "value": 1,
                    "name": "\u786c\u4ef6\u52a0\u901f"
                },
                {
                    "value": 1,
                    "name": "/"
                },
                {
                    "value": 1,
                    "name": "\u6a21\u578b\u538b\u7f29"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u7814\u7a76\u4e0e\u5efa\u6a21"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u4f18\u5316"
                },
                {
                    "value": 1,
                    "name": "RNN\u65f6\u95f4\u5e8f\u5217"
                },
                {
                    "value": 1,
                    "name": "Javascript"
                },
                {
                    "value": 1,
                    "name": "\u5e93\u5b58\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u4fdd\u9669"
                },
                {
                    "value": 1,
                    "name": "AI\u8d85\u7b97"
                },
                {
                    "value": 1,
                    "name": "3D\u89c6\u89c9\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "GNSS\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51\u51fa\u884c"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u76ee/\u53cc\u6444"
                },
                {
                    "value": 1,
                    "name": "SOA"
                },
                {
                    "value": 1,
                    "name": "\u79fb\u52a8\u7aef\u90e8\u7f72"
                },
                {
                    "value": 1,
                    "name": "hive"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5a92\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5e74\u5e95\u591a\u85aa"
                },
                {
                    "value": 1,
                    "name": "Pthon"
                },
                {
                    "value": 1,
                    "name": "\u5e8f\u5217\u9884\u6d4b"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u6587\u5206\u6790"
                },
                {
                    "value": 1,
                    "name": "\u7ed3\u6784\u5149"
                },
                {
                    "value": 1,
                    "name": "\u91cf\u5316"
                },
                {
                    "value": 1,
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u8138\u751f\u6210"
                },
                {
                    "value": 1,
                    "name": "\u6392\u5e8f\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u58f0\u7eb9\u8bc6\u522b"
                },
                {
                    "value": 1,
                    "name": "caffe"
                },
                {
                    "value": 1,
                    "name": "\u591a\u4f20\u611f\u5668"
                },
                {
                    "value": 1,
                    "name": "\u5f02\u5e38\u8bca\u65ad"
                },
                {
                    "value": 1,
                    "name": "\u89c6\u9891\u7f16\u8f91"
                },
                {
                    "value": 1,
                    "name": "\u8fd0\u52a8\u63a7\u5236"
                },
                {
                    "value": 1,
                    "name": "\u63a7\u5236\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08\u7b97\u6cd5"
                },
                {
                    "value": 1,
                    "name": "\u6821\u51c6"
                },
                {
                    "value": 1,
                    "name": "\u5bfc\u822a\u89c4\u5212"
                },
                {
                    "value": 1,
                    "name": "DSP\u7f16\u7a0b"
                },
                {
                    "value": 1,
                    "name": "\u6570\u5b66\u5e93"
                },
                {
                    "value": 1,
                    "name": "\u5361\u5c14\u66fc\u6ee4\u6ce2"
                },
                {
                    "value": 1,
                    "name": "\u8425\u9500\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "VR"
                },
                {
                    "value": 1,
                    "name": "\u53ec\u56de\u7b56\u7565"
                },
                {
                    "value": 1,
                    "name": "\u865a\u62df\u667a\u80fd\u76f4\u64ad"
                },
                {
                    "value": 1,
                    "name": "\u65e0\u76d1\u7763\u5b66\u4e60"
                },
                {
                    "value": 1,
                    "name": "BIM+3D"
                },
                {
                    "value": 1,
                    "name": "\u8def\u51b5\u8ba1\u7b97"
                },
                {
                    "value": 1,
                    "name": "X264"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u961f\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u5373\u65f6\u901a\u8baf"
                },
                {
                    "value": 1,
                    "name": "\u521b\u4e1a"
                },
                {
                    "value": 1,
                    "name": "GO"
                },
                {
                    "value": 1,
                    "name": "\u4e92\u8054\u7f51+"
                },
                {
                    "value": 1,
                    "name": "\u5ba4\u5185\u5b9a\u4f4d"
                },
                {
                    "value": 1,
                    "name": "\u90e8\u95e8\u7ba1\u7406"
                },
                {
                    "value": 1,
                    "name": "\u56fe\u50cf/\u89c6\u9891\u7684\u5206"
                },
                {
                    "value": 1,
                    "name": "\u7cbe\u51c6\u8425\u9500"
                },
                {
                    "value": 1,
                    "name": "vSLAM"
                },
                {
                    "value": 1,
                    "name": "\u8bed\u97f3\u6d4b\u8bc4"
                },
                {
                    "value": 1,
                    "name": "\u4f17\u7b79\u4e1a\u52a1"
                },
                {
                    "value": 1,
                    "name": "3D\u6253\u5370"
                },
                {
                    "value": 1,
                    "name": "PSENET"
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
        chart_0db972f0daac45b89acf4e78aa794069.setOption(option_0db972f0daac45b89acf4e78aa794069);
    </script>
                <div id="e4df0af1556b4b64b7712484143f6392" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_e4df0af1556b4b64b7712484143f6392 = echarts.init(
            document.getElementById('e4df0af1556b4b64b7712484143f6392'), 'white', {renderer: 'canvas'});
        var option_e4df0af1556b4b64b7712484143f6392 = {
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
                1405,
                651,
                133,
                105,
                53,
                23,
                17,
                11
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
                    "value": 1405
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 651
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 133
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 105
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 53
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 23
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 17
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 11
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
                    "value": 1405
                },
                {
                    "name": "\u7855\u58eb",
                    "value": 651
                },
                {
                    "name": "\u5e94\u5c4a / \u672c\u79d1",
                    "value": 133
                },
                {
                    "name": "\u5e94\u5c4a / \u7855\u58eb",
                    "value": 105
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 53
                },
                {
                    "name": "\u535a\u58eb",
                    "value": 23
                },
                {
                    "name": "\u5e94\u5c4a / \u4e0d\u9650",
                    "value": 17
                },
                {
                    "name": "\u5927\u4e13",
                    "value": 11
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
        chart_e4df0af1556b4b64b7712484143f6392.setOption(option_e4df0af1556b4b64b7712484143f6392);
    </script>
                <div id="3b8363dbd241419bbfa34731338922eb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_3b8363dbd241419bbfa34731338922eb = echarts.init(
            document.getElementById('3b8363dbd241419bbfa34731338922eb'), 'white', {renderer: 'canvas'});
        var option_3b8363dbd241419bbfa34731338922eb = {
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
                949,
                493,
                404,
                279,
                261,
                12,
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
                    "value": 949
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 493
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 404
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 279
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 261
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 12
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
                    "value": 949
                },
                {
                    "name": "\u7ecf\u9a8c1-3\u5e74",
                    "value": 493
                },
                {
                    "name": "\u7ecf\u9a8c\u4e0d\u9650",
                    "value": 404
                },
                {
                    "name": "\u7ecf\u9a8c5-10\u5e74",
                    "value": 279
                },
                {
                    "name": "\u7ecf\u9a8c\u5728\u6821",
                    "value": 261
                },
                {
                    "name": "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                    "value": 12
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
        chart_3b8363dbd241419bbfa34731338922eb.setOption(option_3b8363dbd241419bbfa34731338922eb);
    </script>
                <div id="39e4e09c36544f2591ef3d7c9f0c178b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_39e4e09c36544f2591ef3d7c9f0c178b = echarts.init(
            document.getElementById('39e4e09c36544f2591ef3d7c9f0c178b'), 'white', {renderer: 'canvas'});
            
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
    
        var option_39e4e09c36544f2591ef3d7c9f0c178b = {
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
                            "color": "rgb(84,46,62)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u95ee\u7b54",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,44,21)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u52a9\u7406",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,104,140)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5ba2\u670d",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,140,124)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,86,109)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u63a8\u7406",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,141,74)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u6e05\u6d17",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,50,136)"
                        }
                    }
                },
                {
                    "name": "\u60c5\u611f\u5206\u6790",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,100,94)"
                        }
                    }
                },
                {
                    "name": "\u8206\u60c5\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,158,59)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u7406\u89e3",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,83,158)"
                        }
                    }
                },
                {
                    "name": "\u610f\u56fe\u7406\u89e3",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,9,61)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u6458\u8981",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,90,132)"
                        }
                    }
                },
                {
                    "name": "query\u5206\u6790",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,29,24)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,32,18)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u5199\u7ea0\u9519",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,130,94)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u753b\u50cf",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,65,86)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u7279\u5f81",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,90,100)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u53ec\u56de",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,118,149)"
                        }
                    }
                },
                {
                    "name": "\u591a\u8f6e\u5bf9\u8bdd",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,147,14)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,160,47)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u68c0\u7d22",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,155,60)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u5173\u6027",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,96,116)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u67e5\u8be2",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,45,139)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u8c31\u63a8\u7406",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,38,140)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u6587\u672c",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,62,88)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u6587\u672c",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,2,24)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544aNLP",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,78,21)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u7406\u89e3",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,108,29)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u5b89\u5168",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,129,58)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u8baf\u63a8\u8350\u548c\u641c\u7d22",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,145,122)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u884c\u4e3a\u5206\u6790",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,32,87)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u8f6c\u5199",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,100,149)"
                        }
                    }
                },
                {
                    "name": "UGC\u6316\u6398",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,4,138)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5f8b\u95ee\u7b54",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,143,155)"
                        }
                    }
                },
                {
                    "name": "\u9605\u8bfb\u7406\u89e3",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,65,149)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u6807\u7b7e\u4f53\u7cfb",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,136,43)"
                        }
                    }
                },
                {
                    "name": "\u4efb\u52a1\u5f0f\u5bf9\u8bdd\u7cfb\u7edf",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,87,63)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672cspam\u8bc6\u522b",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,82,119)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6559\u80b2\u9886\u57df",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,19,104)"
                        }
                    }
                },
                {
                    "name": "\u50ac\u6536\u6587\u672c\u6316\u6398",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,155,129)"
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
        chart_39e4e09c36544f2591ef3d7c9f0c178b.setOption(option_39e4e09c36544f2591ef3d7c9f0c178b);
    </script>
                <div id="7c8fe1e88fff48d28c862a609e202658" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_7c8fe1e88fff48d28c862a609e202658 = echarts.init(
            document.getElementById('7c8fe1e88fff48d28c862a609e202658'), 'white', {renderer: 'canvas'});
            
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
    
        var option_7c8fe1e88fff48d28c862a609e202658 = {
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
                            "color": "rgb(37,145,56)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,125,38)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,51,151)"
                        }
                    }
                },
                {
                    "name": "GO",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,78,109)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,29,95)"
                        }
                    }
                },
                {
                    "name": "TensorFlow",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,128,131)"
                        }
                    }
                },
                {
                    "name": "Keras",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,77,16)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,63,150)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u5219\u8868\u8fbe\u5f0f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,20,40)"
                        }
                    }
                },
                {
                    "name": "\u547d\u540d\u5b9e\u4f53\u8bc6\u522b",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,82,150)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,119,99)"
                        }
                    }
                },
                {
                    "name": "\u5c5e\u6027\u62bd\u53d6",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,58,41)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u62bd\u53d6",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,127,87)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u5206\u7c7b",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,5,92)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u76f8\u4f3c\u5ea6\u8ba1\u7b97",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,30,133)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u62bd\u53d6",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,95,48)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7b97\u6cd5",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,116,136)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49\u5339\u914d",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,14,2)"
                        }
                    }
                },
                {
                    "name": "\u5e8f\u5217\u6807\u6ce8",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,128,144)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u5b66\u4e60",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,113,91)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001\u7406\u89e3",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,39,138)"
                        }
                    }
                },
                {
                    "name": "\u6587\u672c\u8868\u793a",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,86,135)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u5173\u6027",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,106,132)"
                        }
                    }
                },
                {
                    "name": "\u5206\u8bcd",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,124,72)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,115,59)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u751f\u6210",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,66,46)"
                        }
                    }
                },
                {
                    "name": "Embedding",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,144,94)"
                        }
                    }
                },
                {
                    "name": "Q&A",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,39,68)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,7,154)"
                        }
                    }
                },
                {
                    "name": "SelfAttention",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,23,21)"
                        }
                    }
                },
                {
                    "name": "lda",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,53,15)"
                        }
                    }
                },
                {
                    "name": "RNN",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,113,48)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,144,37)"
                        }
                    }
                },
                {
                    "name": "seq2seq",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,55,50)"
                        }
                    }
                },
                {
                    "name": "Word2vec",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,132,122)"
                        }
                    }
                },
                {
                    "name": "GPT2",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,16,104)"
                        }
                    }
                },
                {
                    "name": "Transformer",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,2,107)"
                        }
                    }
                },
                {
                    "name": "BERT",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,102,48)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u9898\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,66,23)"
                        }
                    }
                },
                {
                    "name": "KBQA",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,37,77)"
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
        chart_7c8fe1e88fff48d28c862a609e202658.setOption(option_7c8fe1e88fff48d28c862a609e202658);
    </script>
                <div id="8aebcb38de1b47208fe166602aa04082" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_8aebcb38de1b47208fe166602aa04082 = echarts.init(
            document.getElementById('8aebcb38de1b47208fe166602aa04082'), 'white', {renderer: 'canvas'});
            
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
    
        var option_8aebcb38de1b47208fe166602aa04082 = {
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
                            "color": "rgb(92,17,49)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,38,135)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,98,18)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u5f71\u50cf\u7406\u89e3",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,157,121)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u68c0\u6d4b\u548c\u8ddf\u8e2a",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,143,149)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,45,20)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u641c\u7d22",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,13,152)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5b9e\u73b0",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,78,145)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,155,29)"
                        }
                    }
                },
                {
                    "name": "\u6027\u80fd\u4f18\u5316",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,22,134)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u89c6\u9891",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,8,82)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u7247\u5185\u5bb9\u751f\u6210",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,6,21)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,68,67)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8c61\u63d0\u53d6",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,136,31)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u611f\u77e5",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,154,47)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u5206\u7c7b",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,14,128)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u8ddf\u8e2a",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,53,101)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7ed3\u6784\u5316",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,131,59)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,156,101)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u89e3\u8bd1",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,40,138)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4ef6\u5206\u6790",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,136,159)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29\u8f7b\u91cf\u5316\u5e94\u7528",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,68,11)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,94,4)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u548c\u5bfc\u822a",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,103,157)"
                        }
                    }
                },
                {
                    "name": "\u6ee4\u955c\u521b\u4f5c\u5de5\u5177",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,20,9)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u70b9\u68c0\u6d4b",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,114,66)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u751f\u6210",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,0,88)"
                        }
                    }
                },
                {
                    "name": "AR/MR",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,20,90)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,114,53)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u6444\u5f71",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,73,2)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,58,45)"
                        }
                    }
                },
                {
                    "name": "\u6750\u8d28\u548c\u5916\u89c2\u91cd\u5efa",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,147,130)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u91cf\u5b66\u4e60",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,30,91)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u4e49/\u5b9e\u4f8b\u5206\u5272",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,121,126)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5b57\u68c0\u6d4b\u8bc6\u522b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,82,122)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u68c0\u6d4b\u8bc6\u522b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,44,46)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7f16\u8f91\u751f\u6210",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,58,129)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u683c\u8fc1\u79fb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,38,152)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56fe\u79c0\u79c0",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,140,0)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u62cd",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,102,119)"
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
        chart_8aebcb38de1b47208fe166602aa04082.setOption(option_8aebcb38de1b47208fe166602aa04082);
    </script>
                <div id="99007c7d41e1496482dba07f69926f2e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_99007c7d41e1496482dba07f69926f2e = echarts.init(
            document.getElementById('99007c7d41e1496482dba07f69926f2e'), 'white', {renderer: 'canvas'});
            
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
    
        var option_99007c7d41e1496482dba07f69926f2e = {
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
                            "color": "rgb(130,62,96)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b/\u5206\u7c7b",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,158,78)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4f53\u68c0\u6d4b",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,93,83)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,68,157)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,130,142)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5206\u5272",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,105,89)"
                        }
                    }
                },
                {
                    "name": "GAN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,99,98)"
                        }
                    }
                },
                {
                    "name": "Linux",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,117,122)"
                        }
                    }
                },
                {
                    "name": "tensorflow",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,122,132)"
                        }
                    }
                },
                {
                    "name": "pytorch",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,47,147)"
                        }
                    }
                },
                {
                    "name": "C++",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,105,84)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,15,46)"
                        }
                    }
                },
                {
                    "name": "CVPR",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,159,97)"
                        }
                    }
                },
                {
                    "name": "ECCV",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,114,50)"
                        }
                    }
                },
                {
                    "name": "ICCV",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,119,66)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8bad\u7ec3",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,97,102)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6a21\u6001",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,152,10)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u76d1\u7763/\u534a\u76d1\u7763\u5b66\u4e60",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,85,7)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,67,101)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u751f\u6210",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,132,152)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u9891\u8bc6\u522b",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,61,6)"
                        }
                    }
                },
                {
                    "name": "OCR",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,13,9)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u538b\u7f29",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,23,122)"
                        }
                    }
                },
                {
                    "name": "SLAM",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,90,113)"
                        }
                    }
                },
                {
                    "name": "OpenCV",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,94,98)"
                        }
                    }
                },
                {
                    "name": "PCL",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,40,151)"
                        }
                    }
                },
                {
                    "name": "\u5355\u76ee/\u53cc\u76ee\u6df1\u5ea6\u4f30\u8ba1",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,89,79)"
                        }
                    }
                },
                {
                    "name": "\u76f8\u673a\u6807\u5b9a/\u914d\u51c6",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,68,84)"
                        }
                    }
                },
                {
                    "name": "3D\u7269\u4f53\u8bc6\u522b\u4e0e\u5206\u5272",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,76,132)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,140,5)"
                        }
                    }
                },
                {
                    "name": "Visual SLAM",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,82,102)"
                        }
                    }
                },
                {
                    "name": "SfM\u3001MVS",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,112,115)"
                        }
                    }
                },
                {
                    "name": "\u5206\u7c7b",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,17,156)"
                        }
                    }
                },
                {
                    "name": "\u56de\u5f52",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,59,147)"
                        }
                    }
                },
                {
                    "name": "\u805a\u7c7b",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,5,157)"
                        }
                    }
                },
                {
                    "name": "\u6982\u7387\u6a21\u578b",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,87,85)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,114,38)"
                        }
                    }
                },
                {
                    "name": "\u6587\u732e\u9605\u8bfb",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,117,117)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u5b66\u4e60\u80fd\u529b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,36,149)"
                        }
                    }
                },
                {
                    "name": "CNN",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,122,88)"
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
        chart_99007c7d41e1496482dba07f69926f2e.setOption(option_99007c7d41e1496482dba07f69926f2e);
    </script>
                <div id="49d375c0bb6f4699b66facabaab24089" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_49d375c0bb6f4699b66facabaab24089 = echarts.init(
            document.getElementById('49d375c0bb6f4699b66facabaab24089'), 'white', {renderer: 'canvas'});
            
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
    
        var option_49d375c0bb6f4699b66facabaab24089 = {
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
                            "color": "rgb(89,110,157)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u6838\u5fc3\u7b97\u6cd5\u7814\u53d1",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,96,4)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5174\u8da3\u5efa\u6a21",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,122,70)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u5b9e\u65f6\u610f\u56fe\u5efa\u6a21",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,8,131)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,53,1)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,148,46)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u9001\u7b97\u6cd5",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,88,141)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,65,119)"
                        }
                    }
                },
                {
                    "name": "\u6392\u5e8f",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,109,141)"
                        }
                    }
                },
                {
                    "name": "\u51b7\u542f\u52a8",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,19,137)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u4f18\u5316",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,3,85)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u80fd\u529b\u6a21\u578b",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,59,105)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u9700\u5173\u7cfb\u6a21\u578b",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,144,111)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b56\u7565",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,135,49)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u63a8\u8350",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,128,140)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22/\u5e7f\u544a",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,79,123)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,128,32)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8425\u9500",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,45,66)"
                        }
                    }
                },
                {
                    "name": "feed\u6d41\u63a8\u8350\u3001\u76f8\u5173\u6027\u63a8\u8350",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,123,58)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d28\u91cf\u4f53\u7cfb",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,157,11)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u6807\u7b7e\u4f53\u7cfb",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,8,24)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5355\u9884\u4f30",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,160,62)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,23,6)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,26,16)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,134,159)"
                        }
                    }
                },
                {
                    "name": "\u6296\u97f3",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,95,80)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,63,97)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,125,59)"
                        }
                    }
                },
                {
                    "name": "\u7ebf\u4e0a\u6392\u5e8f\u7cfb\u7edf",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,78,8)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,62,3)"
                        }
                    }
                },
                {
                    "name": "\u957f\u77ed\u671f\u753b\u50cf",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,10,125)"
                        }
                    }
                },
                {
                    "name": "query\u7406\u89e3",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,157,21)"
                        }
                    }
                },
                {
                    "name": "query\u76f8\u5173\u63a8\u8350",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,3,18)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u4f18\u5316",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,77,47)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5316",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,27,37)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u65f6\u957f",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,145,136)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u7559\u5b58",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,106,150)"
                        }
                    }
                },
                {
                    "name": "\u505c\u7559\u65f6\u957f\u4f18\u5316",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,101,1)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u4f18\u5316",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,35,0)"
                        }
                    }
                },
                {
                    "name": "\u7559\u5b58\u7387\u4f18\u5316",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,23,104)"
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
        chart_49d375c0bb6f4699b66facabaab24089.setOption(option_49d375c0bb6f4699b66facabaab24089);
    </script>
                <div id="9e2b27e3360943f49beae05acd64196f" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_9e2b27e3360943f49beae05acd64196f = echarts.init(
            document.getElementById('9e2b27e3360943f49beae05acd64196f'), 'white', {renderer: 'canvas'});
            
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
    
        var option_9e2b27e3360943f49beae05acd64196f = {
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
                            "color": "rgb(22,20,157)"
                        }
                    }
                },
                {
                    "name": "Tensorflow",
                    "value": 99,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,57,60)"
                        }
                    }
                },
                {
                    "name": "PyTorch",
                    "value": 98,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,25,126)"
                        }
                    }
                },
                {
                    "name": "\u534f\u540c\u8fc7\u6ee4",
                    "value": 97,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,106,10)"
                        }
                    }
                },
                {
                    "name": "FM",
                    "value": 96,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,68,93)"
                        }
                    }
                },
                {
                    "name": "LR",
                    "value": 95,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,88,31)"
                        }
                    }
                },
                {
                    "name": "NN",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,28,119)"
                        }
                    }
                },
                {
                    "name": "LSTM",
                    "value": 93,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,76,43)"
                        }
                    }
                },
                {
                    "name": "GBDT",
                    "value": 92,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,14,81)"
                        }
                    }
                },
                {
                    "name": "C/C++",
                    "value": 91,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,44,126)"
                        }
                    }
                },
                {
                    "name": "Python",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,44,74)"
                        }
                    }
                },
                {
                    "name": "Java",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,77,72)"
                        }
                    }
                },
                {
                    "name": "Hadoop",
                    "value": 88,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,113,8)"
                        }
                    }
                },
                {
                    "name": "Spark",
                    "value": 87,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,102,56)"
                        }
                    }
                },
                {
                    "name": "Storm",
                    "value": 86,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,19,139)"
                        }
                    }
                },
                {
                    "name": "CTR\u9884\u4f30",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,51,33)"
                        }
                    }
                },
                {
                    "name": "xgboost",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,124,83)"
                        }
                    }
                },
                {
                    "name": "lightgbm",
                    "value": 83,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,86,154)"
                        }
                    }
                },
                {
                    "name": "catboost",
                    "value": 82,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,86,40)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u6216\u641c\u7d22\u76f8\u5173\u7ecf\u9a8c",
                    "value": 81,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,47,33)"
                        }
                    }
                },
                {
                    "name": "\u53ec\u56de/\u6392\u5e8f\u7b97\u6cd5",
                    "value": 80,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,158,129)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,102,78)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60",
                    "value": 78,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,110,104)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 77,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,68,90)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u6a21\u578b",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,6,29)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u6392\u5e8f",
                    "value": 75,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,56,23)"
                        }
                    }
                },
                {
                    "name": "LearningToRank",
                    "value": 74,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,54,45)"
                        }
                    }
                },
                {
                    "name": "word2vec",
                    "value": 73,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,74,52)"
                        }
                    }
                },
                {
                    "name": "RecSys",
                    "value": 72,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,151,147)"
                        }
                    }
                },
                {
                    "name": "SIGIR",
                    "value": 71,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,156,56)"
                        }
                    }
                },
                {
                    "name": "WWW",
                    "value": 70,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,28,51)"
                        }
                    }
                },
                {
                    "name": "ICML",
                    "value": 69,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,110,102)"
                        }
                    }
                },
                {
                    "name": "NIPS",
                    "value": 68,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,114,57)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u51fb\u7387\u9884\u4f30",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,31,21)"
                        }
                    }
                },
                {
                    "name": "\u6295\u9012\u9884\u4f30",
                    "value": 66,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,85,63)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b97\u5efa\u8bae",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,63,113)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4ef7\u673a\u5236",
                    "value": 64,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,27,70)"
                        }
                    }
                },
                {
                    "name": "\u5206\u5e03\u5f0f\u8ba1\u7b97",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,56,11)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u5854\u6a21\u578b",
                    "value": 62,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,120,130)"
                        }
                    }
                },
                {
                    "name": "\u7279\u5f81\u5de5\u7a0b",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,134,100)"
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
        chart_9e2b27e3360943f49beae05acd64196f.setOption(option_9e2b27e3360943f49beae05acd64196f);
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
