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

<h2>（2021-05-31更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, '0c0e85cbaf2e4421b6c12474cb6b26e8')">公司</button>
            <button class="tablinks" onclick="showChart(event, '22e8e6ae4aec40ea84153e75b2e5f0d2')">城市</button>
            <button class="tablinks" onclick="showChart(event, '068a663cdfa74deda80638d1e515dfef')">城市占比</button>
            <button class="tablinks" onclick="showChart(event, '6fdd6eac8bd24413bd762882fbab9df2')">招聘地图</button>
            <button class="tablinks" onclick="showChart(event, 'b97d034c55824b6a88afccb5bbcd7fb6')">区域</button>
            <button class="tablinks" onclick="showChart(event, '0d12b46f727f4072a6e115a910cfa99a')">区域占比</button>
            <button class="tablinks" onclick="showChart(event, '829f320011864ac69fef045f368fc9ed')">公司规模</button>
            <button class="tablinks" onclick="showChart(event, 'e956a72f6a904fc7a8ccb87142e5dc14')">人员规模</button>
            <button class="tablinks" onclick="showChart(event, 'c0f07fe394c14b8a9de090f645cee18b')">行业</button>
            <button class="tablinks" onclick="showChart(event, '4f9e455d3f674f10a4c3cd9e317c3ae4')">招聘方向</button>
            <button class="tablinks" onclick="showChart(event, '0f1ba153e9cd452c958efa8579768e62')">公司福利</button>
    </div>

    <div class="box">
                <div id="0c0e85cbaf2e4421b6c12474cb6b26e8" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_0c0e85cbaf2e4421b6c12474cb6b26e8 = echarts.init(
            document.getElementById('0c0e85cbaf2e4421b6c12474cb6b26e8'), 'white', {renderer: 'canvas'});
            
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
    
        var option_0c0e85cbaf2e4421b6c12474cb6b26e8 = {
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
                44,
                24,
                20,
                18,
                16,
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
                    "name": "\u7f8e\u56e2",
                    "value": 45,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,148,14)"
                        }
                    }
                },
                {
                    "name": "\u5b57\u8282\u8df3\u52a8",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,160,89)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79d1\u6280",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,149,152)"
                        }
                    }
                },
                {
                    "name": "Insta360\u5f71\u77f3",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,156,85)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,110,3)"
                        }
                    }
                },
                {
                    "name": "\u9177\u72d7\u97f3\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,69,19)"
                        }
                    }
                },
                {
                    "name": "OPPO",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,133,1)"
                        }
                    }
                },
                {
                    "name": "\u9177\u5bb6\u4e50",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,90,49)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u8d4b\u667a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,41,101)"
                        }
                    }
                },
                {
                    "name": "\u62fc\u591a\u591a",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,147,49)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,68,51)"
                        }
                    }
                },
                {
                    "name": "\u964c\u964c",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,125,28)"
                        }
                    }
                },
                {
                    "name": "\u6167\u5b89\u91d1\u79d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,147,43)"
                        }
                    }
                },
                {
                    "name": "\u7231\u5947\u827a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,53,143)"
                        }
                    }
                },
                {
                    "name": "\u5929\u773c\u67e5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,102,32)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96c6\u56e2",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,54,111)"
                        }
                    }
                },
                {
                    "name": "MINIEYE",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,81,110)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6e56\u9662",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,104,130)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5982\u79c4",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,6,158)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,81,23)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u7f51",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,32,116)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4eba\u5bff",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,86,155)"
                        }
                    }
                },
                {
                    "name": "\u6d82\u9e26\u667a\u80fd",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,75,94)"
                        }
                    }
                },
                {
                    "name": "\u767e\u5ea6",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,107,65)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u65b9\u706b\u79cd\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,41,60)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8054\u6570\u636e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,66,55)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5609\u4e92\u8054",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,66,152)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u78c1\u77f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,50,8)"
                        }
                    }
                },
                {
                    "name": "Versa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,28,78)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,75,128)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5c45\u5ba2",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,67,81)"
                        }
                    }
                },
                {
                    "name": "\u8c31\u65f6\u660a\u552f\u6570\u636e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,137,86)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u58f3",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,147,75)"
                        }
                    }
                },
                {
                    "name": "\u732b\u5c90\u667a\u80fd",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,13,160)"
                        }
                    }
                },
                {
                    "name": "\u5f97\u7269App",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,73,69)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u695a\u701a\u624d\u4f20\u5a92",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,70,113)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5730\u91cf\u5b50",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,67,48)"
                        }
                    }
                },
                {
                    "name": "\u65f7\u89c6MEGVII",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,69,44)"
                        }
                    }
                },
                {
                    "name": "DMAI\u667a\u80fd\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,22,49)"
                        }
                    }
                },
                {
                    "name": "\u8054\u5408\u96c6\u56e2",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,15,147)"
                        }
                    }
                },
                {
                    "name": "\u5fc5\u793a\u79d1\u6280",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,7,41)"
                        }
                    }
                },
                {
                    "name": "\u5faa\u73af\u667a\u80fd",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,71,107)"
                        }
                    }
                },
                {
                    "name": "\u8363\u8000\u7ec8\u7aef",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,113,116)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,89,137)"
                        }
                    }
                },
                {
                    "name": "\u53c2\u6570",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,87,32)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u56fe\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,1,158)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u821f\u667a\u822a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,141,59)"
                        }
                    }
                },
                {
                    "name": "\u730e\u6237\u661f\u7a7a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,148,25)"
                        }
                    }
                },
                {
                    "name": "360os",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,42,133)"
                        }
                    }
                },
                {
                    "name": "\u7693\u884c\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,140,137)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u624b",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,120,56)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u597d\u5b66",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,11,120)"
                        }
                    }
                },
                {
                    "name": "\u597d\u672a\u6765",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,119,10)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u521b\u79d1\u6280",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,117,139)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7814\u7a76\u9662",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,124,69)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6e56",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,146,52)"
                        }
                    }
                },
                {
                    "name": "Soul",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,76,106)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4ed3\u667a\u80fd\u4ed3\u50a8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,102,45)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u51b0",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,96,126)"
                        }
                    }
                },
                {
                    "name": "Gostudy",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,20,101)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5b87\u65e0\u9650",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,122,146)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5411\u4e7e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,84,66)"
                        }
                    }
                },
                {
                    "name": "\u5151\u5427",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,1,120)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5c1a\u535a\u745e",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,125,132)"
                        }
                    }
                },
                {
                    "name": "\u827a\u6570\u672a\u6765",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,0,103)"
                        }
                    }
                },
                {
                    "name": "\u660e\u7565\u79d1\u6280\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,57,72)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u76ee\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,98,129)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5c1a\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,33,127)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,103,11)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u667a\u6167",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,31,66)"
                        }
                    }
                },
                {
                    "name": "\u5546\u6c64\u79d1\u6280",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,130,126)"
                        }
                    }
                },
                {
                    "name": "\u643a\u7a0b\u96c6\u56e2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,117,127)"
                        }
                    }
                },
                {
                    "name": "\u6613\u8f66\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,68,43)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5408\u5929\u5730",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,95,77)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u67d4\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,37,40)"
                        }
                    }
                },
                {
                    "name": "\u4f2f\u6069\u5149\u5b66",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,143,81)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b9d\u6811",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,157,2)"
                        }
                    }
                },
                {
                    "name": "\u6749\u6570\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,25,57)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,156,97)"
                        }
                    }
                },
                {
                    "name": "\u6765\u672a\u6765",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,68,23)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u89c6\u521b\u65b0",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,158,155)"
                        }
                    }
                },
                {
                    "name": "\u6155\u601d\u5065\u5eb7\u7761\u7720",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,160,11)"
                        }
                    }
                },
                {
                    "name": "\u9890\u90a6\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,87,145)"
                        }
                    }
                },
                {
                    "name": "GYENNO",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,45,137)"
                        }
                    }
                },
                {
                    "name": "\u8fbe\u89c2\u6570\u636e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,85,107)"
                        }
                    }
                },
                {
                    "name": "\u6597\u9c7c\u76f4\u64ad",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,122,26)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5b8f\u74f4\u79d1\u6280\u53d1\u5c55\u6709\u9650...",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,63,59)"
                        }
                    }
                },
                {
                    "name": "\u5cb1\u609f\u667a\u80fd",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,130,45)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u4e09\u7ef4\u5bb6\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,33,123)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6df1\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,84,123)"
                        }
                    }
                },
                {
                    "name": "\u706b\u773c\u4e91",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,23,99)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u6da6\u5bcc\u8054",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,53,75)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u4fe1\u91d1\u79d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,69,2)"
                        }
                    }
                },
                {
                    "name": "\u5219\u4e00\u4f9b\u5e94\u94fe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,158,116)"
                        }
                    }
                },
                {
                    "name": "\u5143\u6a61\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,154,13)"
                        }
                    }
                },
                {
                    "name": "\u6b63\u96c5\u9f7f\u79d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,37,82)"
                        }
                    }
                },
                {
                    "name": "\u8611\u83c7\u8857",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,111,29)"
                        }
                    }
                },
                {
                    "name": "\u666e\u6e21\u79d1\u6280",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,49,13)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u89c6\u533b\u7597",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,45,66)"
                        }
                    }
                },
                {
                    "name": "\u5927\u540d\u8f6f\u4ef6",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,29,157)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u62cd\u5802",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,35,81)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6cdb\u89c6\u89d2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,124,148)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u7b77\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,119,26)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u667a\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,96,84)"
                        }
                    }
                },
                {
                    "name": "\u835f\u8bda\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,31,88)"
                        }
                    }
                },
                {
                    "name": "\u533b\u836f\u9b54\u65b9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,148,20)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,65,128)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u82bd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,26,10)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u7eff\u571f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,27,123)"
                        }
                    }
                },
                {
                    "name": "\u9053\u9053",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,70,38)"
                        }
                    }
                },
                {
                    "name": "\u89c2\u8fdc\u6570\u636e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,130,134)"
                        }
                    }
                },
                {
                    "name": "AKULAKU",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,83,19)"
                        }
                    }
                },
                {
                    "name": "FunPlus \u8da3\u52a0\u6e38\u620f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,0,10)"
                        }
                    }
                },
                {
                    "name": "\u5916\u8111\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,150,62)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u5a31\u65f6\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,25,81)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,141,112)"
                        }
                    }
                },
                {
                    "name": "BLUE",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,133,35)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u9014\u8bfe\u5802",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,105,129)"
                        }
                    }
                },
                {
                    "name": "\u745e\u9f99\u90a6\u730e\u5934",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,61,53)"
                        }
                    }
                },
                {
                    "name": "\u597d\u897f\u67da\u6559\u80b2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,144,81)"
                        }
                    }
                },
                {
                    "name": "\u7279\u9e4f\u7f51\u7edc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,88,60)"
                        }
                    }
                },
                {
                    "name": "EM3",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,138,136)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7c73\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,121,87)"
                        }
                    }
                },
                {
                    "name": "\u7269\u754c\uff08\u4e0a\u6d77\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,135,82)"
                        }
                    }
                },
                {
                    "name": "Roborock",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,27,2)"
                        }
                    }
                },
                {
                    "name": "\u601d\u8d24\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,148,131)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u535a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,23,6)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u4ea7\u9669",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,19,25)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u822a\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,107,23)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u96c6\u56e2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,156,5)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5764\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,103,38)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u5fc3\u97f3\u7b26",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,66,34)"
                        }
                    }
                },
                {
                    "name": "\u641c\u624d\u4eba\u529b\u8d44\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,47,94)"
                        }
                    }
                },
                {
                    "name": "Disney+Hotstar",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,91,28)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5149",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,133,2)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e92\u6559\u6559\u80b2\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,48,128)"
                        }
                    }
                },
                {
                    "name": "\u597d\u5927\u592b\u5728\u7ebf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,2,81)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u79d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,69,149)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u77e5\u672a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,129,49)"
                        }
                    }
                },
                {
                    "name": "NIO\u851a\u6765",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,129,71)"
                        }
                    }
                },
                {
                    "name": "Walmart China",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,154,139)"
                        }
                    }
                },
                {
                    "name": "\u601d\u7ef4\u9020\u7269",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,109,13)"
                        }
                    }
                },
                {
                    "name": "Mobvista",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,54,9)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,90,76)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u90ae\u653f\u50a8\u84c4\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,58,27)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u97f3\u667a\u80fd\u79d1\u6280  SpeakIn",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,105,19)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,16,32)"
                        }
                    }
                },
                {
                    "name": "\u9646\u91d1\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,40,156)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u805a\u96c6\u56e2\uff08JOYY Inc.\uff09",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,148,75)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u5ba2\u6734\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,60,16)"
                        }
                    }
                },
                {
                    "name": "\u58a8\u4e91\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,5,49)"
                        }
                    }
                },
                {
                    "name": "\u8304\u5b50\u5feb\u4f20",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,133,106)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5eb7\u5a01\u89c6",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,140,57)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,132,125)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5947\u667a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,59,24)"
                        }
                    }
                },
                {
                    "name": "Convert lab",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,91,23)"
                        }
                    }
                },
                {
                    "name": "\u89e6\u5b9d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,59,1)"
                        }
                    }
                },
                {
                    "name": "\u574e\u5fb7\u62c9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,17,68)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u514b\u65af\u5de5\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,151,91)"
                        }
                    }
                },
                {
                    "name": "\u767e\u878d\u4e91\u521b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,54,80)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u601d\u4fe1\u5b89",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,105,152)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u676d\u5dde\u7814\u7a76\u6240",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,1,11)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u9c7c\u6613\u8fde",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,25,74)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e3a\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,128,34)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u91d1\u878d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,106,155)"
                        }
                    }
                },
                {
                    "name": "westwell\u897f\u4e95\u79d1\u6280",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,54,99)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6c38\u8f89\u8d85\u5e02\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,58,85)"
                        }
                    }
                },
                {
                    "name": "\u552f\u54c1\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,57,147)"
                        }
                    }
                },
                {
                    "name": "LAYABOX",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,76,153)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u60f3\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,65,129)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u9e3d\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,71,98)"
                        }
                    }
                },
                {
                    "name": "\u5a5a\u793c\u7eaa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,153,147)"
                        }
                    }
                },
                {
                    "name": "\u9cb2\u9e4f\u4e91\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,83,95)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7075\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,144,151)"
                        }
                    }
                },
                {
                    "name": "\u8fc1\u79fb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,79,129)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e3a\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,63,17)"
                        }
                    }
                },
                {
                    "name": "\u73cd\u7231\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,124,9)"
                        }
                    }
                },
                {
                    "name": "\u90bb\u6c47\u5427",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,94,116)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fe1\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,82,11)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u4fe1\u521b\u8054",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,26,139)"
                        }
                    }
                },
                {
                    "name": "\u6700\u6709\u6599",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,101,80)"
                        }
                    }
                },
                {
                    "name": "\u7ecf\u4f20\u591a\u8d62",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,13,63)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u7586\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,119,118)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\uff08\u4e2d\u56fd\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,58,143)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98de\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,94,4)"
                        }
                    }
                },
                {
                    "name": "\u4e50\u6211\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,31,32)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5766\u667a\u6167",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,80,8)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u6167\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,6,117)"
                        }
                    }
                },
                {
                    "name": "\u8861\u660a\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,118,24)"
                        }
                    }
                },
                {
                    "name": "\u54c8\u5570\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,116,117)"
                        }
                    }
                },
                {
                    "name": "\u878d360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,41,54)"
                        }
                    }
                },
                {
                    "name": "\u5929\u667a\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,36,2)"
                        }
                    }
                },
                {
                    "name": "\u53ca\u672a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,119,124)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u8bc1\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,131,107)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u89c2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,131,130)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u9536\u5170\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,80,9)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u7ff0\u683c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,51,72)"
                        }
                    }
                },
                {
                    "name": "\u6613\u822a\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,36,5)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u770b\u6f2b\u753b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,111,89)"
                        }
                    }
                },
                {
                    "name": "LinkDoc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,83,34)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7814\u7f51",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,37,51)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5c0f\u8fc8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,59,120)"
                        }
                    }
                },
                {
                    "name": "\u4f17\u4eab\u5929\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,71,136)"
                        }
                    }
                },
                {
                    "name": "\u827e\u5fb7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,26,129)"
                        }
                    }
                },
                {
                    "name": "\u661f\u8206\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,131,85)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u56fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,10,29)"
                        }
                    }
                },
                {
                    "name": "\u6570\u7f8e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,20,58)"
                        }
                    }
                },
                {
                    "name": "360",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,20,68)"
                        }
                    }
                },
                {
                    "name": "Shopee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,160,45)"
                        }
                    }
                },
                {
                    "name": "roobo",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,64,101)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11\u5065\u5eb7",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,85,160)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u835f\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,10,136)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u65b9\u548c\u5317\u4eac",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,69,0)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6295\u5b66\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,83,59)"
                        }
                    }
                },
                {
                    "name": "\u6613\u6d41",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,141,152)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6d4b\u5bfc\u822a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,138,85)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u63a2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,118,76)"
                        }
                    }
                },
                {
                    "name": "\u51cc\u5b87\u667a\u63a7\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,86,33)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f71APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,30,129)"
                        }
                    }
                },
                {
                    "name": "\u661f\u5c18\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,32,134)"
                        }
                    }
                },
                {
                    "name": "\u777f\u9b54\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,82,139)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u9053\u5b87",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,159,42)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77\u4f18\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,79,109)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u6709\u4f20\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,110,52)"
                        }
                    }
                },
                {
                    "name": "RealAI",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,143,152)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8d5e|Tezign",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,67,29)"
                        }
                    }
                },
                {
                    "name": "\u534e\u91cc\u7f51\u7edc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,10,16)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u8f91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,63,156)"
                        }
                    }
                },
                {
                    "name": "\u8fc8\u6da6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,159,64)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,78,16)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u6700\u597d\u7684\u5728\u7ebf\u4eba\u8138\u8bc6\u522b\u5f15\u64ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,111,62)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u56fd\u4fe1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,8,68)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u4fe1\u65f6\u4ee3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,87,94)"
                        }
                    }
                },
                {
                    "name": "\u638c\u9605",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,83,79)"
                        }
                    }
                },
                {
                    "name": "\u751f\u7269\u56fe\u817e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,43,32)"
                        }
                    }
                },
                {
                    "name": "\u5600\u55d2\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,147,64)"
                        }
                    }
                },
                {
                    "name": "\u949b\u6c2a\u65b0\u5a92\u4f53\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,108,4)"
                        }
                    }
                },
                {
                    "name": "\u89c5\u777f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,73,37)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u8d8a\u901f\u8fd0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,74,103)"
                        }
                    }
                },
                {
                    "name": "Rokid",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,55,43)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u90ae\u4fe1\u606f\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,78,85)"
                        }
                    }
                },
                {
                    "name": "\u6d6a\u6dd8\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,72,80)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6cf0\u661f\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,136,40)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5e0c\u671b\u516d\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,4,123)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u8ff9\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,48,72)"
                        }
                    }
                },
                {
                    "name": "StepBeats",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,50,118)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u76db\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,60,13)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u884c\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,119,12)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u76fe\u6570\u636e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,20,137)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e91\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,143,35)"
                        }
                    }
                },
                {
                    "name": "\u536b\u74f4\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,147,153)"
                        }
                    }
                },
                {
                    "name": "\u521b\u90bb\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,125,53)"
                        }
                    }
                },
                {
                    "name": "\u6807\u8d1d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,53,147)"
                        }
                    }
                },
                {
                    "name": "eBrain",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,139,49)"
                        }
                    }
                },
                {
                    "name": "\u71e7\u4eba\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,98,30)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u96c6\u56e2IT",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,156,136)"
                        }
                    }
                },
                {
                    "name": "Long Bridge",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,56,61)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u53f7\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,79,147)"
                        }
                    }
                },
                {
                    "name": "PowerVision",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,12,105)"
                        }
                    }
                },
                {
                    "name": "\u767d\u7280\u725b\u667a\u8fbe\uff08\u5317\u4eac\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,13,109)"
                        }
                    }
                },
                {
                    "name": "\u6765\u56de\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,27,58)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u5f18\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,119,3)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u725b\u7535\u52a8\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,49,145)"
                        }
                    }
                },
                {
                    "name": "\u7075\u52a8\u97f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,57,72)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u4e30\u5de2\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,8,123)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u5149\u534e\u667a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,7,61)"
                        }
                    }
                },
                {
                    "name": "\u745e\u591a\u601d\u533b\u7597",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,126,86)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u7279\u7eb3\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,62,48)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u9ed1\u683c\u667a\u9020\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,151,72)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e5d\u8857\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,154,122)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u94fe\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,104,58)"
                        }
                    }
                },
                {
                    "name": "\u8d27\u7279\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,44,47)"
                        }
                    }
                },
                {
                    "name": "\u9ea6\u5b50\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,128,39)"
                        }
                    }
                },
                {
                    "name": "\u6dfb\u624d\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,108,44)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6469\u68ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,113,133)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u79d1\u5b66\u9662\u7535\u5b50\u5b66\u7814\u7a76\u6240\u82cf\u5dde\u7814\u7a76\u9662",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,132,59)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8fc8\u79d1\u65af\u5a92\u4f53\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,49,67)"
                        }
                    }
                },
                {
                    "name": "Ximmerse",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,101,130)"
                        }
                    }
                },
                {
                    "name": "\u6cfd\u97f6\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,118,69)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u777f\u667a\u836f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,110,111)"
                        }
                    }
                },
                {
                    "name": "\u601d\u56fe\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,88,118)"
                        }
                    }
                },
                {
                    "name": "\u6781\u89c6\u89d2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,58,47)"
                        }
                    }
                },
                {
                    "name": "\u901f\u611f\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,96,96)"
                        }
                    }
                },
                {
                    "name": "\u53ee\u549a\u4e70\u83dc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,69,40)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5ddd\u5f18\u548c\u96c6\u56e2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,73,160)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u91ce\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,47,8)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u539f\u6d88\u8d39\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,106,105)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u666e\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,17,111)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7267\u539f\u6570\u5b57\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,55,130)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u72d7\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,74,128)"
                        }
                    }
                },
                {
                    "name": "\u9510\u4ed5\u65b9\u8fbe\u4eba\u529b\u8d44\u6e90\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,121,72)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u987e\u4eba\u529b\u8d44\u6e90",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,90,82)"
                        }
                    }
                },
                {
                    "name": "\u817e\u5c55\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,108,112)"
                        }
                    }
                },
                {
                    "name": "\u777f\u755c\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,13,120)"
                        }
                    }
                },
                {
                    "name": "\u521b\u6cf0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,4,54)"
                        }
                    }
                },
                {
                    "name": "\u888b\u9f20\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,85,132)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6e90\u6052\u9645",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,36,76)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u8bc1\u5238",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,56,105)"
                        }
                    }
                },
                {
                    "name": "\u6653\u6a3e\u667a\u80fd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,97,76)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u529e\u516c\u8f6f\u4ef6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,154,152)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u4e16\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,90,0)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53ca\u96f6\u552e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,133,125)"
                        }
                    }
                },
                {
                    "name": "\u5bc4\u4e91\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,13,22)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u5934\u6761",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,0,33)"
                        }
                    }
                },
                {
                    "name": "\u8206\u9686\u5174\u8fbe",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,107,160)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u91cf\u8d28\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,154,0)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u878d\u521b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,27,12)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u96f6\u8dc3\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,122,38)"
                        }
                    }
                },
                {
                    "name": "\u54d7\u5566\u5566",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,14,24)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9a6c\u4f01\u670d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,119,23)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde\u9886\u89c1\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,37,128)"
                        }
                    }
                },
                {
                    "name": "\u5149\u7ebf\u4e91",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,36,6)"
                        }
                    }
                },
                {
                    "name": "Veniibot\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,12,88)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u516c\u4e92\u52a8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,45,66)"
                        }
                    }
                },
                {
                    "name": "\u572d\u76ee\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,2,3)"
                        }
                    }
                },
                {
                    "name": "\u5929\u55bb\u4fe1\u606f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,50,144)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u7b11\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,126,51)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u660e\u73e0\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,73,37)"
                        }
                    }
                },
                {
                    "name": "\u5047\u9762\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,95,151)"
                        }
                    }
                },
                {
                    "name": "\u97e9\u521b\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,48,113)"
                        }
                    }
                },
                {
                    "name": "\u677e\u7acb\u63a7\u80a1\u96c6\u56e2\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,121,83)"
                        }
                    }
                },
                {
                    "name": "\u521b\u5fc5\u627f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,21,62)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u9c81\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,102,37)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u80a1\u4efd",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,115,51)"
                        }
                    }
                },
                {
                    "name": "\u5947\u68a6\u8005",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,55,116)"
                        }
                    }
                },
                {
                    "name": "\u864e\u535a\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,94,85)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5965\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,146,29)"
                        }
                    }
                },
                {
                    "name": "\u8bc1\u901a\u7535\u5b50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,60,122)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u9002\u751f\u7269",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,88,129)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\uff08\u5e7f\u4e1c\uff09\u4ea7\u4e1a\u4e92\u8054\u7f51...",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,23,152)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u4e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,128,116)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8863\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,110,158)"
                        }
                    }
                },
                {
                    "name": "Moka",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,40,88)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6e90\u8fea\u79d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,97,82)"
                        }
                    }
                },
                {
                    "name": "UU\u8dd1\u817f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,12,88)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u58f0\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,78,37)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u76c8\u745e\u6052",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,23,90)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8111\u94f6\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,151,99)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u8da3social-touch",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,30,25)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u679c\u6bd4\u7279",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,33,139)"
                        }
                    }
                },
                {
                    "name": "AfterShip",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,113,11)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7535",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,28,123)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u84ddCP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,120,30)"
                        }
                    }
                },
                {
                    "name": "Mai",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,114,148)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,3,75)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9Dmall",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,68,108)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6f14\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,101,26)"
                        }
                    }
                },
                {
                    "name": "\u6d3e\u8fe9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,13,119)"
                        }
                    }
                },
                {
                    "name": "KLOOK \u5ba2\u8def\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,11,96)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u6bd4\u7279\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,67,45)"
                        }
                    }
                },
                {
                    "name": "\u4eb2\u5bb6\u7f51\u7edc\u6280\u672f\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,37,102)"
                        }
                    }
                },
                {
                    "name": "\u8fde\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,43,18)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u5174\u79d1\u6280\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,33,112)"
                        }
                    }
                },
                {
                    "name": "\u5b8f\u7131\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,101,100)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5e73\u6d0b\u623f\u5730\u4ea7\u7ecf\u7eaa\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,126,123)"
                        }
                    }
                },
                {
                    "name": "\u4e70\u4e70\u53cb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,5,143)"
                        }
                    }
                },
                {
                    "name": "\u667a\u610f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,36,52)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e30\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,130,30)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5bb6\u5065\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,24,101)"
                        }
                    }
                },
                {
                    "name": "\u7fcc\u65e5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,36,49)"
                        }
                    }
                },
                {
                    "name": "\u5927\u7bb4\uff08\u676d\u5dde\uff09\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,43,49)"
                        }
                    }
                },
                {
                    "name": "\u98de\u5e38\u51c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,125,57)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u751f\u4ea7\u79d1\u5b66\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,72,103)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u6c7d\u7814",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,13,124)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u798f\u7984\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,134,100)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5f84\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,12,66)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e3a\u6570\u7801",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,95,28)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u9886\u4eba\u624d\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,142,138)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u9488\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,0,49)"
                        }
                    }
                },
                {
                    "name": "MetaApp",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,47,64)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u96c4\u4e92\u5a31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,15,153)"
                        }
                    }
                },
                {
                    "name": "\u6c57\u9a6c\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,145,26)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u6052\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,107,101)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u7b97\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,100,33)"
                        }
                    }
                },
                {
                    "name": "\u6167\u62e9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,65,39)"
                        }
                    }
                },
                {
                    "name": "GALASPORTS",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,157,107)"
                        }
                    }
                },
                {
                    "name": "\u6469\u822a\u65f6\u4ee3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,70,117)"
                        }
                    }
                },
                {
                    "name": "\u5965\u7279\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,16,118)"
                        }
                    }
                },
                {
                    "name": "\u5bd3\u8a00\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,73,70)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u4e91\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,42,28)"
                        }
                    }
                },
                {
                    "name": "\u7231\u8bed\u5427",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,25,114)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9ad8\u63a7\u80a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,40,146)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5965\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,50,117)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5353\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2\u670d\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,62,35)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5f55\u8d85\u6e05\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,84,156)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u667a\u7c73\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,45,95)"
                        }
                    }
                },
                {
                    "name": "\u8d22\u76c8\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,144,59)"
                        }
                    }
                },
                {
                    "name": "Riley Cillian\u83b1\u7199\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,6,158)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u6d1b\u514b\u822a\u7a7a\u79d1\u6280\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,136,3)"
                        }
                    }
                },
                {
                    "name": "Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,122,20)"
                        }
                    }
                },
                {
                    "name": "\u7ef4\u5ba2\u6615\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,47,3)"
                        }
                    }
                },
                {
                    "name": "\u8def\u884c\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,131,45)"
                        }
                    }
                },
                {
                    "name": "\u4e01\u9999\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,118,103)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u7f51\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,93,152)"
                        }
                    }
                },
                {
                    "name": "\u8c6a\u732a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,73,85)"
                        }
                    }
                },
                {
                    "name": "\u6570\u777f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,59,142)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4fdd\u9669\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,97,108)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u667a\u52a0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,98,0)"
                        }
                    }
                },
                {
                    "name": "\u9636\u5f62",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,58,54)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u6781\u777f\u79d1\u6280\u6709\u9650\u8d23\u4efb\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,14,92)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u535a\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,125,35)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u53c2\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,85,141)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7acb\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,43,5)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8d62\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,148,109)"
                        }
                    }
                },
                {
                    "name": "Flash express",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,9,78)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5927\u8baf\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,149,92)"
                        }
                    }
                },
                {
                    "name": "vivo",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,63,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5723\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,110,136)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u8f7b\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,37,46)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u6fb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,125,139)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u6469\u8c61\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,119,109)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u4e2d\u8f6f\u534e\u817e\u8f6f\u4ef6\u7cfb\u7edf\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,39,151)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,123,39)"
                        }
                    }
                },
                {
                    "name": "\u516d\u4e00\u6559\u80b2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,107,9)"
                        }
                    }
                },
                {
                    "name": "\u8d28\u5b50\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,119,98)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,88,24)"
                        }
                    }
                },
                {
                    "name": "\u5408\u5408\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,29,89)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u91d1\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,141,19)"
                        }
                    }
                },
                {
                    "name": "\u57c3\u5fae",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,45,54)"
                        }
                    }
                },
                {
                    "name": "\u5531\u5427-\u73a9\u97f3\u4e50\uff0c\u5c31\u4e0a\u5531\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,69,125)"
                        }
                    }
                },
                {
                    "name": "\u8da3\u9014\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,39,10)"
                        }
                    }
                },
                {
                    "name": "\u4f5c\u4e1a\u5e2e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,83,17)"
                        }
                    }
                },
                {
                    "name": "InMobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,116,61)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u6773\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,92,11)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u5174\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,20,102)"
                        }
                    }
                },
                {
                    "name": "\u503c\u5f97\u4e70\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,160,149)"
                        }
                    }
                },
                {
                    "name": "\u4ee5\u89c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,141,4)"
                        }
                    }
                },
                {
                    "name": "\u4f9d\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,60,45)"
                        }
                    }
                },
                {
                    "name": "\u68a6\u9977\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,67,6)"
                        }
                    }
                },
                {
                    "name": "\u6c49\u4eea\u5b57\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,105,123)"
                        }
                    }
                },
                {
                    "name": "\u8354\u679d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,0,41)"
                        }
                    }
                },
                {
                    "name": "\u55b5\u661f\u63a2\u7d22",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,86,12)"
                        }
                    }
                },
                {
                    "name": "\u6f8e\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,45,137)"
                        }
                    }
                },
                {
                    "name": "\u9cb8\u6984\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,123,74)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u6570\u79d1\u96c6\u56e2\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,92,90)"
                        }
                    }
                },
                {
                    "name": "\u5988\u5988\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,53,151)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,92,18)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u65b9\u4f4e\u78b3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,137,113)"
                        }
                    }
                },
                {
                    "name": "\u70ed\u4e91\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,38,93)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u7ef4\u667a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,148,41)"
                        }
                    }
                },
                {
                    "name": "Micagent",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,110,44)"
                        }
                    }
                },
                {
                    "name": "\u6613\u79d1\u5947\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,122,140)"
                        }
                    }
                },
                {
                    "name": "\u76db\u4e16\u9e92\u9e9f\u519c\u4e1a\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,43,118)"
                        }
                    }
                },
                {
                    "name": "DataEye",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,14,42)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,96,104)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u79d1\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,86,51)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u540c\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,75,133)"
                        }
                    }
                },
                {
                    "name": "\u6c90\u77b3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,8,40)"
                        }
                    }
                },
                {
                    "name": "\u6155\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,149,106)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,102,160)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u7279\u7f8e\u8fea",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,47,120)"
                        }
                    }
                },
                {
                    "name": "\u8054\u901a\u65f6\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,101,157)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5cb3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,123,32)"
                        }
                    }
                },
                {
                    "name": "\u76ef\u76ef\u62cd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,48,151)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u4eba\u5bff",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,14,97)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u949b\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,58,34)"
                        }
                    }
                },
                {
                    "name": "\u767b\u8679",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,135,137)"
                        }
                    }
                },
                {
                    "name": "\u82f1\u8bed\u8da3\u914d\u97f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,79,126)"
                        }
                    }
                },
                {
                    "name": "BaseBit AI \u7ffc\u65b9\u5065\u6570",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,12,64)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5730\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,126,72)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u8302\u5929\u521d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,129,124)"
                        }
                    }
                },
                {
                    "name": "\u8eba\u5e73\u8bbe\u8ba1\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,47,4)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u4f18\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,106,82)"
                        }
                    }
                },
                {
                    "name": "Xeno Dynamics",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,84,48)"
                        }
                    }
                },
                {
                    "name": "\u957f\u4ead\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,65,32)"
                        }
                    }
                },
                {
                    "name": "\u6c38\u8f89\u4e91\u521b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,66,65)"
                        }
                    }
                },
                {
                    "name": "\u864e\u7259\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,124,88)"
                        }
                    }
                },
                {
                    "name": "Yeahmobi",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,147,130)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u4e1a\u989c\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,111,97)"
                        }
                    }
                },
                {
                    "name": "\u8109\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,154,12)"
                        }
                    }
                },
                {
                    "name": "\u7545\u6377\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,119,160)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u8fbe\u6570\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,75,43)"
                        }
                    }
                },
                {
                    "name": "\u5149\u9274\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,60,25)"
                        }
                    }
                },
                {
                    "name": "\u9541\u4fe1\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,50,26)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751\u6613\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,82,20)"
                        }
                    }
                },
                {
                    "name": "Nox\u591c\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,160,156)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u91d1\u670d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,3,70)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u5e2e\u7535\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,147,144)"
                        }
                    }
                },
                {
                    "name": "\u667a\u4e91\u5065\u5eb7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,86,88)"
                        }
                    }
                },
                {
                    "name": "\u53cb\u5854\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,49,32)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8f85\u7279\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,61,85)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6b21\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,110,53)"
                        }
                    }
                },
                {
                    "name": "\u6a59\u5b50\u6570\u5b57\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,87,22)"
                        }
                    }
                },
                {
                    "name": "\u9038\u4eab\u7535\u5b50\u5546\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,45,22)"
                        }
                    }
                },
                {
                    "name": "\u4f73\u5146\u4e1a\u6295\u8d44\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,135,54)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u5e74\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,146,158)"
                        }
                    }
                },
                {
                    "name": "\u96f7\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,117,47)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u83dc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,15,58)"
                        }
                    }
                },
                {
                    "name": "\u7231\u7279\u66fc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,28,47)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u80fd\u8fbe\u901a\u4fe1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,91,44)"
                        }
                    }
                },
                {
                    "name": "\u65af\u683c\u56fd\u9645",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,96,1)"
                        }
                    }
                },
                {
                    "name": "\u667a\u795e\u4fe1\u606f\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,89,99)"
                        }
                    }
                },
                {
                    "name": "\u8054\u8fd0\u77e5\u6167\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,81,58)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u89c8\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,78,49)"
                        }
                    }
                },
                {
                    "name": "UMU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,0,65)"
                        }
                    }
                },
                {
                    "name": "\u5c0fi\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,14,138)"
                        }
                    }
                },
                {
                    "name": "\u711c\u8000\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,136,84)"
                        }
                    }
                },
                {
                    "name": "\u54d4\u54e9\u54d4\u54e9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,103,5)"
                        }
                    }
                },
                {
                    "name": "\u53f8\u5357\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,51,61)"
                        }
                    }
                },
                {
                    "name": "\u4e3a\u534e\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,13,65)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u79ef\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,116,37)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u6e38\u7231",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,121,110)"
                        }
                    }
                },
                {
                    "name": "\u5965\u6bd4\u4e2d\u5149",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,15,86)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u4e16\u7eaa\u4e1c\u65b9\u901a\u8baf\u8bbe\u5907\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,81,83)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u839e\u7f8e\u5b9c\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,46,55)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u5b9a\u667a\u6167",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,153,114)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5929\u52b1\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,45,36)"
                        }
                    }
                },
                {
                    "name": "\u8bfa\u5a01\u534e\u4ed5\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,129,43)"
                        }
                    }
                },
                {
                    "name": "\u96ea\u7403",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,7,142)"
                        }
                    }
                },
                {
                    "name": "\u638c\u4e0a\u5148\u673a-\u65fa\u5e97\u901aERP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,11,118)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5219\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,34,122)"
                        }
                    }
                },
                {
                    "name": "\u7545\u804a\u5929\u4e0b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,99,9)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u5e02\u667a\u80fd\u5236\u9020\u8f6f\u4ef6\u5f00\u53d1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,102,43)"
                        }
                    }
                },
                {
                    "name": "IntraMirror",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,73,71)"
                        }
                    }
                },
                {
                    "name": "\u9014\u5bb6\u6c11\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,14,92)"
                        }
                    }
                },
                {
                    "name": "\u886b\u6570\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,118,45)"
                        }
                    }
                },
                {
                    "name": "\u53eb\u53eb\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,51,48)"
                        }
                    }
                },
                {
                    "name": "\u6da6\u5efa\u80a1\u4efd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,147,23)"
                        }
                    }
                },
                {
                    "name": "\u8d1d\u53f6\u65af\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,98,61)"
                        }
                    }
                },
                {
                    "name": "\u8c46\u679c\u7f8e\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,157,141)"
                        }
                    }
                },
                {
                    "name": "\u827e\u7f8e\u7f51\u7edc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,140,134)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7f8e\u63a7\u80a1\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,66,122)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u4e07\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,95,34)"
                        }
                    }
                },
                {
                    "name": "\u7545\u884c\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,120,35)"
                        }
                    }
                },
                {
                    "name": "\u542c\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,140,1)"
                        }
                    }
                },
                {
                    "name": "\u591a\u70b9\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,30,128)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u6210",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,88,2)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u901a\u5feb\u9012",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,96,142)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u5065\u5eb7\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,68,33)"
                        }
                    }
                },
                {
                    "name": "\u83ab\u6bd4\u55e8\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,76,61)"
                        }
                    }
                },
                {
                    "name": "\u5b8c\u7f8e\u4e16\u754c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,120,9)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5c14\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,130,77)"
                        }
                    }
                },
                {
                    "name": "\u64ce\u521b\u66e6\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,113,13)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u4e50\u79cd\u5b50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,146,13)"
                        }
                    }
                },
                {
                    "name": "\u732b\u773c\u7535\u5f71",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,57,78)"
                        }
                    }
                },
                {
                    "name": "\u7b2c\u4e09\u77f3\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,108,32)"
                        }
                    }
                },
                {
                    "name": "\u67ab\u53f6\u4e92\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,111,153)"
                        }
                    }
                },
                {
                    "name": "\u7d2b\u8346\u6843\u674e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,50,75)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,44,96)"
                        }
                    }
                },
                {
                    "name": "Camera360",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,65,79)"
                        }
                    }
                },
                {
                    "name": "\u661f\u9645\u5927\u9646",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,104,113)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u597d\u591a\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,42,146)"
                        }
                    }
                },
                {
                    "name": "\u51ef\u8fea\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,56,58)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u653f\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,124,58)"
                        }
                    }
                },
                {
                    "name": "\u95ea\u5e03\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,5,53)"
                        }
                    }
                },
                {
                    "name": "\u4f0a\u5bf9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,43,95)"
                        }
                    }
                },
                {
                    "name": "\u5fb7\u5fc3\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,154,22)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u96c5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,115,97)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8f66\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,7,49)"
                        }
                    }
                },
                {
                    "name": "e\u7b7e\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,42,114)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u6728\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,76,25)"
                        }
                    }
                },
                {
                    "name": "\u534e\u98ce\u7231\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,106,120)"
                        }
                    }
                },
                {
                    "name": "\u6cf0\u5eb7\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,76,91)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5fc5\u9009\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,76,6)"
                        }
                    }
                },
                {
                    "name": "\u745b\u592a\u83b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,53,54)"
                        }
                    }
                },
                {
                    "name": "\u5343\u5bfb\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,62,76)"
                        }
                    }
                },
                {
                    "name": "\u5f53\u5f53\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,151,15)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,83,127)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u70b9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,108,116)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u667a\u4f17\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,132,75)"
                        }
                    }
                },
                {
                    "name": "\u9756\u6208\u91cf\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,120,141)"
                        }
                    }
                },
                {
                    "name": "\u6708\u76db\u658b\u6295\u8d44\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,113,71)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8d28\u6570\u65af\u8fbe\u514b\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,62,93)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5b8f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,96,0)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u52bf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,129,1)"
                        }
                    }
                },
                {
                    "name": "\u5370\u8c61\u7b14\u8bb0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,146,152)"
                        }
                    }
                },
                {
                    "name": "\u9518\u5d34\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,5,140)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7738\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,123,147)"
                        }
                    }
                },
                {
                    "name": "Kika Tech(\u65b0\u7f8e\u4e92\u901a)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,59,66)"
                        }
                    }
                },
                {
                    "name": "FreeWheel",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,57,56)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u65b0\u5927\u701a\u4eba\u529b\u8d44\u6e90",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,79,4)"
                        }
                    }
                },
                {
                    "name": "\u745e\u5a01\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,48,17)"
                        }
                    }
                },
                {
                    "name": "\u5ea6\u5c0f\u6ee1\u91d1\u878d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,44,18)"
                        }
                    }
                },
                {
                    "name": "\u963f\u5361\u7d22\u5916\u6559\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,145,33)"
                        }
                    }
                },
                {
                    "name": "WeLab\u536b\u76c8\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,127,84)"
                        }
                    }
                },
                {
                    "name": "\u592a\u5b57\u6d41\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,143,147)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u8003\u76f4\u901a\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,145,129)"
                        }
                    }
                },
                {
                    "name": "\u591a\u725b\u4f20\u5a92",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,107,155)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u901a\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,85,125)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u70b9\u8d44\u8baf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,54,98)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u5e7f\u4fe1\u901a\u4fe1\u670d\u52a1\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,6,143)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5de5\u540c\u667a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,148,51)"
                        }
                    }
                },
                {
                    "name": "\u534e\u665f\u660e\u9014",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,13,87)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u4f73\u4fe1\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,124,11)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u706f\u9c7c\u667a\u80fd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,47,95)"
                        }
                    }
                },
                {
                    "name": "\u5373\u6784\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,59,85)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u96c6\u8054\u7f51\u7edc\u6280\u672f\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,17,13)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u7f51\u7edc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,82,135)"
                        }
                    }
                },
                {
                    "name": "\u5bfa\u5e93",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,109,50)"
                        }
                    }
                },
                {
                    "name": "\u7c73\u7edc\u661f\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,145,142)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u6b65\u5728\u5bb6\u65e9\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,65,39)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u81f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,29,96)"
                        }
                    }
                },
                {
                    "name": "\u777f\u8c61\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,107,59)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u4e1c\u8dc3\u6609\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,118,43)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u7fcc\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,110,115)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u5927\u5b66\u667a\u80fd\u4ea7\u4e1a\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,34,79)"
                        }
                    }
                },
                {
                    "name": "\u5353\u8f69\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,74,80)"
                        }
                    }
                },
                {
                    "name": "Fordeal",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,157,63)"
                        }
                    }
                },
                {
                    "name": "\u67d2\u96f6\u58f9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,129,124)"
                        }
                    }
                },
                {
                    "name": "\u4e98\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,134,96)"
                        }
                    }
                },
                {
                    "name": "FREE BRIO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,131,96)"
                        }
                    }
                },
                {
                    "name": "\u660e\u6e90\u4e91\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,92,156)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u5361",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,117,70)"
                        }
                    }
                },
                {
                    "name": "\u94a2\u94c1\u4fa0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,131,51)"
                        }
                    }
                },
                {
                    "name": "\u84dd\u6df1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,65,4)"
                        }
                    }
                },
                {
                    "name": "\u4e3d\u7acb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,152,26)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u7ae0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,125,86)"
                        }
                    }
                },
                {
                    "name": "\u6570\u5b57\u4ea7\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,67,155)"
                        }
                    }
                },
                {
                    "name": "\u5a01\u661f\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,14,85)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u4ed5\u8fbe\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,106,142)"
                        }
                    }
                },
                {
                    "name": "\u51b0\u6cb3\u4e91\u5b58\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,99,80)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u51cc\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,114,118)"
                        }
                    }
                },
                {
                    "name": "\u7384\u6b66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,11,97)"
                        }
                    }
                },
                {
                    "name": "\u5341\u624d\u730e\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,66,41)"
                        }
                    }
                },
                {
                    "name": "\u5154\u73a9\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,144,26)"
                        }
                    }
                },
                {
                    "name": "\u8c61\u5fc3\u529b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,129,67)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5f66\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,4,54)"
                        }
                    }
                },
                {
                    "name": "\u6613\u5c45\u4e2d\u56fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,28,97)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u4ee3\u62d3\u7075",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,132,127)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u57ce\u601d\u521b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,83,47)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,125,83)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u6f2b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,4,80)"
                        }
                    }
                },
                {
                    "name": "OSR",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,28,134)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8c61\u4f18\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,67,77)"
                        }
                    }
                },
                {
                    "name": "\u9b54\u98de\u7f51\u7edc-\u8f66\u8f7d\u5a31\u4e50",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,40,25)"
                        }
                    }
                },
                {
                    "name": "\u81f3\u771f\u4e92\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,98,84)"
                        }
                    }
                },
                {
                    "name": "\u9e3f\u6cf0\u9f0e\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,54,107)"
                        }
                    }
                },
                {
                    "name": "\u533b\u51c6\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,159,28)"
                        }
                    }
                },
                {
                    "name": "\u5e93\u73c0\u6052\u5b89",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,7,84)"
                        }
                    }
                },
                {
                    "name": "\u8ffd\u89c5\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,1,44)"
                        }
                    }
                },
                {
                    "name": "\u5706\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,12,160)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u64ad\u7535\u89c6\u7814\u7a76\u6240",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,59,77)"
                        }
                    }
                },
                {
                    "name": "\u90a6\u9f13\u601d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,58,155)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u8235\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,68,34)"
                        }
                    }
                },
                {
                    "name": "Sleepace \u4eab\u7761",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,25,16)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u7f19\u4f01\u4e1a\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,155,121)"
                        }
                    }
                },
                {
                    "name": "\u9c81\u73ed\u5ae1\u7cfb\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,4,59)"
                        }
                    }
                },
                {
                    "name": "\u6700\u53f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,54,119)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5f26\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,67,40)"
                        }
                    }
                },
                {
                    "name": "\u534e\u783a\u667a\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,59,108)"
                        }
                    }
                },
                {
                    "name": "\u67cf\u7f8e\u8fea\u5eb7\u4e0a\u6d77",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,139,9)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cfd\u667a\u4e91",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,80,135)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u516b\u7ef4\u7814\u4fee\u5b66\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,82,61)"
                        }
                    }
                },
                {
                    "name": "\u5341\u835f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,155,135)"
                        }
                    }
                },
                {
                    "name": "\u660e\u4e4b\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,120,15)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,4,48)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u777f\u89c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,76,11)"
                        }
                    }
                },
                {
                    "name": "\u827e\u8015\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,116,0)"
                        }
                    }
                },
                {
                    "name": "\u767e\u70bc\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,114,34)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u7075\u611f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,4,123)"
                        }
                    }
                },
                {
                    "name": "\u771f\u6e90\u6865\u4f01\u4e1a\u54a8\u8be2\uff08\u5317\u4eac\uff09\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,74,3)"
                        }
                    }
                },
                {
                    "name": "\u6c47\u4fe1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,32,95)"
                        }
                    }
                },
                {
                    "name": "\u5353\u671b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,93,52)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u7ec7\u7b97\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,116,72)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7535\u535a\u4e9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,43,134)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6c11\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,10,73)"
                        }
                    }
                },
                {
                    "name": "TalkingData",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,53,29)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u6444",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,11,48)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8702\u7a9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,40,33)"
                        }
                    }
                },
                {
                    "name": "\u5317\u660e\u6570\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,159,36)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4e13\u5bb6.COM",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,94,151)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u7280\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,115,20)"
                        }
                    }
                },
                {
                    "name": "\u6dd8\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,73,113)"
                        }
                    }
                },
                {
                    "name": "\u7279\u8c19\u65af\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,119,15)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,76,35)"
                        }
                    }
                },
                {
                    "name": "\u7ffc\u8bfe\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,88,136)"
                        }
                    }
                },
                {
                    "name": "\u6c85\u9038\u65b9\u8fbe\u7ba1\u7406\u54a8\u8be2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,152,9)"
                        }
                    }
                },
                {
                    "name": "\u8d5b\u5427\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,108,43)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u725b\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,157,32)"
                        }
                    }
                },
                {
                    "name": "\u79cd\u68a6\u5ba2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,88,42)"
                        }
                    }
                },
                {
                    "name": "\u770b\u623f\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,129,54)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u4e91\u6749",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,44,157)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u7280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,121,129)"
                        }
                    }
                },
                {
                    "name": "\u8d62\u706b\u866b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,97,128)"
                        }
                    }
                },
                {
                    "name": "\u540d\u7af9\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,18,3)"
                        }
                    }
                },
                {
                    "name": "\u7279\u65af\u62c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,65,16)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5fc5\u80dc\u4e92\u5a31\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,120,139)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u5927\u90fd\u5e02\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,50,86)"
                        }
                    }
                },
                {
                    "name": "\u683c\u5170\u4ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,54,41)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u91cd\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,28,88)"
                        }
                    }
                },
                {
                    "name": "\u9e70\u4e4b\u773c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,12,110)"
                        }
                    }
                },
                {
                    "name": "\u73af\u7403\u8f66\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,112,159)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u4f17\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,138,42)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6570\u667a\u82af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,118,31)"
                        }
                    }
                },
                {
                    "name": "\u7aef\u70c1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,66,64)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5a01\u8f6f\u4ef6\u80a1\u4efd\u6709\u9650\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,112,52)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5f99\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,26,96)"
                        }
                    }
                },
                {
                    "name": "\u6f2b\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,130,63)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77\u5594\u8da3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,13,102)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5370\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,47,73)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u90a6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,39,79)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd\u8086\u96f6\u8086",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,7,125)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u94f6\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,116,87)"
                        }
                    }
                },
                {
                    "name": "CraiditX",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,157,23)"
                        }
                    }
                },
                {
                    "name": "\u660e\u671d\u4e07\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,53,51)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4e91\u4e2d\u76db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,84,99)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u7eaa\u4f73\u7f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,4,155)"
                        }
                    }
                },
                {
                    "name": "\u8001\u864e\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,135,76)"
                        }
                    }
                },
                {
                    "name": "\u9876\u70b9\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,119,123)"
                        }
                    }
                },
                {
                    "name": "\u667a\u8d1d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,146,13)"
                        }
                    }
                },
                {
                    "name": "\u65b9\u76f4\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,49,18)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u777f\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,133,60)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u7ea7\u7329\u7329\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,42,113)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u8fbe\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,38,7)"
                        }
                    }
                },
                {
                    "name": "\u4e45\u90a6GOMO",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,146,105)"
                        }
                    }
                },
                {
                    "name": "\u638c\u95e8\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,44,157)"
                        }
                    }
                },
                {
                    "name": "\u548c\u7f8e\u4fe1\u606f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,116,58)"
                        }
                    }
                },
                {
                    "name": "OPENAILAB",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,90,5)"
                        }
                    }
                },
                {
                    "name": "Udesk\uff0d\u4f01\u4e1a\u7ea7\u667a\u80fd\u5ba2\u670d\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,25,132)"
                        }
                    }
                },
                {
                    "name": "\u5916\u7814\u5728\u7ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,136,44)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u5b89\u79df\u8d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,153,152)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u987f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,75,157)"
                        }
                    }
                },
                {
                    "name": "\u8054\u6613\u878dlinklogis",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,61,101)"
                        }
                    }
                },
                {
                    "name": "\u592a\u521d\u5f08\u5baa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,69,25)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u4e4e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,121,20)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79fb\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,9,139)"
                        }
                    }
                },
                {
                    "name": "\u9884\u7b56\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,56,56)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u79d1\u95fb\u6b4c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,97,0)"
                        }
                    }
                },
                {
                    "name": "\u667a\u878d\u4fe1\u8fbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,73,18)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u732b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,159,105)"
                        }
                    }
                },
                {
                    "name": "YY",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,21,134)"
                        }
                    }
                },
                {
                    "name": "\u878d\u6167\u91d1\u79d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,11,36)"
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
                "\u5e73\u5b89\u79d1\u6280",
                "Insta360\u5f71\u77f3",
                "\u6ef4\u6ef4",
                "\u9177\u72d7\u97f3\u4e50",
                "OPPO",
                "\u9177\u5bb6\u4e50",
                "\u6df1\u5ea6\u8d4b\u667a",
                "\u62fc\u591a\u591a"
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
        chart_0c0e85cbaf2e4421b6c12474cb6b26e8.setOption(option_0c0e85cbaf2e4421b6c12474cb6b26e8);
    </script>
                <div id="22e8e6ae4aec40ea84153e75b2e5f0d2" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_22e8e6ae4aec40ea84153e75b2e5f0d2 = echarts.init(
            document.getElementById('22e8e6ae4aec40ea84153e75b2e5f0d2'), 'white', {renderer: 'canvas'});
        var option_22e8e6ae4aec40ea84153e75b2e5f0d2 = {
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
                668,
                314,
                309,
                180,
                90,
                58,
                29,
                14,
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
                    "value": 668,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,83,115)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 314,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,31,39)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 309,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,114,97)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 180,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,4,30)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": 90,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,35,145)"
                        }
                    }
                },
                {
                    "name": "\u6210\u90fd",
                    "value": 58,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,119,93)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,142,153)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,148,45)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,10,139)"
                        }
                    }
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,138,67)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,91,77)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,139,79)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5b89",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,66,97)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9521",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,54,48)"
                        }
                    }
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,108,129)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,150,38)"
                        }
                    }
                },
                {
                    "name": "\u5408\u80a5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,137,15)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,11,4)"
                        }
                    }
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,150,12)"
                        }
                    }
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,145,103)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,121,90)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,60,93)"
                        }
                    }
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,140,96)"
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
                "\u82cf\u5dde",
                "\u5357\u4eac",
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
        chart_22e8e6ae4aec40ea84153e75b2e5f0d2.setOption(option_22e8e6ae4aec40ea84153e75b2e5f0d2);
    </script>
                <div id="068a663cdfa74deda80638d1e515dfef" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_068a663cdfa74deda80638d1e515dfef = echarts.init(
            document.getElementById('068a663cdfa74deda80638d1e515dfef'), 'white', {renderer: 'canvas'});
        var option_068a663cdfa74deda80638d1e515dfef = {
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
                    "value": 668,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 314,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 309,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 180,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 90,
                    "name": "\u5e7f\u5dde"
                },
                {
                    "value": 58,
                    "name": "\u6210\u90fd"
                },
                {
                    "value": 29,
                    "name": "\u6b66\u6c49"
                },
                {
                    "value": 14,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 10,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 10,
                    "name": "\u4f5b\u5c71"
                },
                {
                    "value": 8,
                    "name": "\u91cd\u5e86"
                },
                {
                    "value": 6,
                    "name": "\u957f\u6c99"
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
                    "value": 4,
                    "name": "\u53a6\u95e8"
                },
                {
                    "value": 4,
                    "name": "\u90d1\u5dde"
                },
                {
                    "value": 4,
                    "name": "\u5408\u80a5"
                },
                {
                    "value": 3,
                    "name": "\u73e0\u6d77"
                },
                {
                    "value": 2,
                    "name": "\u9752\u5c9b"
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
                    "name": "\u798f\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u6d4e\u5357"
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
        chart_068a663cdfa74deda80638d1e515dfef.setOption(option_068a663cdfa74deda80638d1e515dfef);
    </script>
                <div id="6fdd6eac8bd24413bd762882fbab9df2" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_6fdd6eac8bd24413bd762882fbab9df2 = echarts.init(
            document.getElementById('6fdd6eac8bd24413bd762882fbab9df2'), 'white', {renderer: 'canvas'});
            
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
    
        var option_6fdd6eac8bd24413bd762882fbab9df2 = {
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
                        668
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        314
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
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        180
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        90
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        58
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
                        14
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        10
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
                        8
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        6
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
                    "name": "\u53a6\u95e8",
                    "value": [
                        118.1,
                        24.46,
                        4
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
                        4
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
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
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
                    "name": "\u60e0\u5dde",
                    "value": [
                        114.4,
                        23.09,
                        2
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
                    "name": "\u6d4e\u5357",
                    "value": [
                        117,
                        36.65,
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
        chart_6fdd6eac8bd24413bd762882fbab9df2.setOption(option_6fdd6eac8bd24413bd762882fbab9df2);
    </script>
                <div id="b97d034c55824b6a88afccb5bbcd7fb6" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_b97d034c55824b6a88afccb5bbcd7fb6 = echarts.init(
            document.getElementById('b97d034c55824b6a88afccb5bbcd7fb6'), 'white', {renderer: 'canvas'});
        var option_b97d034c55824b6a88afccb5bbcd7fb6 = {
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
                184,
                144,
                129,
                42,
                42,
                40,
                39,
                36,
                36,
                35
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
                    "value": 184,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,10,66)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u533a",
                    "value": 144,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,148,125)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533a",
                    "value": 129,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,8,9)"
                        }
                    }
                },
                {
                    "name": "\u4f59\u676d\u533a",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,15,77)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed",
                    "value": 42,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,67,147)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u4e1c\u65b0\u2026",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,90,158)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5317\u65fa",
                    "value": 39,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,160,138)"
                        }
                    }
                },
                {
                    "name": "\u5b9d\u5b89\u533a",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,66,152)"
                        }
                    }
                },
                {
                    "name": "\u671b\u4eac",
                    "value": 36,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,72,132)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5173\u6751",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,137,148)"
                        }
                    }
                },
                {
                    "name": "\u95f5\u884c\u533a",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,66,46)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6c47\u533a",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,103,23)"
                        }
                    }
                },
                {
                    "name": "\u5f20\u6c5f",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,7,23)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9053\u53e3",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,115,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u533a",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,158,98)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530\u533a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,55,39)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56\u533a",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,91,11)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u4faf\u533a",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,17,26)"
                        }
                    }
                },
                {
                    "name": "\u8679\u53e3\u533a",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,96,143)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6eaa",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,121,61)"
                        }
                    }
                },
                {
                    "name": "\u8d8a\u79c0\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,105,33)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6c5f\u533a",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,84,3)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b81\u533a",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,127,151)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6885\u8def",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,74,157)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u533a",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,56,79)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u6625\u8def",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,16,131)"
                        }
                    }
                },
                {
                    "name": "\u6768\u6d66\u533a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,85,89)"
                        }
                    }
                },
                {
                    "name": "\u5927\u51b2",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,61,80)"
                        }
                    }
                },
                {
                    "name": "\u62f1\u5885\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,136,90)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u57ce\u533a",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,99,92)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6cb3",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,77)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e8c\u65d7",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,132,138)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5174\u533a",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,12,1)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u6e56\u65b0\u2026",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,55,87)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e\u65b0\u2026",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,49,62)"
                        }
                    }
                },
                {
                    "name": "\u666e\u9640\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,8,24)"
                        }
                    }
                },
                {
                    "name": "\u756a\u79ba\u533a",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,10,68)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5730",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,92,152)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u534e",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,127,15)"
                        }
                    }
                },
                {
                    "name": "\u987a\u5fb7\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,4,111)"
                        }
                    }
                },
                {
                    "name": "\u897f\u57ce\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,110,57)"
                        }
                    }
                },
                {
                    "name": "\u77f3\u666f\u5c71\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,87,89)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,136,17)"
                        }
                    }
                },
                {
                    "name": "\u677e\u6c5f\u533a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,62,67)"
                        }
                    }
                },
                {
                    "name": "\u5929\u5c71\u8def",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,86,35)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u6e7e",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,147,149)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u56ed\u2026",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,119,61)"
                        }
                    }
                },
                {
                    "name": "\u6d2a\u5c71\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,13,115)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6c99\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,112,27)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e09\u65d7",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,116,32)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u73e0\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,116,101)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u5bb6\u6c47",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,28,156)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u6d66\u533a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,123,83)"
                        }
                    }
                },
                {
                    "name": "\u9752\u6d66\u533a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,78,139)"
                        }
                    }
                },
                {
                    "name": "\u4ed3\u524d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,111,16)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5174",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,81,131)"
                        }
                    }
                },
                {
                    "name": "\u5927\u671b\u8def",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,95,56)"
                        }
                    }
                },
                {
                    "name": "\u5173\u5c71",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,73,115)"
                        }
                    }
                },
                {
                    "name": "\u897f\u6e56",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,123,112)"
                        }
                    }
                },
                {
                    "name": "\u5cb3\u9e93\u533a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,147,144)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c71\u5b50",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,138,44)"
                        }
                    }
                },
                {
                    "name": "\u6765\u5e7f\u8425",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,73,13)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9662\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,0,76)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e09\u8def",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,158,2)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,60,159)"
                        }
                    }
                },
                {
                    "name": "\u6d0b\u6cfe",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,159,72)"
                        }
                    }
                },
                {
                    "name": "\u56de\u9f99\u89c2",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,97,8)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,116,96)"
                        }
                    }
                },
                {
                    "name": "\u897f\u76f4\u95e8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,68,133)"
                        }
                    }
                },
                {
                    "name": "\u5317\u65b0\u6cfe",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,23,0)"
                        }
                    }
                },
                {
                    "name": "\u901a\u5dde\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,105,135)"
                        }
                    }
                },
                {
                    "name": "\u68e0\u4e0b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,94,18)"
                        }
                    }
                },
                {
                    "name": "\u7f57\u6e56\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,51,122)"
                        }
                    }
                },
                {
                    "name": "\u4e9a\u8fd0\u6751",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,143,66)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u4e2d\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,44,158)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6d77",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,121,4)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u58a9\u8def",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,83,43)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u57d4\u533a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,83,152)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u58a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,155,108)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u5c97\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,30,39)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,100,109)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u89d2\u573a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,140,39)"
                        }
                    }
                },
                {
                    "name": "\u56db\u60e0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,30,95)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6cb9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,83,59)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u8425",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,160,19)"
                        }
                    }
                },
                {
                    "name": "\u5609\u5b9a\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,28,141)"
                        }
                    }
                },
                {
                    "name": "\u6ee8\u6e56\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,133,49)"
                        }
                    }
                },
                {
                    "name": "\u660c\u5e73\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,18,120)"
                        }
                    }
                },
                {
                    "name": "\u9547\u5b81\u8def",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,63,106)"
                        }
                    }
                },
                {
                    "name": "\u5ef6\u5409",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,75,81)"
                        }
                    }
                },
                {
                    "name": "\u53e4\u8361",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,14,76)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u5173",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,8,106)"
                        }
                    }
                },
                {
                    "name": "\u601d\u660e\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,35,3)"
                        }
                    }
                },
                {
                    "name": "\u540e\u6d77",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,122,131)"
                        }
                    }
                },
                {
                    "name": "\u9759\u5b89\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,84,109)"
                        }
                    }
                },
                {
                    "name": "\u9526\u6c5f\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,139,16)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u6cb3\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,46,149)"
                        }
                    }
                },
                {
                    "name": "\u547c\u5bb6\u697c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,5,158)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u56fd\u95e8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,156,106)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e61",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,126,28)"
                        }
                    }
                },
                {
                    "name": "\u548c\u5e73\u91cc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,88,16)"
                        }
                    }
                },
                {
                    "name": "\u534e\u6f15",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,29,104)"
                        }
                    }
                },
                {
                    "name": "\u5f90\u6cfe",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,84,31)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5703",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,78,98)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5357",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,27,138)"
                        }
                    }
                },
                {
                    "name": "\u9999\u6d32\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,75,101)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u57ce\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,93,62)"
                        }
                    }
                },
                {
                    "name": "\u8427\u5c71\u533a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,74,149)"
                        }
                    }
                },
                {
                    "name": "\u71d5\u838e",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,98,124)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5916\u6ee9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,7,142)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,99,152)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6cc9\u9a7f\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,50,27)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u90ba\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,11,92)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u5c71",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,153,14)"
                        }
                    }
                },
                {
                    "name": "\u94b1\u5858\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,8,48)"
                        }
                    }
                },
                {
                    "name": "\u676d\u5dde",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,144,127)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u5916\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,133,150)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u968d\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,152,125)"
                        }
                    }
                },
                {
                    "name": "\u5149\u660e\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,38,137)"
                        }
                    }
                },
                {
                    "name": "\u592a\u9633\u5bab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,114,29)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5c71\u516c\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,65,61)"
                        }
                    }
                },
                {
                    "name": "\u7ea2\u5e99",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,21,25)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5858",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,34,57)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,63,58)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u5143\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,12,95)"
                        }
                    }
                },
                {
                    "name": "\u6885\u9647",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,53,65)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7891\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,116,159)"
                        }
                    }
                },
                {
                    "name": "\u6253\u6d66\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,63,69)"
                        }
                    }
                },
                {
                    "name": "\u9a6c\u8fde\u6d3c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,55,57)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5cb8\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,140,153)"
                        }
                    }
                },
                {
                    "name": "\u897f\u4e3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,141,35)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u95e8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,87,92)"
                        }
                    }
                },
                {
                    "name": "\u73e0\u6c5f\u65b0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,72,106)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,106,57)"
                        }
                    }
                },
                {
                    "name": "\u80dc\u6d66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,135,11)"
                        }
                    }
                },
                {
                    "name": "\u6797\u548c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,127,156)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u5b81\u8def",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,24,7)"
                        }
                    }
                },
                {
                    "name": "\u5317\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,133,124)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u4ead",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,85,33)"
                        }
                    }
                },
                {
                    "name": "\u897f\u82d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,63,61)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u798f\u5e84",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,21,62)"
                        }
                    }
                },
                {
                    "name": "\u5929\u6cb3\u57ce",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,137,30)"
                        }
                    }
                },
                {
                    "name": "\u673a\u6295\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,80,131)"
                        }
                    }
                },
                {
                    "name": "\u96e8\u82b1\u53f0\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,62,145)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u725b\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,23,26)"
                        }
                    }
                },
                {
                    "name": "\u9646\u5bb6\u5634",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,90,99)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u6cb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,21,135)"
                        }
                    }
                },
                {
                    "name": "\u60e0\u9633\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,81,131)"
                        }
                    }
                },
                {
                    "name": "\u671d\u5916",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,9,48)"
                        }
                    }
                },
                {
                    "name": "\u9152\u4ed9\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,32,151)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5b89",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,35,61)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6c34\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,32,29)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u6c34\u6865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,86,134)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5885\u6e56",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,12,2)"
                        }
                    }
                },
                {
                    "name": "\u65e0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,109,56)"
                        }
                    }
                },
                {
                    "name": "\u96c1\u5854\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,139,157)"
                        }
                    }
                },
                {
                    "name": "\u6e1d\u5317\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,99,68)"
                        }
                    }
                },
                {
                    "name": "\u4e07\u67f3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,130,122)"
                        }
                    }
                },
                {
                    "name": "\u6c5f\u590f\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,45,48)"
                        }
                    }
                },
                {
                    "name": "\u5929\u76ee\u5c71\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,66,132)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5934",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,145,27)"
                        }
                    }
                },
                {
                    "name": "\u5317\u4eac\u5927\u2026",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,35,22)"
                        }
                    }
                },
                {
                    "name": "\u5b98\u6d32",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,45,25)"
                        }
                    }
                },
                {
                    "name": "\u5357\u6d77\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,38,110)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u8857",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,137,14)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u53f0\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,62,143)"
                        }
                    }
                },
                {
                    "name": "\u911e\u5dde\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,94,16)"
                        }
                    }
                },
                {
                    "name": "\u5742\u7530",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,119,61)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u5357\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,74,33)"
                        }
                    }
                },
                {
                    "name": "\u9b4f\u516c\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,114,152)"
                        }
                    }
                },
                {
                    "name": "\u56db\u5b63\u9752",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,140,71)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,128,116)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,68,153)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u6ca7\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,62,105)"
                        }
                    }
                },
                {
                    "name": "\u6587\u4e00\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,36,52)"
                        }
                    }
                },
                {
                    "name": "\u534e\u4fa8\u57ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,151,20)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u53d1\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,21,26)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6986\u6811",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,62,120)"
                        }
                    }
                },
                {
                    "name": "\u6d66\u53e3\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,40,100)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,103,139)"
                        }
                    }
                },
                {
                    "name": "\u897f\u5173",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,86,28)"
                        }
                    }
                },
                {
                    "name": "\u987a\u4e49\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,32,88)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5434\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,4,112)"
                        }
                    }
                },
                {
                    "name": "\u6e2d\u5858",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,36,51)"
                        }
                    }
                },
                {
                    "name": "\u5357\u4eac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,57,127)"
                        }
                    }
                },
                {
                    "name": "\u822a\u7a7a\u6e2f\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,156,8)"
                        }
                    }
                },
                {
                    "name": "\u6816\u971e\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,95,139)"
                        }
                    }
                },
                {
                    "name": "\u8700\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,23,34)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5fb7\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,12,6)"
                        }
                    }
                },
                {
                    "name": "\u4e5d\u9f99\u5761\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,93,63)"
                        }
                    }
                },
                {
                    "name": "\u90d1\u4e1c\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,1,87)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u56ed\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,68,102)"
                        }
                    }
                },
                {
                    "name": "\u6b66\u6c49\u7ecf\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,49,2)"
                        }
                    }
                },
                {
                    "name": "\u5965\u4f53",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,115,101)"
                        }
                    }
                },
                {
                    "name": "\u5386\u57ce\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,140,24)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u56db",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,112,77)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u5dde\u5927\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,52,108)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u76f4\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,130,58)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u6167\u5bfa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,15,36)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u697c\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,104,6)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u6d41\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,78,87)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u5b9d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,85,14)"
                        }
                    }
                },
                {
                    "name": "\u6f58\u5bb6\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,101,89)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,102,149)"
                        }
                    }
                },
                {
                    "name": "\u6f4d\u574a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,159,101)"
                        }
                    }
                },
                {
                    "name": "\u5434\u6cfe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,6,17)"
                        }
                    }
                },
                {
                    "name": "\u5510\u9547",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,52,36)"
                        }
                    }
                },
                {
                    "name": "\u767d\u77f3\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,107,10)"
                        }
                    }
                },
                {
                    "name": "\u8398\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,50,153)"
                        }
                    }
                },
                {
                    "name": "\u9ec4\u5c9b\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,18,104)"
                        }
                    }
                },
                {
                    "name": "\u8700\u6c49\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,30,123)"
                        }
                    }
                },
                {
                    "name": "\u841d\u5c97\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,152,118)"
                        }
                    }
                },
                {
                    "name": "\u5357\u5c71\u533b\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,3,74)"
                        }
                    }
                },
                {
                    "name": "\u6797\u6821\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,82,105)"
                        }
                    }
                },
                {
                    "name": "\u5927\u77f3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,134,92)"
                        }
                    }
                },
                {
                    "name": "\u4ea6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,23,151)"
                        }
                    }
                },
                {
                    "name": "\u576a\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,99,8)"
                        }
                    }
                },
                {
                    "name": "\u957f\u6c99\u53bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,17,116)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u516c\u5e99",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,132,85)"
                        }
                    }
                },
                {
                    "name": "\u5de6\u5bb6\u5e84",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,10,17)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u7ad9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,40,40)"
                        }
                    }
                },
                {
                    "name": "\u5458\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,141,6)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,67,112)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u5c71\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,49,87)"
                        }
                    }
                },
                {
                    "name": "\u6ca3\u6e2d\u65b0\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,88,91)"
                        }
                    }
                },
                {
                    "name": "\u8679\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,155,48)"
                        }
                    }
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,92,138)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6e2f\u4e1c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,31,49)"
                        }
                    }
                },
                {
                    "name": "\u9f99\u6eaa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,74,40)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5bff\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,125,83)"
                        }
                    }
                },
                {
                    "name": "\u76d0\u7530\u533a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,34,54)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u534e\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,88,77)"
                        }
                    }
                },
                {
                    "name": "\u5c55\u89c8\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,95,3)"
                        }
                    }
                },
                {
                    "name": "\u78a7\u4e91\u793e\u2026",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,75,24)"
                        }
                    }
                },
                {
                    "name": "\u592a\u548c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,132,5)"
                        }
                    }
                },
                {
                    "name": "\u51bc\u6751",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,14,44)"
                        }
                    }
                },
                {
                    "name": "\u6a2a\u5c97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,109,153)"
                        }
                    }
                },
                {
                    "name": "\u5ba3\u6b66\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,72,96)"
                        }
                    }
                },
                {
                    "name": "\u5cad\u5357",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,42,10)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u7ed3\u6e56",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,12,151)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u5e7f\u6865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,143,153)"
                        }
                    }
                },
                {
                    "name": "\u7436\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,126,15)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d32",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,36,59)"
                        }
                    }
                },
                {
                    "name": "\u8096\u5bb6\u6cb3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,112,90)"
                        }
                    }
                },
                {
                    "name": "\u6f15\u5b9d\u8def",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,124,154)"
                        }
                    }
                },
                {
                    "name": "\u5e38\u8425",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,39,124)"
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
                "\u4f59\u676d\u533a",
                "\u79d1\u6280\u56ed",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u897f\u5317\u65fa",
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
        chart_b97d034c55824b6a88afccb5bbcd7fb6.setOption(option_b97d034c55824b6a88afccb5bbcd7fb6);
    </script>
                <div id="0d12b46f727f4072a6e115a910cfa99a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0d12b46f727f4072a6e115a910cfa99a = echarts.init(
            document.getElementById('0d12b46f727f4072a6e115a910cfa99a'), 'white', {renderer: 'canvas'});
        var option_0d12b46f727f4072a6e115a910cfa99a = {
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
                    "value": 184,
                    "name": "\u6d77\u6dc0\u533a"
                },
                {
                    "value": 144,
                    "name": "\u671d\u9633\u533a"
                },
                {
                    "value": 129,
                    "name": "\u5357\u5c71\u533a"
                },
                {
                    "value": 42,
                    "name": "\u4f59\u676d\u533a"
                },
                {
                    "value": 42,
                    "name": "\u79d1\u6280\u56ed"
                },
                {
                    "value": 40,
                    "name": "\u6d66\u4e1c\u65b0\u2026"
                },
                {
                    "value": 39,
                    "name": "\u897f\u5317\u65fa"
                },
                {
                    "value": 36,
                    "name": "\u5b9d\u5b89\u533a"
                },
                {
                    "value": 36,
                    "name": "\u671b\u4eac"
                },
                {
                    "value": 35,
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
                    "name": "\u5f20\u6c5f"
                },
                {
                    "value": 28,
                    "name": "\u4e94\u9053\u53e3"
                },
                {
                    "value": 27,
                    "name": "\u9ad8\u65b0\u533a"
                },
                {
                    "value": 26,
                    "name": "\u798f\u7530\u533a"
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
                    "name": "\u8679\u6885\u8def"
                },
                {
                    "value": 15,
                    "name": "\u5929\u6cb3\u533a"
                },
                {
                    "value": 14,
                    "name": "\u77e5\u6625\u8def"
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
                    "name": "\u957f\u6cb3"
                },
                {
                    "value": 11,
                    "name": "\u897f\u4e8c\u65d7"
                },
                {
                    "value": 11,
                    "name": "\u5927\u5174\u533a"
                },
                {
                    "value": 10,
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
                    "name": "\u756a\u79ba\u533a"
                },
                {
                    "value": 9,
                    "name": "\u4e0a\u5730"
                },
                {
                    "value": 9,
                    "name": "\u9f99\u534e"
                },
                {
                    "value": 8,
                    "name": "\u987a\u5fb7\u533a"
                },
                {
                    "value": 8,
                    "name": "\u897f\u57ce\u533a"
                },
                {
                    "value": 8,
                    "name": "\u77f3\u666f\u5c71\u2026"
                },
                {
                    "value": 8,
                    "name": "\u5317\u4eac"
                },
                {
                    "value": 8,
                    "name": "\u677e\u6c5f\u533a"
                },
                {
                    "value": 8,
                    "name": "\u5929\u5c71\u8def"
                },
                {
                    "value": 8,
                    "name": "\u6df1\u5733\u6e7e"
                },
                {
                    "value": 8,
                    "name": "\u5de5\u4e1a\u56ed\u2026"
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
                    "name": "\u897f\u4e09\u65d7"
                },
                {
                    "value": 7,
                    "name": "\u6d77\u73e0\u533a"
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
                    "name": "\u9752\u6d66\u533a"
                },
                {
                    "value": 6,
                    "name": "\u4ed3\u524d"
                },
                {
                    "value": 6,
                    "name": "\u897f\u5174"
                },
                {
                    "value": 6,
                    "name": "\u5927\u671b\u8def"
                },
                {
                    "value": 6,
                    "name": "\u5173\u5c71"
                },
                {
                    "value": 5,
                    "name": "\u897f\u6e56"
                },
                {
                    "value": 5,
                    "name": "\u5cb3\u9e93\u533a"
                },
                {
                    "value": 5,
                    "name": "\u5927\u5c71\u5b50"
                },
                {
                    "value": 5,
                    "name": "\u6765\u5e7f\u8425"
                },
                {
                    "value": 5,
                    "name": "\u5b66\u9662\u8def"
                },
                {
                    "value": 5,
                    "name": "\u6587\u4e09\u8def"
                },
                {
                    "value": 5,
                    "name": "\u6df1\u5733"
                },
                {
                    "value": 5,
                    "name": "\u6d0b\u6cfe"
                },
                {
                    "value": 4,
                    "name": "\u56de\u9f99\u89c2"
                },
                {
                    "value": 4,
                    "name": "\u4e0a\u6d77"
                },
                {
                    "value": 4,
                    "name": "\u897f\u76f4\u95e8"
                },
                {
                    "value": 4,
                    "name": "\u5317\u65b0\u6cfe"
                },
                {
                    "value": 4,
                    "name": "\u901a\u5dde\u533a"
                },
                {
                    "value": 4,
                    "name": "\u68e0\u4e0b"
                },
                {
                    "value": 4,
                    "name": "\u7f57\u6e56\u533a"
                },
                {
                    "value": 4,
                    "name": "\u4e9a\u8fd0\u6751"
                },
                {
                    "value": 4,
                    "name": "\u6e1d\u4e2d\u533a"
                },
                {
                    "value": 4,
                    "name": "\u524d\u6d77"
                },
                {
                    "value": 4,
                    "name": "\u53e4\u58a9\u8def"
                },
                {
                    "value": 4,
                    "name": "\u9ec4\u57d4\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e09\u58a9"
                },
                {
                    "value": 3,
                    "name": "\u9f99\u5c97\u533a"
                },
                {
                    "value": 3,
                    "name": "\u65b0\u6e2f"
                },
                {
                    "value": 3,
                    "name": "\u4e94\u89d2\u573a"
                },
                {
                    "value": 3,
                    "name": "\u56db\u60e0"
                },
                {
                    "value": 3,
                    "name": "\u5357\u6cb9"
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
                    "name": "\u6ee8\u6e56\u533a"
                },
                {
                    "value": 3,
                    "name": "\u660c\u5e73\u533a"
                },
                {
                    "value": 3,
                    "name": "\u9547\u5b81\u8def"
                },
                {
                    "value": 3,
                    "name": "\u5ef6\u5409"
                },
                {
                    "value": 3,
                    "name": "\u53e4\u8361"
                },
                {
                    "value": 3,
                    "name": "\u5c0f\u5173"
                },
                {
                    "value": 3,
                    "name": "\u601d\u660e\u533a"
                },
                {
                    "value": 3,
                    "name": "\u540e\u6d77"
                },
                {
                    "value": 3,
                    "name": "\u9759\u5b89\u533a"
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
                    "name": "\u547c\u5bb6\u697c"
                },
                {
                    "value": 3,
                    "name": "\u5efa\u56fd\u95e8"
                },
                {
                    "value": 3,
                    "name": "\u897f\u4e61"
                },
                {
                    "value": 3,
                    "name": "\u548c\u5e73\u91cc"
                },
                {
                    "value": 3,
                    "name": "\u534e\u6f15"
                },
                {
                    "value": 3,
                    "name": "\u5f90\u6cfe"
                },
                {
                    "value": 3,
                    "name": "\u4e1c\u5703"
                },
                {
                    "value": 3,
                    "name": "\u6c5f\u5357"
                },
                {
                    "value": 3,
                    "name": "\u9999\u6d32\u533a"
                },
                {
                    "value": 3,
                    "name": "\u4e0b\u57ce\u533a"
                },
                {
                    "value": 3,
                    "name": "\u8427\u5c71\u533a"
                },
                {
                    "value": 3,
                    "name": "\u71d5\u838e"
                },
                {
                    "value": 3,
                    "name": "\u5317\u5916\u6ee9"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u65b0\u6280\u2026"
                },
                {
                    "value": 2,
                    "name": "\u9f99\u6cc9\u9a7f\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u90ba\u533a"
                },
                {
                    "value": 2,
                    "name": "\u4e94\u5c71"
                },
                {
                    "value": 2,
                    "name": "\u94b1\u5858\u533a"
                },
                {
                    "value": 2,
                    "name": "\u676d\u5dde"
                },
                {
                    "value": 2,
                    "name": "\u5efa\u5916\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u57ce\u968d\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u5149\u660e\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u592a\u9633\u5bab"
                },
                {
                    "value": 2,
                    "name": "\u4e2d\u5c71\u516c\u2026"
                },
                {
                    "value": 2,
                    "name": "\u7ea2\u5e99"
                },
                {
                    "value": 2,
                    "name": "\u4e0a\u5858"
                },
                {
                    "value": 2,
                    "name": "\u576a\u5c71\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u4e09\u5143\u6865"
                },
                {
                    "value": 2,
                    "name": "\u6885\u9647"
                },
                {
                    "value": 2,
                    "name": "\u9ad8\u7891\u5e97"
                },
                {
                    "value": 2,
                    "name": "\u6253\u6d66\u6865"
                },
                {
                    "value": 2,
                    "name": "\u9a6c\u8fde\u6d3c"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5cb8\u533a"
                },
                {
                    "value": 2,
                    "name": "\u897f\u4e3d"
                },
                {
                    "value": 2,
                    "name": "\u671d\u9633\u95e8"
                },
                {
                    "value": 2,
                    "name": "\u73e0\u6c5f\u65b0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u6d66\u6cbf"
                },
                {
                    "value": 2,
                    "name": "\u80dc\u6d66"
                },
                {
                    "value": 2,
                    "name": "\u6797\u548c"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u5b81\u8def"
                },
                {
                    "value": 2,
                    "name": "\u5317\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5b89\u4ead"
                },
                {
                    "value": 2,
                    "name": "\u897f\u82d1"
                },
                {
                    "value": 2,
                    "name": "\u5b9a\u798f\u5e84"
                },
                {
                    "value": 2,
                    "name": "\u5929\u6cb3\u57ce"
                },
                {
                    "value": 2,
                    "name": "\u673a\u6295\u6865"
                },
                {
                    "value": 2,
                    "name": "\u96e8\u82b1\u53f0\u2026"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u725b\u533a"
                },
                {
                    "value": 2,
                    "name": "\u9646\u5bb6\u5634"
                },
                {
                    "value": 2,
                    "name": "\u6e05\u6cb3"
                },
                {
                    "value": 2,
                    "name": "\u60e0\u9633\u533a"
                },
                {
                    "value": 2,
                    "name": "\u671d\u5916"
                },
                {
                    "value": 2,
                    "name": "\u9152\u4ed9\u6865"
                },
                {
                    "value": 2,
                    "name": "\u65b0\u5b89"
                },
                {
                    "value": 2,
                    "name": "\u91d1\u6c34\u533a"
                },
                {
                    "value": 2,
                    "name": "\u7acb\u6c34\u6865"
                },
                {
                    "value": 2,
                    "name": "\u72ec\u5885\u6e56"
                },
                {
                    "value": 2,
                    "name": "\u65e0"
                },
                {
                    "value": 2,
                    "name": "\u96c1\u5854\u533a"
                },
                {
                    "value": 2,
                    "name": "\u6e1d\u5317\u533a"
                },
                {
                    "value": 2,
                    "name": "\u4e07\u67f3"
                },
                {
                    "value": 2,
                    "name": "\u6c5f\u590f\u533a"
                },
                {
                    "value": 2,
                    "name": "\u5929\u76ee\u5c71\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5357\u5934"
                },
                {
                    "value": 2,
                    "name": "\u5317\u4eac\u5927\u2026"
                },
                {
                    "value": 2,
                    "name": "\u5b98\u6d32"
                },
                {
                    "value": 2,
                    "name": "\u5357\u6d77\u533a"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u878d\u8857"
                },
                {
                    "value": 1,
                    "name": "\u4e30\u53f0\u533a"
                },
                {
                    "value": 1,
                    "name": "\u911e\u5dde\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5742\u7530"
                },
                {
                    "value": 1,
                    "name": "\u5e02\u5357\u533a"
                },
                {
                    "value": 1,
                    "name": "\u9b4f\u516c\u6751"
                },
                {
                    "value": 1,
                    "name": "\u56db\u5b63\u9752"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u5c0f\u884c"
                },
                {
                    "value": 1,
                    "name": "\u6d77\u6ca7\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6587\u4e00\u8def"
                },
                {
                    "value": 1,
                    "name": "\u534e\u4fa8\u57ce"
                },
                {
                    "value": 1,
                    "name": "\u5f00\u53d1\u533a"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6986\u6811"
                },
                {
                    "value": 1,
                    "name": "\u6d66\u53e3\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4eba\u548c"
                },
                {
                    "value": 1,
                    "name": "\u897f\u5173"
                },
                {
                    "value": 1,
                    "name": "\u987a\u4e49\u533a"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u5434\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6e2d\u5858"
                },
                {
                    "value": 1,
                    "name": "\u5357\u4eac"
                },
                {
                    "value": 1,
                    "name": "\u822a\u7a7a\u6e2f\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6816\u971e\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8700\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5b89\u5fb7\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u4e5d\u9f99\u5761\u2026"
                },
                {
                    "value": 1,
                    "name": "\u90d1\u4e1c\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u79d1\u6280\u56ed\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6b66\u6c49\u7ecf\u2026"
                },
                {
                    "value": 1,
                    "name": "\u5965\u4f53"
                },
                {
                    "value": 1,
                    "name": "\u5386\u57ce\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u56db"
                },
                {
                    "value": 1,
                    "name": "\u5e7f\u5dde\u5927\u2026"
                },
                {
                    "value": 1,
                    "name": "\u4e1c\u76f4\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u5b9a\u6167\u5bfa"
                },
                {
                    "value": 1,
                    "name": "\u9f13\u697c\u533a"
                },
                {
                    "value": 1,
                    "name": "\u53cc\u6d41\u533a"
                },
                {
                    "value": 1,
                    "name": "\u4e03\u5b9d"
                },
                {
                    "value": 1,
                    "name": "\u6f58\u5bb6\u56ed"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u6865"
                },
                {
                    "value": 1,
                    "name": "\u6f4d\u574a"
                },
                {
                    "value": 1,
                    "name": "\u5434\u6cfe"
                },
                {
                    "value": 1,
                    "name": "\u5510\u9547"
                },
                {
                    "value": 1,
                    "name": "\u767d\u77f3\u6865"
                },
                {
                    "value": 1,
                    "name": "\u8398\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u9ec4\u5c9b\u533a"
                },
                {
                    "value": 1,
                    "name": "\u8700\u6c49\u8def"
                },
                {
                    "value": 1,
                    "name": "\u841d\u5c97\u533a"
                },
                {
                    "value": 1,
                    "name": "\u5357\u5c71\u533b\u2026"
                },
                {
                    "value": 1,
                    "name": "\u6797\u6821\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5927\u77f3"
                },
                {
                    "value": 1,
                    "name": "\u4ea6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u576a\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u957f\u6c99\u53bf"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u516c\u5e99"
                },
                {
                    "value": 1,
                    "name": "\u5de6\u5bb6\u5e84"
                },
                {
                    "value": 1,
                    "name": "\u8f66\u7ad9"
                },
                {
                    "value": 1,
                    "name": "\u5458\u6751"
                },
                {
                    "value": 1,
                    "name": "\u5e73\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u91d1\u5c71\u533a"
                },
                {
                    "value": 1,
                    "name": "\u6ca3\u6e2d\u65b0\u2026"
                },
                {
                    "value": 1,
                    "name": "\u8679\u6865"
                },
                {
                    "value": 1,
                    "name": "\u82cf\u5dde"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6e2f\u4e1c"
                },
                {
                    "value": 1,
                    "name": "\u9f99\u6eaa"
                },
                {
                    "value": 1,
                    "name": "\u957f\u5bff\u8def"
                },
                {
                    "value": 1,
                    "name": "\u76d0\u7530\u533a"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u534e\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5c55\u89c8\u8def"
                },
                {
                    "value": 1,
                    "name": "\u78a7\u4e91\u793e\u2026"
                },
                {
                    "value": 1,
                    "name": "\u592a\u548c"
                },
                {
                    "value": 1,
                    "name": "\u51bc\u6751"
                },
                {
                    "value": 1,
                    "name": "\u6a2a\u5c97"
                },
                {
                    "value": 1,
                    "name": "\u5ba3\u6b66\u95e8"
                },
                {
                    "value": 1,
                    "name": "\u5cad\u5357"
                },
                {
                    "value": 1,
                    "name": "\u56e2\u7ed3\u6e56"
                },
                {
                    "value": 1,
                    "name": "\u4eac\u5e7f\u6865"
                },
                {
                    "value": 1,
                    "name": "\u7436\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u65b0\u6d32"
                },
                {
                    "value": 1,
                    "name": "\u8096\u5bb6\u6cb3"
                },
                {
                    "value": 1,
                    "name": "\u6f15\u5b9d\u8def"
                },
                {
                    "value": 1,
                    "name": "\u5e38\u8425"
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
        chart_0d12b46f727f4072a6e115a910cfa99a.setOption(option_0d12b46f727f4072a6e115a910cfa99a);
    </script>
                <div id="829f320011864ac69fef045f368fc9ed" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_829f320011864ac69fef045f368fc9ed = echarts.init(
            document.getElementById('829f320011864ac69fef045f368fc9ed'), 'white', {renderer: 'canvas'});
        var option_829f320011864ac69fef045f368fc9ed = {
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
                437,
                348,
                221,
                194,
                172,
                141,
                124,
                91
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
                    "value": 437
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 348
                },
                {
                    "name": "A\u8f6e",
                    "value": 221
                },
                {
                    "name": "B\u8f6e",
                    "value": 194
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 172
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 141
                },
                {
                    "name": "C\u8f6e",
                    "value": 124
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 91
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
                    "value": 437
                },
                {
                    "name": "\u4e0d\u9700\u8981\u878d\u8d44",
                    "value": 348
                },
                {
                    "name": "A\u8f6e",
                    "value": 221
                },
                {
                    "name": "B\u8f6e",
                    "value": 194
                },
                {
                    "name": "D\u8f6e\u53ca\u4ee5\u4e0a",
                    "value": 172
                },
                {
                    "name": "\u672a\u878d\u8d44",
                    "value": 141
                },
                {
                    "name": "C\u8f6e",
                    "value": 124
                },
                {
                    "name": "\u5929\u4f7f\u8f6e",
                    "value": 91
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
        chart_829f320011864ac69fef045f368fc9ed.setOption(option_829f320011864ac69fef045f368fc9ed);
    </script>
                <div id="e956a72f6a904fc7a8ccb87142e5dc14" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_e956a72f6a904fc7a8ccb87142e5dc14 = echarts.init(
            document.getElementById('e956a72f6a904fc7a8ccb87142e5dc14'), 'white', {renderer: 'canvas'});
        var option_e956a72f6a904fc7a8ccb87142e5dc14 = {
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
                499,
                377,
                325,
                316,
                182,
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
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "2000\u4eba\u4ee5\u4e0a",
                    "value": 499
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 377
                },
                {
                    "name": "50-150\u4eba",
                    "value": 325
                },
                {
                    "name": "150-500\u4eba",
                    "value": 316
                },
                {
                    "name": "15-50\u4eba",
                    "value": 182
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 29
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
                    "value": 499
                },
                {
                    "name": "500-2000\u4eba",
                    "value": 377
                },
                {
                    "name": "50-150\u4eba",
                    "value": 325
                },
                {
                    "name": "150-500\u4eba",
                    "value": 316
                },
                {
                    "name": "15-50\u4eba",
                    "value": 182
                },
                {
                    "name": "\u5c11\u4e8e15\u4eba",
                    "value": 29
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
        chart_e956a72f6a904fc7a8ccb87142e5dc14.setOption(option_e956a72f6a904fc7a8ccb87142e5dc14);
    </script>
                <div id="c0f07fe394c14b8a9de090f645cee18b" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_c0f07fe394c14b8a9de090f645cee18b = echarts.init(
            document.getElementById('c0f07fe394c14b8a9de090f645cee18b'), 'white', {renderer: 'canvas'});
        var option_c0f07fe394c14b8a9de090f645cee18b = {
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
                554,
                317,
                198,
                196,
                165,
                129,
                100
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
                    "value": 554,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,66,49)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                    "value": 317,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,42,117)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u670d\u52a1",
                    "value": 198,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,141,93)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u670d\u52a1",
                    "value": 196,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,131,111)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 165,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,42,10)"
                        }
                    }
                },
                {
                    "name": "IT\u6280\u672f\u670d\u52a1",
                    "value": 129,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,11,145)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u91d1\u878d",
                    "value": 100,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,104,91)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                    "value": 94,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,149,73)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u8d44\u8baf",
                    "value": 84,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,152,40)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u4e92\u8054\u7f51",
                    "value": 79,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,57,58)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5e73\u53f0",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,69,10)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 76,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,109,113)"
                        }
                    }
                },
                {
                    "name": "\u77ed\u89c6\u9891",
                    "value": 67,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,54,100)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5a92\u4f53",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,83,137)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,110,62)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891",
                    "value": 60,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,54,159)"
                        }
                    }
                },
                {
                    "name": "\u6d88\u8d39\u751f\u6d3b",
                    "value": 59,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,44,121)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u670d\u52a1",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,0,1)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f",
                    "value": 56,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,150,2)"
                        }
                    }
                },
                {
                    "name": "\u5176\u4ed6",
                    "value": 53,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,113,34)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u6559\u80b2",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,83,115)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5e73\u53f0",
                    "value": 52,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,147,55)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u670d\u52a1",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,96,90)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u793e\u533a",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,116,100)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 35,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,48,105)"
                        }
                    }
                },
                {
                    "name": "\u8425\u9500\u670d\u52a1",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,34,65)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u884c",
                    "value": 34,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,145,96)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4\u5a92\u4f53",
                    "value": 32,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,117,107)"
                        }
                    }
                },
                {
                    "name": "\u5728\u7ebf\u533b\u7597",
                    "value": 30,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,123,29)"
                        }
                    }
                },
                {
                    "name": "\u5236\u9020\u4e1a",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,55,10)"
                        }
                    }
                },
                {
                    "name": "\u786c\u4ef6",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,55,84)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u4e1a",
                    "value": 26,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,41,66)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,98,20)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u4e28\u5065\u5eb7",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,86,75)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,145,141)"
                        }
                    }
                },
                {
                    "name": "\u5c45\u4f4f\u670d\u52a1",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,151,24)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u68c0\u7d22",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,70,58)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,65,9)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,157,72)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5e73\u53f0",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,5,68)"
                        }
                    }
                },
                {
                    "name": "MCN",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,23,110)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,151,140)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u901a\u4fe1",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,32,109)"
                        }
                    }
                },
                {
                    "name": "\u751f\u6d3b\u670d\u52a1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,53,68)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,148,38)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5065",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,92,105)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u5bb9",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,154,70)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,156,72)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u8f93",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,93,65)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,133,57)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,112,81)"
                        }
                    }
                },
                {
                    "name": "\u8d38\u6613",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,94,65)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,88,116)"
                        }
                    }
                },
                {
                    "name": "\u8fdb\u51fa\u53e3",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,108,110)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4ea4\u6613\u5e73\u53f0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,69,98)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5a31\u4e28\u5185\u5bb9",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,78,13)"
                        }
                    }
                },
                {
                    "name": "\u6279\u53d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,13,68)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4ea4",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,72,56)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u4e28\u8fd0\u8f93",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,7,16)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u552e",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,136,54)"
                        }
                    }
                },
                {
                    "name": "\u5efa\u7b51",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,142,100)"
                        }
                    }
                },
                {
                    "name": "\u623f\u5730\u4ea7",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,57,60)"
                        }
                    }
                },
                {
                    "name": "\u7269\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,128,85)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u9650",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,113,152)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u80fd\u6e90\u6c7d\u8f66\u5236\u9020",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,58,9)"
                        }
                    }
                },
                {
                    "name": "\u4f11\u95f2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,1,16)"
                        }
                    }
                },
                {
                    "name": "\u77ff\u4ea7",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,60,14)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,14,68)"
                        }
                    }
                },
                {
                    "name": "\u80fd\u6e90",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,88,110)"
                        }
                    }
                },
                {
                    "name": "\u5a31\u4e50",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,5,74)"
                        }
                    }
                },
                {
                    "name": "\u73af\u4fdd",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,9,54)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41\u5e73\u53f0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,30,95)"
                        }
                    }
                },
                {
                    "name": "\u5f71\u89c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,123,147)"
                        }
                    }
                },
                {
                    "name": "\u52a8\u6f2b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,13,133)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u4f20\u5a92",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,66,43)"
                        }
                    }
                },
                {
                    "name": "\u6c7d\u8f66\u4e28\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,9,139)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u3001\u8f6f\u4ef6\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,91,33)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,23,67)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6\u5f00\u53d1\u3001\u4eba\u5de5\u667a\u80fd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,110,46)"
                        }
                    }
                },
                {
                    "name": "\u519c\u6797\u7267\u6e14",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,99,14)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u5177",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,120,160)"
                        }
                    }
                },
                {
                    "name": "\u623f\u4ea7\u5bb6\u5c45",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,55,99)"
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
                "\u6570\u636e\u670d\u52a1",
                "\u8f6f\u4ef6\u670d\u52a1",
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
        chart_c0f07fe394c14b8a9de090f645cee18b.setOption(option_c0f07fe394c14b8a9de090f645cee18b);
    </script>
                <div id="4f9e455d3f674f10a4c3cd9e317c3ae4" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_4f9e455d3f674f10a4c3cd9e317c3ae4 = echarts.init(
            document.getElementById('4f9e455d3f674f10a4c3cd9e317c3ae4'), 'white', {renderer: 'canvas'});
        var option_4f9e455d3f674f10a4c3cd9e317c3ae4 = {
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
                481,
                106,
                89,
                51,
                51,
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
                    "value": 481,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,60,130)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 106,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,127,113)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 89,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,33,103)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,8,53)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 51,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,53,128)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u7b97\u6cd5",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,128,110)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,128,7)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,131,98)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,151,136)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,1,81)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u7b97\u6cd5",
                    "value": 21,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,3,148)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b97\u6cd5",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,154,130)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,65,64)"
                        }
                    }
                },
                {
                    "name": "ai\u7b97\u6cd5",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,39,80)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u9891\u7b97\u6cd5",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,14,84)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,26,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,99,103)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,7,125)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u7b97\u6cd5",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,7,14)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,85,59)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u8bc6\u522b\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,149,46)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b97\u6cd5",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,29,129)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,66,66)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,27,72)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u7b97\u6cd5",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,115,93)"
                        }
                    }
                },
                {
                    "name": "\u63a7\u5236\u7b97\u6cd5",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,146,79)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,116,101)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,40,7)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,62,147)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,60,105)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,123,46)"
                        }
                    }
                },
                {
                    "name": "SLAM\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,160,68)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,94,64)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7AI\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,39,147)"
                        }
                    }
                },
                {
                    "name": "\u51e0\u4f55\u7b97\u6cd5",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,79,77)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406 \u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,85,117)"
                        }
                    }
                },
                {
                    "name": "ocr\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,61,76)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u56fe\u50cf\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,117,63)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u822a\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,149,133)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,143,89)"
                        }
                    }
                },
                {
                    "name": "\u521d\u7ea7\u7b97\u6cd5",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,110,18)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u611f\u77e5\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,149,76)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,147,96)"
                        }
                    }
                },
                {
                    "name": "CV\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,23,157)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u5408\u6210\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,15,4)"
                        }
                    }
                },
                {
                    "name": "\u7c7b\u8111\u667a\u80fd\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,35,9)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,2,3)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5316\u5b66\u4e60\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,46,104)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,22,18)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u89c4\u5212\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,18,39)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,79,59)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u5e7f\u544a\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,151,150)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,50,122)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,44,137)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,143,40)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u63a7\u5236\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,49,149)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2-\u63a8\u8350\u641c\u7d22\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,28,97)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u589e\u957f\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,107,133)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,13,112)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,1,115)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,39,80)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u4f18\u5316\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,149,159)"
                        }
                    }
                },
                {
                    "name": "\u901a\u4fe1\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,54,75)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u7801\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,13,9)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,106,42)"
                        }
                    }
                },
                {
                    "name": "SK6563-PTBU-\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,21,10)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,110,49)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6691\u5047\u5b9e\u4e60\u751f\u3011\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,154,52)"
                        }
                    }
                },
                {
                    "name": "DSP\u5e7f\u544a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,140,9)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u8c61\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,94,63)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6570\u636e\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,75,49)"
                        }
                    }
                },
                {
                    "name": "\u5171\u8bc6\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,41,118)"
                        }
                    }
                },
                {
                    "name": "\u7b56\u7565\u67b6\u6784\u7814\u53d1\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,145,94)"
                        }
                    }
                },
                {
                    "name": "\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,87,115)"
                        }
                    }
                },
                {
                    "name": "GNSS\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,1,15)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,63,133)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,94,151)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,18,152)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u63a7\u5236\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,156,37)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u53cd\u6b3a\u8bc8\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,74,74)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7cbe\u5730\u56fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,90,152)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u5e08\\\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,127,91)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60/\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,42,136)"
                        }
                    }
                },
                {
                    "name": "\u6210\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,34,136)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u97f3\u9891\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,71,127)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,140,44)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u3001\u56fe\u50cf\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,19,1)"
                        }
                    }
                },
                {
                    "name": "AI \u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,43,159)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u722c\u866b\u7b56\u7565\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,20,75)"
                        }
                    }
                },
                {
                    "name": "GJ2127-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,108,61)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5546\u54c1\u641c\u7d22\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,102,22)"
                        }
                    }
                },
                {
                    "name": "\u9884\u6d4b\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,22,85)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,77,94)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u4ea4\u6613\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,131,121)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7b79\u5b66\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,2,43)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,41,145)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u5bfc\u822a\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,119,43)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,66,65)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,15,46)"
                        }
                    }
                },
                {
                    "name": "25317O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,120,71)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u4e09\u7ef4\u9ad8\u7cbe\u5efa\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,29,156)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,15,121)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,159,50)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,15,153)"
                        }
                    }
                },
                {
                    "name": "AF\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,127,109)"
                        }
                    }
                },
                {
                    "name": "00233-\u5d4c\u5165\u5f0f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,116,73)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,147,115)"
                        }
                    }
                },
                {
                    "name": "SJY-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,30,55)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,147,104)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,30,94)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,35,1)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,42,152)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,39,128)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,51,90)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u68c0\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,101,25)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u68c0\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,93,39)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,32,139)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,72,151)"
                        }
                    }
                },
                {
                    "name": "\u5a92\u4f53\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,62,90)"
                        }
                    }
                },
                {
                    "name": "29912-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,130,64)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u4f53\u9a8c\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,14,119)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,75,88)"
                        }
                    }
                },
                {
                    "name": "3D \u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,120,160)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60/\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,105,142)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u5e73\u53f0-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,15,115)"
                        }
                    }
                },
                {
                    "name": "PCG09-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,26,25)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u641c\u7d22-\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,39,53)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,66,104)"
                        }
                    }
                },
                {
                    "name": "\u5185\u5bb9\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,87,153)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u6280\u672f\u5e73\u53f0\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,71,82)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,149,154)"
                        }
                    }
                },
                {
                    "name": "\u5546\u54c1\u7ecf\u8425\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,81,129)"
                        }
                    }
                },
                {
                    "name": "\u5b89\u5168\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,33,151)"
                        }
                    }
                },
                {
                    "name": "AI\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,27,124)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,52,30)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,44,50)"
                        }
                    }
                },
                {
                    "name": "11122N-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,78,37)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,104,97)"
                        }
                    }
                },
                {
                    "name": "SLAM/VIO/\u4e09\u7ef4\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,84,109)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u7ed3\u6784\u5316\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,148,72)"
                        }
                    }
                },
                {
                    "name": "\u91cf\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,156,74)"
                        }
                    }
                },
                {
                    "name": "SJY-\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,28,24)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,140,96)"
                        }
                    }
                },
                {
                    "name": "55413P-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,79,104)"
                        }
                    }
                },
                {
                    "name": "024168-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,138,152)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,68,155)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u624b\u5199\u8bc6\u522b-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,59,35)"
                        }
                    }
                },
                {
                    "name": "\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,109,58)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u5e7f\u544a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,88,77)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,46,41)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,9,111)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u9a91\u884c-\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,9,43)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,31,21)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u4eba\u4f53/\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,70,53)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,131,64)"
                        }
                    }
                },
                {
                    "name": "\u7ec4\u5408\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,42,4)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,157,90)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,117,27)"
                        }
                    }
                },
                {
                    "name": "\u5730\u56fe\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,85,119)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,92,107)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,132,8)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7d27\u6025\u5c97\u4f4d\u3011\u301095\u5206\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,86,60)"
                        }
                    }
                },
                {
                    "name": "AIOPs\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,150,94)"
                        }
                    }
                },
                {
                    "name": "324121-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,78,135)"
                        }
                    }
                },
                {
                    "name": "114114-\u9ad8\u7ea7/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,134,66)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,97,86)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u5de5\u7a0b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,115,111)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7ade\u4ef7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,38,160)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,12,58)"
                        }
                    }
                },
                {
                    "name": "00239-\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,111,160)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,46,72)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u603b\u76d1\uff08\u5927\u6570\u636e/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,81,30)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5f81\u4fe1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,138,42)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u5bfc\u822a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,148,49)"
                        }
                    }
                },
                {
                    "name": "11122M-LT-311-\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,109,82)"
                        }
                    }
                },
                {
                    "name": "Algorithm Engineer \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,133,91)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf/\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,6,124)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996eSaaS\u6280\u672f\u90e8-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,124,10)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u9a7e\u9a76\u5b9a\u4f4d\u4e0e\u5730\u56fe\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,18,124)"
                        }
                    }
                },
                {
                    "name": "\u8f68\u8ff9\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,46,56)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,36,50)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,18,138)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5de5\u7a0b\u5e08-\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,149,16)"
                        }
                    }
                },
                {
                    "name": "\u3010\u4e0a\u6d77\u677e\u6c5f\u533a\u3011\u6545\u969c\u9884\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,126,140)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8bed\u97f3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,124,96)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6a21\u578b\u5de5\u7a0b\u5e08\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,108,143)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,46,153)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08/AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,16,106)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u7edc\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,114,40)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u52a8\u5065\u5eb7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,116,113)"
                        }
                    }
                },
                {
                    "name": "CG8005-SPBU-3D\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,105,113)"
                        }
                    }
                },
                {
                    "name": "\u8ba1\u7b97\u673a\u89c6\u89c9\uff083D\u65b9\u5411\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,131,38)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,45,18)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u6392\u5e8f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,151,121)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5149\u8c31\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,110,99)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,114,129)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u611f\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,153,97)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,142,124)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u4e0e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,6,20)"
                        }
                    }
                },
                {
                    "name": "11318V-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,158,129)"
                        }
                    }
                },
                {
                    "name": "TTS\u8bed\u97f3\u5408\u6210\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,150,100)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe-SLAM\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,100,107)"
                        }
                    }
                },
                {
                    "name": "0232KT-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,130,144)"
                        }
                    }
                },
                {
                    "name": "\u3010\u7f8e\u56e2\u4f18\u9009\u3011-\u8425\u9500\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,92,100)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,87,160)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u533b\u7597\u641c\u7d22-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,120,132)"
                        }
                    }
                },
                {
                    "name": "FF2824-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,7,132)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,71,122)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22/\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,15,7)"
                        }
                    }
                },
                {
                    "name": "113154-\u8d44\u6df1/\u4e13\u5bb6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,42,95)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,13,68)"
                        }
                    }
                },
                {
                    "name": "00206-NLP\u9ad8\u7ea7\u5de5\u7a0b\u5e08/\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,15,82)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5f00\u53d1/unity/\u6d4b\u8bd5/\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,153,124)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,12,10)"
                        }
                    }
                },
                {
                    "name": "VU1966-SPBU-AI\u5de5\u7a0b\u5316\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,110,135)"
                        }
                    }
                },
                {
                    "name": "2D/3D\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,135,109)"
                        }
                    }
                },
                {
                    "name": "25318B-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,53,81)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u7ffb\u8bd1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,159,40)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u4f533D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,82,114)"
                        }
                    }
                },
                {
                    "name": "55413O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,86,41)"
                        }
                    }
                },
                {
                    "name": "nlp/cv \u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,90,140)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u8f86\u52a8\u529b\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,55,119)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6df1\u5733\u3011GNSS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,40,87)"
                        }
                    }
                },
                {
                    "name": "11413S-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,10,111)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,19,60)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u5e73\u53f0\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,12,150)"
                        }
                    }
                },
                {
                    "name": "\u79fb\u52a8\u7aef\u63a8\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,6,151)"
                        }
                    }
                },
                {
                    "name": "1141BC-\u673a\u5668\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,9,75)"
                        }
                    }
                },
                {
                    "name": "\u533a\u5757\u94fe\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,92,118)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,160,106)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149SLAM/\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,77,101)"
                        }
                    }
                },
                {
                    "name": "\u98de\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,98,127)"
                        }
                    }
                },
                {
                    "name": "\u9065\u611f\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,103,63)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7Gnss\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,17,24)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u5f71\u50cf\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,18,100)"
                        }
                    }
                },
                {
                    "name": "\uff08\u6821\u62db\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,53,69)"
                        }
                    }
                },
                {
                    "name": "11417L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,48,5)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u56fd\u533a-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,125,134)"
                        }
                    }
                },
                {
                    "name": "11312G-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,1,19)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,63,57)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22&\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,61,131)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u8138\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,111,85)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,37,53)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u5149\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,56,88)"
                        }
                    }
                },
                {
                    "name": "C++\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,72,116)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u548c\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,150,28)"
                        }
                    }
                },
                {
                    "name": "05412O-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,64,74)"
                        }
                    }
                },
                {
                    "name": "\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,91,45)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,119,134)"
                        }
                    }
                },
                {
                    "name": "TX2980-SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,102,57)"
                        }
                    }
                },
                {
                    "name": "1121XJ-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,95,110)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,10,56)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,38,10)"
                        }
                    }
                },
                {
                    "name": "\u63a5\u7ba1\u9884\u8b66\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,158,150)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,72,7)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u53ca\u5bc6\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,14,75)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u65f6\u8def\u51b5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,5,137)"
                        }
                    }
                },
                {
                    "name": "ARVR/\u673a\u5668\u89c6\u89c9/\u56fe\u50cf\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,52,139)"
                        }
                    }
                },
                {
                    "name": "113195-\u97f3\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,54,39)"
                        }
                    }
                },
                {
                    "name": "254138-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,115,8)"
                        }
                    }
                },
                {
                    "name": "\u70b9\u4e91\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,58,65)"
                        }
                    }
                },
                {
                    "name": "BL5944-SPBU-\u7f8e\u989c\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,91,103)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,94,83)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u56fe\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,118,140)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,23,36)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4ea7\u54c1\u7ecf\u7406(\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,147,104)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f\u5185\u63a8 - \u5f00\u53d1/\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,58,45)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7/\u97f3\u4e50\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,32,82)"
                        }
                    }
                },
                {
                    "name": "ADAS\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,34,58)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6027\u80fd\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,21,42)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,22,121)"
                        }
                    }
                },
                {
                    "name": "\u65f6\u7a7a\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,155,62)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u7814\u53d1\u5de5\u7a0b\u5e08-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,57,138)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u89c4\u5212\u4e0e\u51b3\u7b56\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,41,23)"
                        }
                    }
                },
                {
                    "name": "\u6545\u969c\u8bca\u65ad(PHM)\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,105,138)"
                        }
                    }
                },
                {
                    "name": "npu\u67b6\u6784\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,11,42)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,104,136)"
                        }
                    }
                },
                {
                    "name": "AEB/LKA/ACC\u7814\u53d1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,62,41)"
                        }
                    }
                },
                {
                    "name": "BK32CA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,107,18)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,151,45)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,105,64)"
                        }
                    }
                },
                {
                    "name": "11414F-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,148,127)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,132,139)"
                        }
                    }
                },
                {
                    "name": "\u533b\u5b66\u56fe\u50cf\u914d\u51c6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,144,50)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u5f62\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,127,85)"
                        }
                    }
                },
                {
                    "name": "3D\u91cd\u5efa\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,46,56)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,18,132)"
                        }
                    }
                },
                {
                    "name": "OP2255-PTBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,93,114)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u5b9a\u4f4d\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,112,78)"
                        }
                    }
                },
                {
                    "name": "05415O-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,103,138)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,114,110)"
                        }
                    }
                },
                {
                    "name": "02416A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,28,125)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2App-\u7528\u6237\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,77,149)"
                        }
                    }
                },
                {
                    "name": "024254-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,79,97)"
                        }
                    }
                },
                {
                    "name": "\u4eca\u65e5\u5934\u6761-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,147,154)"
                        }
                    }
                },
                {
                    "name": "Vslam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,48,142)"
                        }
                    }
                },
                {
                    "name": "AI\u5730\u56fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,56,93)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u5a92\u4f53\u4f20\u8f93\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,121,134)"
                        }
                    }
                },
                {
                    "name": "Soul App-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,7,119)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u53f7\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,30,109)"
                        }
                    }
                },
                {
                    "name": "NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,47,99)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7cfb\u7edf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,129,27)"
                        }
                    }
                },
                {
                    "name": "09412L-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,42,125)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u56e2\u5e73\u53f0-\u6570\u636e\u6316\u6398\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,64,50)"
                        }
                    }
                },
                {
                    "name": "SG8103-SPBU-\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,72,73)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,98,69)"
                        }
                    }
                },
                {
                    "name": "SPBU-\u9ad8\u7ea7\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,132,142)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u4e0eNLP\u90e8-\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,56,83)"
                        }
                    }
                },
                {
                    "name": "11312H-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,76,135)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,78,38)"
                        }
                    }
                },
                {
                    "name": "\u5e94\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,84,94)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u8d37\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,94,142)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,89,79)"
                        }
                    }
                },
                {
                    "name": "RU0112-SPBU-\u89c6\u9891\u7f16\u89e3\u7801\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,103,117)"
                        }
                    }
                },
                {
                    "name": "11413B-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,129,118)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,72,3)"
                        }
                    }
                },
                {
                    "name": "\u7269\u7406\u5c42\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,157,35)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u7ea7AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,3,108)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u9065\u611f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,23,126)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,116,115)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66\u4e8b\u4e1a\u90e8_\u611f\u77e5\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,130,0)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,111,85)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u89c6\u9891\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,149,39)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6280\u53d1\u5c55\u90e8-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,144,121)"
                        }
                    }
                },
                {
                    "name": "\u6beb\u7c73\u6ce2\u96f7\u8fbe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,9,77)"
                        }
                    }
                },
                {
                    "name": "\u6e32\u67d3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,104,38)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc4\u6d4b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,15,114)"
                        }
                    }
                },
                {
                    "name": "\u641c\u7d22\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,36,0)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,133,56)"
                        }
                    }
                },
                {
                    "name": "[\u6025]\u7f51\u5b89\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,110,146)"
                        }
                    }
                },
                {
                    "name": "\u89c4\u5212\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,30,147)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u77e5\u8bc6\u56fe\u8c31\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,151,151)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u6027\u5316\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,86,131)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u6821\u62db\u3011\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,116,90)"
                        }
                    }
                },
                {
                    "name": "SW-\u673a\u5668\u4eba\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,94,91)"
                        }
                    }
                },
                {
                    "name": "AI\u8bad\u7ec3/\u63a8\u7406\u52a0\u901f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,29,60)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,67,34)"
                        }
                    }
                },
                {
                    "name": "0241UC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,114,20)"
                        }
                    }
                },
                {
                    "name": "AR\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,117,51)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u753b\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,41,118)"
                        }
                    }
                },
                {
                    "name": "\u6821\u62db-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,107,48)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,27,54)"
                        }
                    }
                },
                {
                    "name": "55413Q-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,38,76)"
                        }
                    }
                },
                {
                    "name": "1141BD-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,51,45)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u4fe1\u53f7\u5904\u7406/\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,146,18)"
                        }
                    }
                },
                {
                    "name": "PCG-\u5e7f\u544a\u589e\u957f\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,58,56)"
                        }
                    }
                },
                {
                    "name": "39318E-\u8ba1\u7b97\u673a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,42,128)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,100,140)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,64,37)"
                        }
                    }
                },
                {
                    "name": "11412I-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,91,93)"
                        }
                    }
                },
                {
                    "name": "2021\u6821\u56ed\u62db\u8058-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,101,108)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u5b66\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,7,60)"
                        }
                    }
                },
                {
                    "name": "1121PC-LT-354-\u5927\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,67,119)"
                        }
                    }
                },
                {
                    "name": "ASR/TTS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,84,63)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u548c\u89c6\u9891\u7406\u89e3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,42,117)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6d6a\u8d22\u7ecf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,71,3)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u667a\u80fd\u7ec4-\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,146,112)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u9690\u79c1\u8ba1\u7b97\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,139,4)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u603b\u76d1\uff08\u6570\u636e\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,156,138)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u56fe\u5f62\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,77,40)"
                        }
                    }
                },
                {
                    "name": "LJ5001-SPBU-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,45,134)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u6570\u5b57\u4eba-3D\u4eba\u8138\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,25,4)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u6316\u6398\u5de5\u7a0b\u5e08\uff08\u5e7f\u544a\u7b56\u7565\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,60,66)"
                        }
                    }
                },
                {
                    "name": "1131OJ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,90,135)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u7fa4\u8c03\u5ea6\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,112,100)"
                        }
                    }
                },
                {
                    "name": "3D\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,21,34)"
                        }
                    }
                },
                {
                    "name": "SS1060-SPBU-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,74,153)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,92,19)"
                        }
                    }
                },
                {
                    "name": "0341ET-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,114,134)"
                        }
                    }
                },
                {
                    "name": "\u8def\u5f84\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,56,24)"
                        }
                    }
                },
                {
                    "name": "AR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,4,148)"
                        }
                    }
                },
                {
                    "name": "55414C-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,130,89)"
                        }
                    }
                },
                {
                    "name": "\u30102021\u79cb\u62db\u3011\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,28,45)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u6d4f\u89c8\u5668\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,156,90)"
                        }
                    }
                },
                {
                    "name": "114125-\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,147,73)"
                        }
                    }
                },
                {
                    "name": "11416Z-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,156,118)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,13,53)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u9875\u641c\u7d22-\u591a\u6a21\u6001\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,70,78)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u97f3\u8bc6\u522b\uff08\u8bed\u8a00\u5efa\u6a21\uff09\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,102,21)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u89c9\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,49,106)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,0,81)"
                        }
                    }
                },
                {
                    "name": "MIG-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,137,134)"
                        }
                    }
                },
                {
                    "name": "11122I-LT-312-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,154,4)"
                        }
                    }
                },
                {
                    "name": "Camera\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,71,68)"
                        }
                    }
                },
                {
                    "name": "YAI-\u4eba\u5de5\u667a\u80fd\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,126,95)"
                        }
                    }
                },
                {
                    "name": "55413N-AI\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,123,101)"
                        }
                    }
                },
                {
                    "name": "\u57ce\u5e02\u8ba1\u7b97\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,11,0)"
                        }
                    }
                },
                {
                    "name": "\u878d\u5408\u5b9a\u4f4d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,37,111)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,133,26)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u683c\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,26,155)"
                        }
                    }
                },
                {
                    "name": "0241QC-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,77,81)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,138,24)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7/\u8d44\u6df1\u8fd0\u7b79\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,111,109)"
                        }
                    }
                },
                {
                    "name": "\u4e34\u5e8a\u7814\u7a76\u5458/\u4e34\u5e8a\u7814\u7a76\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,145,71)"
                        }
                    }
                },
                {
                    "name": "\u8bed\u8a00\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,147,47)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,90,43)"
                        }
                    }
                },
                {
                    "name": "BK4658-SPBU-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,53,66)"
                        }
                    }
                },
                {
                    "name": "\u5929\u732b\u597d\u623f-\u9ad8\u7ea7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,84,45)"
                        }
                    }
                },
                {
                    "name": "11122K-LT-310-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,140,66)"
                        }
                    }
                },
                {
                    "name": "0341DN-\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,74,43)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,92,17)"
                        }
                    }
                },
                {
                    "name": "5G\u57fa\u5e26\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,123,144)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,122,39)"
                        }
                    }
                },
                {
                    "name": "26310R-\u81ea\u7136\u8bed\u8a00\u5904\u7406\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,71,118)"
                        }
                    }
                },
                {
                    "name": "KHQ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,8,19)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350/\u5e7f\u544a/\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,67,72)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u7ef4\u70b9\u4e91\u5206\u6790\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,41,16)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u64ad\u5b89\u5168\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,153,7)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u673a\u5668\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,99,103)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u8bed\u97f3\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,48,111)"
                        }
                    }
                },
                {
                    "name": "\u58f0\u7eb9\u8bc6\u522b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,106,149)"
                        }
                    }
                },
                {
                    "name": "0241VF-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,157,9)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u6a21\u578b\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,136,118)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u7ea7\u63a8\u8350\u5f00\u53d1\uff08\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,115,89)"
                        }
                    }
                },
                {
                    "name": "\u8def\u7f51\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,108,131)"
                        }
                    }
                },
                {
                    "name": "\u51b3\u7b56\u4e0e\u8fd0\u52a8\u89c4\u5212\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,156,83)"
                        }
                    }
                },
                {
                    "name": "02426A-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,78,38)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u95fb\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,63,124)"
                        }
                    }
                },
                {
                    "name": "1131HA-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,68,100)"
                        }
                    }
                },
                {
                    "name": "\u591a\u4f20\u611f\u5668\u878d\u5408\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,153,118)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76\u8f66\u8f86\u63a7\u5236\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,80,49)"
                        }
                    }
                },
                {
                    "name": "024208-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,152,76)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u544a\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,94,58)"
                        }
                    }
                },
                {
                    "name": "AIOPS\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,42,146)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u770b\u70b9\u5546\u4e1a\u5316\u5e7f\u544a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,30,89)"
                        }
                    }
                },
                {
                    "name": "39314F-\u901a\u7528\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,125,6)"
                        }
                    }
                },
                {
                    "name": "0341DO-NLP\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,87,10)"
                        }
                    }
                },
                {
                    "name": "AI\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,27,114)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u6d41\u5e7f\u544a-\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,57,87)"
                        }
                    }
                },
                {
                    "name": "\u589e\u5f3a\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,45,51)"
                        }
                    }
                },
                {
                    "name": "OCR\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,140,104)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,107,23)"
                        }
                    }
                },
                {
                    "name": "0241VZ-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,113,15)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u98ce\u63a7\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,22,39)"
                        }
                    }
                },
                {
                    "name": "\u4eff\u771f\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,91,35)"
                        }
                    }
                },
                {
                    "name": "0232S5-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,87,139)"
                        }
                    }
                },
                {
                    "name": "LJ5001-\u56fe\u50cf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,96,130)"
                        }
                    }
                },
                {
                    "name": "11312J-\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,77,59)"
                        }
                    }
                },
                {
                    "name": "\u7f16\u8bd1\u5668\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,92,90)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,101,71)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6821\u62db\u3011\u641c\u7d22\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,69,113)"
                        }
                    }
                },
                {
                    "name": "\u5bf9\u8bdd\u63a8\u8350\u8d44\u6df1\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,32,47)"
                        }
                    }
                },
                {
                    "name": "\u7acb\u4f53\u89c6\u89c9\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,124,12)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u4f5c\u5f0a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,42,8)"
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
        chart_4f9e455d3f674f10a4c3cd9e317c3ae4.setOption(option_4f9e455d3f674f10a4c3cd9e317c3ae4);
    </script>
                <div id="0f1ba153e9cd452c958efa8579768e62" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0f1ba153e9cd452c958efa8579768e62 = echarts.init(
            document.getElementById('0f1ba153e9cd452c958efa8579768e62'), 'white', {renderer: 'canvas'});
            
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
    
        var option_0f1ba153e9cd452c958efa8579768e62 = {
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
                    "value": 241,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,127,142)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1",
                    "value": 126,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,31,64)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047",
                    "value": 112,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,108,21)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 107,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,113,85)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,8,61)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f11",
                    "value": 85,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,158,118)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,136,62)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229",
                    "value": 65,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,143,22)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11",
                    "value": 63,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,27,136)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,145,20)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336",
                    "value": 61,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,63,95)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u597d",
                    "value": 55,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,142,85)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968\u671f\u6743",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,99,40)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956",
                    "value": 47,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,105,6)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u516c\u53f8",
                    "value": 46,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,90,124)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 44,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,156,157)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0",
                    "value": 43,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,92,144)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u597d",
                    "value": 41,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,24,14)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u7ba1\u7406",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,18,88)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865",
                    "value": 40,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,109,14)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,140,150)"
                        }
                    }
                },
                {
                    "value": 38,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,35,48)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u4e91\u96c6",
                    "value": 37,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,35,88)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,38,69)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f",
                    "value": 33,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,91,71)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f",
                    "value": 29,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,129,21)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u745c\u4f3d",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,104,36)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d",
                    "value": 28,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,56,137)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316",
                    "value": 27,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,64,152)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u597d",
                    "value": 25,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,156,55)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,123,31)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcnice",
                    "value": 24,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,45,11)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,62,22)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55",
                    "value": 23,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,120,74)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u6fc0\u52b1",
                    "value": 22,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,78,54)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5927",
                    "value": 20,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,41,144)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,143,24)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u56e2\u961f",
                    "value": 19,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,110,95)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u597d",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,53,19)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743",
                    "value": 18,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,107,115)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e09\u9910",
                    "value": 17,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,0,24)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6587\u5316",
                    "value": 16,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,35,120)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u65f6",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,138,55)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,124,94)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,145,149)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa",
                    "value": 15,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,7,8)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u91d1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,104,34)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfc\u597d",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,149,69)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u6fc0\u52b1",
                    "value": 14,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,42,113)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u6c1b\u56f4",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,86,55)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,60,75)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u5236",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,19,0)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1",
                    "value": 13,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,88,50)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u597d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,23,85)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,56,132)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,63,128)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1",
                    "value": 12,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,78,39)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u664b\u5347",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,71,58)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u4f11\u5047",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,52,17)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u578b\u7814\u7a76\u9662",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,37,64)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u624d\u623f\u7968",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,53,59)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,35,123)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4\u5927",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,107,53)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u592e\u4f01",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,39,86)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,52,4)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u56e2\u961f",
                    "value": 11,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,131,68)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u73ed\u8f66",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,128,105)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u6253\u5361",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,80,117)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u5f3a",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,64,102)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,99,4)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e00\u91d1",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,42,145)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,59,13)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u4f18\u79c0",
                    "value": 10,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,98,154)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,53,78)"
                        }
                    }
                },
                {
                    "name": "\u7269\u8054\u7f51",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,17,12)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa",
                    "value": 9,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,156,150)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,134,58)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,53,158)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8\u5956",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,50,26)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,126,102)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u5168\u85aa",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,19,82)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u7a7a\u95f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,142,123)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u6280\u672f",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,126,130)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u7a7a\u95f4",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,21,127)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u597d",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,66,50)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,136,33)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4e30\u539a",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,8,77)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,131,134)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5927",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,146,135)"
                        }
                    }
                },
                {
                    "name": "AI",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,27,35)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e\u516c",
                    "value": 8,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,30,148)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,139,11)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u6cbf",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,160,116)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e8c\u91d1",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,48,119)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,48,2)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,38,112)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5bfc\u5e08",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,50,153)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,145,151)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961fnice",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,124,109)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u72ec\u89d2\u517d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,14,28)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,149,122)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5e74\u7ec8",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,76,134)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u8d34",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,141,16)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,28,77)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u9a7e\u9a76",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,42,70)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,9,4)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u5927",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,54,118)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,113,25)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u4f53\u68c0",
                    "value": 7,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,114,81)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u4e94\u9669\u4e00\u91d1",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,123,6)"
                        }
                    }
                },
                {
                    "name": "\u6025\u901f\u6210\u957f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,101,141)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,5,29)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,34,50)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNICE",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,105,144)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6c\u6b63",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,146,0)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u4e91\u96c6",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,145,144)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,23,150)"
                        }
                    }
                },
                {
                    "name": "\u8bf1\u4eba\u798f\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,120,132)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u4fbf\u5229",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,6,0)"
                        }
                    }
                },
                {
                    "name": "\u5927\u843d\u5730\u573a\u666f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,120,94)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u9879\u76ee",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,68,11)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,11,66)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u5b66\u4e60",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,26,27)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u5e73\u53f0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,107,138)"
                        }
                    }
                },
                {
                    "name": "\u79df\u623f\u8865\u8d34",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,74,64)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u7b49",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,33,111)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,54,128)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6c1b\u56f4\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,133,16)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,139,103)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u822a\u5929\u884c\u4e1a\u524d\u666f\u826f\u597d",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,60,69)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,135,102)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4f18\u79c0",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,61,16)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f\u9614",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,40,24)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5168\u664b\u5347\u673a\u5236",
                    "value": 6,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,45,129)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4e2d\u5fc3",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,158,84)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f73",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,82,36)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,160,2)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u591a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,109,47)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5f00\u516c\u6b63",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,144,103)"
                        }
                    }
                },
                {
                    "name": "\u673a\u4f1a\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,126,64)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u7b49",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,65,27)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5168",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,13,90)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5927\u725b\u591a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,31,115)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u56e2\u961f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,142,21)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u73ed",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,118,55)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u8865\u5145",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,34,33)"
                        }
                    }
                },
                {
                    "name": "16\u85aa",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,39,125)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u65f6\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,67,32)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f6c\u6b63\u673a\u4f1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,95,51)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u65f6\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,35,120)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u7968",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,75,2)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,121,30)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,97,119)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u80a1\u4e0a\u5e02",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,102,97)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5206\u7ea2",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,156,136)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c14\u6c1b\u597d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,151,157)"
                        }
                    }
                },
                {
                    "name": "\u4e8b\u4e1a\u5355\u4f4d",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,109,8)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,147,71)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u5546\u4e1a\u4fdd\u9669",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,111,102)"
                        }
                    }
                },
                {
                    "name": "\u671d\u9633\u884c\u4e1a",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,74,97)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,108,74)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u56e2\u961f",
                    "value": 5,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,14,111)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,155,97)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,58,57)"
                        }
                    }
                },
                {
                    "name": "\u623f\u8865",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,136,67)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd\u516c\u79ef\u91d1",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,128,3)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u73af\u5883\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,10,30)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8d39\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,81,24)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,101,156)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,126,90)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u4e0e\u5b66\u4e60\u6c1b\u56f4\u3002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,70,151)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u9ad8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,9,2)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,56,73)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,121,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u4e30\u539a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,109,156)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,2,154)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9f50\u5168",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,73,31)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u56e2\u961f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,97,40)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u6cbf",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,114,141)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,57,20)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,80,145)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5bb6\u5c45",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,117,30)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,10,139)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4nice",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,4,105)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u6709\u6d3b\u529b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,73,51)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,56,160)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u8f7b\u677e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,103,154)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u6709\u524d\u666f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,66,90)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,43,5)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u8d34",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,160,80)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,21,142)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u4e13\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,39,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,54,34)"
                        }
                    }
                },
                {
                    "name": "\u4e0d996",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,111,40)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7a33\u5b9a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,57,52)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u62a5\u9500",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,135,35)"
                        }
                    }
                },
                {
                    "name": "\u843d\u6237\u5feb",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,101,26)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u516c\u53f8",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,59,118)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,120,140)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u5927\u725b",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,136,123)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,69,88)"
                        }
                    }
                },
                {
                    "name": "8\u5929\u5e74\u5047",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,30,146)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u6d53",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,118,150)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u65c5\u6e38",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,132,49)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8212\u9002",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,154,8)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u6587\u5316\u597d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,21,34)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4efd\u671f\u6743",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,13,150)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u6c14\u5341\u8db3",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,62,28)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d12-6\u4e2a\u6708",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,12,123)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u673a\u4f1a\u591a",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,107,82)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u56e2\u5efa",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,145,150)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6570\u636e",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,131,76)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u53d1\u5c55\u8d8b\u52bf\u4e0e\u53d1\u5c55\u7a7a\u95f4",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,29,116)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8fdc\u7a0b\u529e\u516c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,65,1)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,70,37)"
                        }
                    }
                },
                {
                    "name": "\u8f66\u5382\u5408\u4f5c",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,159,155)"
                        }
                    }
                },
                {
                    "name": "\u5168\u52e4\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,51,22)"
                        }
                    }
                },
                {
                    "name": "\u6709\u517c\u804c\u5c97\u4f4d",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,2,114)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5b8c\u5584",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,133,7)"
                        }
                    }
                },
                {
                    "name": "2-6\u4e2a\u6708\u5e74\u7ec8\u5956",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,131,150)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,105,53)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u9910",
                    "value": 4,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,7,32)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u56db\u6b21\u8bc4\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,94,102)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,2,62)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u5316\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,6,83)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u89c4\u8303",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,32,102)"
                        }
                    }
                },
                {
                    "name": "\u611f\u77e5\u9636\u8dc3\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,66,91)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5bfc\u5411",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,55,114)"
                        }
                    }
                },
                {
                    "name": "\u56fe\u50cf\u7b97\u6cd5",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,116,132)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,46,130)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u68d2\u7684\u9886\u5bfc",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,46,57)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,106,116)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,143,24)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,7,100)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u53ef\u89c2",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,70,140)"
                        }
                    }
                },
                {
                    "name": "\u8fc7\u8282\u8d39",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,69,15)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,48,116)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u7231",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,17,11)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,110,77)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,78,31)"
                        }
                    }
                },
                {
                    "name": "base",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,155,65)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,43,100)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u65b9\u4fbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,105,82)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u9879\u76ee",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,122,33)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u5e26\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,2,112)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,104,25)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u574718\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,50,25)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u75c5\u5047",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,24,126)"
                        }
                    }
                },
                {
                    "name": "\u996d\u8865",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,88,111)"
                        }
                    }
                },
                {
                    "name": "\u5bbf\u820d\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,17,82)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u7a0b\u5e08\u6587\u5316",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,69,115)"
                        }
                    }
                },
                {
                    "name": "15\u85aa",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,31,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u4f1a\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,104,74)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,116,13)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,146,28)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,70,20)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u4e1a\u52a1\u573a\u666f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,103,88)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u5b9e\u4ea4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,97,97)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,103,153)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,150,116)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u652f\u6301\u7ed9\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,33,15)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u52a0\u73ed",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,152,154)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4f4f\u5bbf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,13,109)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u641c\u7d22\u7b97\u6cd5\u6838\u5fc3\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,0,63)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,37,115)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u8fc7\u4ebf",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,45,0)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,54,138)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u57f9\u8bad",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,70,130)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,134,37)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u878d\u6d3d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,25,76)"
                        }
                    }
                },
                {
                    "name": "\u5348\u9910\u8865\u52a9",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,48,95)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,73,86)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,85,38)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u6240\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,73,15)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f73",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,62,63)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u7cbe\u6e5b",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,129,88)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u6e5b\u7684\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,118,19)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,101,74)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u53d1\u5c55\u7a7a\u95f4",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,52,50)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u725b\u7684\u6280\u672f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,140,97)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5496\u5561",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,85,4)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u85aa\u916c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,83,158)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u65e9\u5348\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,52,96)"
                        }
                    }
                },
                {
                    "name": "\u65e0996",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,66,70)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u96f6\u98df",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,94,118)"
                        }
                    }
                },
                {
                    "name": "\uff0858\uff09\u730e\u5934\u804c\u4f4d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,101,37)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u4e1a\u52a1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,29,27)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,151,133)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u56e2\u961f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,72,107)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u5956\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,24,57)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,72,99)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u80a1\u7968",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,136,34)"
                        }
                    }
                },
                {
                    "name": "\u671d\u4e5d\u665a\u516d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,73,43)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c\u4e94\u767e\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,34,35)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u884c\u4e1a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,104,139)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5065\u5168",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,12,146)"
                        }
                    }
                },
                {
                    "name": "\u591f\u6311\u6218\u591f\u523a\u6fc0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,99,76)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u8fdb\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,148,69)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u5f53\u4e00\u9762",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,19,84)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u52b1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,155,1)"
                        }
                    }
                },
                {
                    "name": "\u7b7e\u5b57\u73b0\u91d1",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,151,57)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,77,111)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4e0b\u5348\u8336",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,82,132)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,50,55)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,40,46)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,38,131)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u884c\u4e1a\u9886\u5148",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,20,4)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,65,89)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u7b79\u5907",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,12,46)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,4,66)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u5f00\u653e\u73af\u5883",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,84,84)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u8865\u8d34",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,121,155)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u6c1b\u56f4\u597d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,48,100)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6709\u5927\u884c\u76f4\u9500\u94f6\u884c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,113,32)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fNice",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,0,125)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u6210\u957f",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,131,79)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,94,57)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u5168\u989d",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,136,76)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956\u52b1\u5236",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,150,139)"
                        }
                    }
                },
                {
                    "name": "**\u56e2\u961f+\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,15,113)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5021\u8ffd\u6c42\u5353\u8d8a",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,38,125)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u9879\u76ee\u7ecf\u9a8c",
                    "value": 3,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,55,123)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u4f18\u6e25",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,7,67)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,56,72)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u4e0b\u5348\u8336",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,149,107)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,21,148)"
                        }
                    }
                },
                {
                    "name": "\u745c\u4f3d\u5065\u8eab",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,84,64)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,137,44)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,79,14)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,144,59)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,136,3)"
                        }
                    }
                },
                {
                    "name": "\u516d\u65e5\u53cc\u4f11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,1,145)"
                        }
                    }
                },
                {
                    "name": "\u4e24\u9910\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,82,129)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,89,6)"
                        }
                    }
                },
                {
                    "name": "P7+\u53ef\u4eab\u53d7\u963f\u91cc\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,133,49)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,136,138)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab/\u96f6\u98df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,25,72)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,85,1)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7ba1\u7406",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,119,38)"
                        }
                    }
                },
                {
                    "name": "\u671f\u5f85\u60a8\u7684\u52a0\u5165",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,18,141)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u5927\u5b66\u7684\u667a\u80fd\u8fd0\u7ef4\u5b9e\u9a8c\u5ba4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,13,126)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5f3a\u5236\u52a0\u73ed",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,66,143)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u8865",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,72,79)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,36,71)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ade\u4e89\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,151,33)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u5e73\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,116,35)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,53,63)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u6c11APP",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,64,126)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u6253\u5361",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,49,151)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u8005\u7ed9\u4e0e\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,98,43)"
                        }
                    }
                },
                {
                    "name": "14-20\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,95,81)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u589e\u957f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,59,102)"
                        }
                    }
                },
                {
                    "name": "\u4e16\u754c500\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,37,133)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7ebf\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,95,119)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,56,89)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u6c1b\u56f4\u4ff1\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,16,12)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u8d8b\u52bf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,23,15)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u82f1\u6587\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,4,116)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5ba2\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,69,78)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,109,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u91d1+\u5b63\u5ea6\u5956\u91d1+\u597d\u5fc3\u60c5+\u798f\u5229\u591a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,49,18)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5e73\u53f0\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,79,2)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,108,29)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6280\u672f\u9886\u5148",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,24,9)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u7fd8\u695a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,144,125)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,93,130)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u7ed9\u529b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,101,97)"
                        }
                    }
                },
                {
                    "name": "AI\u673a\u5668\u4eba",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,119,106)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,17,113)"
                        }
                    }
                },
                {
                    "name": "\u6781\u5177\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u5f85\u9047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,147,63)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0a\u5e02\u9884\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,145,93)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5956\u91d1+\u80a1\u6743/\u671f\u6743\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,81,31)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,159,134)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u5168\u989d\u7f34\u7eb3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,80,98)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u4f11\u5047",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,83,77)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8bafC\u8f6e\u9886\u6295",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,119,21)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,96,0)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,30,50)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u53e3\u6d6a\u5c16",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,112,103)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u65b0\u5174\u9886\u57df",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,32,23)"
                        }
                    }
                },
                {
                    "name": "AI\u97f3\u4e50",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,119,97)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,27,131)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u91cf\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,131,107)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u6d59\u5927",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,104,50)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185TOP3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,8,122)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u4e2d\u53f0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,48,2)"
                        }
                    }
                },
                {
                    "name": "\u7845\u8c37\u5927\u725b",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,63,37)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u65b0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,149,95)"
                        }
                    }
                },
                {
                    "name": "\u98de\u901f\u53d1\u5c55",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,128,75)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u4ea7\u54c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,68,127)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,35,5)"
                        }
                    }
                },
                {
                    "name": "14\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,49,32)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,11,84)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u673a\u4f1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,65,100)"
                        }
                    }
                },
                {
                    "name": "\u6d25\u8d34\u8865\u52a9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,91,140)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u4e91\u96c6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,68,4)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,110,14)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,86,160)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u901a\u8054\u6570\u636e\u8054\u5408\u62db\u8058",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,149,155)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,100,100)"
                        }
                    }
                },
                {
                    "name": "*\u5e74\u5e95\u53cc\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,160,34)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u7814\u7a76",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,29,83)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,29,113)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u843d\u5730",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,152,90)"
                        }
                    }
                },
                {
                    "name": "base*13+0-6\u4e2a\u6708\u5e74\u7ec8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,55,85)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,134,39)"
                        }
                    }
                },
                {
                    "name": "\u6301\u724c\u673a\u6784",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,41,34)"
                        }
                    }
                },
                {
                    "name": "AI+\u6559\u80b2",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,5,97)"
                        }
                    }
                },
                {
                    "name": "\u524d\u666f\u5e7f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,100,129)"
                        }
                    }
                },
                {
                    "name": "\u9760\u8c31\u516c\u53f8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,31,136)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u5730\u94c1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,62,73)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5956\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,85,47)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,114,104)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u52a0\u73ed\u53cc\u500d\u5de5\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,15,52)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053\u5b8c\u5584",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,77,53)"
                        }
                    }
                },
                {
                    "name": "\u843d\u5730\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,103,154)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u6cbf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,35,64)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u6307\u5bfc",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,87,52)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u751f\u65e5\u8282\u5047\u65e5\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,62,58)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u63d0\u4f9b\u4e09\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,18,14)"
                        }
                    }
                },
                {
                    "name": "\u6cd5\u5b9a\u8282\u5047\u65e5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,86,42)"
                        }
                    }
                },
                {
                    "name": "13\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,91,141)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44OPEN",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,4,78)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u81ea\u7531",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,77,4)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80fd\u529b\u5f3a\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,49,38)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6b21\u8c03\u85aa",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,114,146)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u578b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,74,39)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7406\u53d1\u5e97",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,138,159)"
                        }
                    }
                },
                {
                    "name": "\u73ed\u8f66\u63a5\u9001",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,110,67)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u665a\u9910",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,53,92)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,11,111)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,61,98)"
                        }
                    }
                },
                {
                    "name": "\u66f9\u64cd\u51fa\u884c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,112,51)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5733\u51fa\u6d77\u524d\u4e09",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,138,42)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u7968",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,14,72)"
                        }
                    }
                },
                {
                    "name": "\u989c\u503c\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,108,130)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u5c11",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,117,149)"
                        }
                    }
                },
                {
                    "name": "\u4e1c\u5357\u4e9a\u5e02\u573a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,117,157)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u6fc0\u60c5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,16,53)"
                        }
                    }
                },
                {
                    "name": "\u901a\u8baf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,144,45)"
                        }
                    }
                },
                {
                    "name": "\u5404\u9879\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,94,139)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5927\u3002",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,12,127)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,116,8)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,99,142)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5e74\u7ec8\u5956+\u5458\u5de5\u6301\u80a1\u5236\u5ea6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,67,60)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u957f\u671f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,94,129)"
                        }
                    }
                },
                {
                    "name": "IOT\u9886\u5148\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,141,153)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u8fc5\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,48,87)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,118,147)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u524d\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,156,119)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9510\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,21,33)"
                        }
                    }
                },
                {
                    "name": "*\u80a1\u7968\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,136,53)"
                        }
                    }
                },
                {
                    "name": "16\u85aa\u8d44",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,82,10)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u52a8\u9a7e\u9a76\u524d\u77bb\u6280\u672f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,105,14)"
                        }
                    }
                },
                {
                    "name": "*\u6708\u5ea6\u7ee9\u6548\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,124,3)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u65e0\u9650",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,110,19)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,43,32)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u57fa\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,8,59)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u7ade\u4e89\u529b\u7684\u85aa\u8d44\u6c34\u5e73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,90,141)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,144,57)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a33\u5b9a+\u6210\u957f\u664b\u5347+\u6280\u672f\u9a71\u52a8+\u80a1\u7968\u6fc0\u52b1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,46,94)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e1a\u52a1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,45,62)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5f3a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,14,121)"
                        }
                    }
                },
                {
                    "name": "6\u96692\u91d1",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,136,50)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1/\u5b63\u5ea6\u5956/\u5e26\u85aa\u5e74\u5047/\u5e74\u7ec8\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,45,21)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5927\u4e0a\u73af\u5883",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,101,140)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u4e0a\u76d6",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,85,6)"
                        }
                    }
                },
                {
                    "name": "Mac\u529e\u516c",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,69,56)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,143,124)"
                        }
                    }
                },
                {
                    "name": "\u6ef4\u6ef4\u6253\u8f66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,125,149)"
                        }
                    }
                },
                {
                    "name": "\u98ce\u63a7\u72ec\u89d2\u517d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,36,23)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u9ad8",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,46,60)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,145,116)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u96c4\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,17,113)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u9879\u76ee",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,129,159)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,74,23)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,158,121)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f73",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,64,47)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,145,7)"
                        }
                    }
                },
                {
                    "name": "\u516c\u5e73\u516c\u6b63",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,109,140)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e1a\u52a1\u573a\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,143,142)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4e1a\u52a1\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,7,16)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u725b\u591a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,70,40)"
                        }
                    }
                },
                {
                    "name": "\u96c6\u56e2\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,114,54)"
                        }
                    }
                },
                {
                    "name": "\u94f6\u884c\u80cc\u666f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,77,106)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,128,97)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u7528\u6237",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,153,158)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u539a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,155,128)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,56,120)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u878d\u6d3d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,95,114)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f/\u85aa\u8d44\u798f\u5229",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,86,16)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,28,121)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u798f\u5229\u7b49",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,150,99)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u900f\u660e",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,117,29)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,29,149)"
                        }
                    }
                },
                {
                    "name": "80%\u8f6c\u6b63\u7387",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,13,119)"
                        }
                    }
                },
                {
                    "name": "\u8f7b\u677e\u6d3b\u8dc3",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,121,3)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185\u9886\u5148\u91d1\u878d\u79d1\u6280",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,134,34)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,57,89)"
                        }
                    }
                },
                {
                    "name": "\u5065\u5eb7\u4f53\u68c0",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,48,128)"
                        }
                    }
                },
                {
                    "name": "Geek",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,22,84)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u7ea2\u4e66",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,156,147)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u5e76\u53d1\u7cfb\u7edf",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,124,61)"
                        }
                    }
                },
                {
                    "name": "\u5730\u94c1\u5468\u8fb9",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,146,136)"
                        }
                    }
                },
                {
                    "name": "\u793e\u533a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,135,151)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u597d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,43,146)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u52b2\u535a\u58eb\u56e2\u961f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,7,102)"
                        }
                    }
                },
                {
                    "name": "AI\u91d1\u878d",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,18,28)"
                        }
                    }
                },
                {
                    "name": "AI\u82af\u7247",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,35,30)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u6709\u5b9e\u529b\u7684\u5927\u4f01\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,65,115)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u5feb\u901f",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,46,109)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u6280\u672f\u6c1b\u56f4",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,104,68)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,62,9)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168\u9762",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(151,24,105)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u7a33\u5b9a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,88,10)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f18\u8d8a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,135,132)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u521b\u65b0\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,155,147)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u884c\u4e1a",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,14,26)"
                        }
                    }
                },
                {
                    "name": "\u5f02\u5730\u5b66\u751f\u5b9e\u4e60\u6709\u4f4f\u5bbf\u8865\u8d34",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,126,95)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u5956",
                    "value": 2,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,18,138)"
                        }
                    }
                },
                {
                    "name": "\u5782\u76f4\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,7,128)"
                        }
                    }
                },
                {
                    "name": "**\u6295\u8d44\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,87,93)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6e90\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,58,85)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,135,16)"
                        }
                    }
                },
                {
                    "name": "\u4fdd\u5e9513\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,149,78)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u4e1a\u52a1\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,16,78)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u4f11\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,135,20)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5168",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,138,116)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,128,141)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,33,7)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,66,12)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u8bbe\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,64,120)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b9e\u4e60\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,17,33)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,9,94)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u8f7b\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,71,11)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u8d85\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,158,30)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u7f34\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,150,139)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,70,151)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,147,56)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5f02\u8005\u53ef\u8f6c\u6821\u62db\u6b63\u5f0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,120,15)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u4f53\u68c0\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,70,11)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e081v1\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,26,121)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,10,139)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u533b\u7597\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,27,89)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u56e2\u961f\u5747\u4e3a\u81ea\u52a8\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,39,54)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,119,78)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18\u826f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,4,48)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u63a8\u8350",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,91,25)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e0d\u5dee\u94b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,46,127)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u57fa\u5efa\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,58,98)"
                        }
                    }
                },
                {
                    "name": "\u6784\u5efa\u4eba\u7c7b\u865a\u62df\u4e16\u754c\u65b0\u4f53\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,146,70)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,76,47)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u671f\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,17,49)"
                        }
                    }
                },
                {
                    "name": "\u4eab\u6709\u80a1\u6743\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,66,37)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,143,117)"
                        }
                    }
                },
                {
                    "name": "\u9910\u996e\u8865\u52a9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,95,4)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u767e\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,141,28)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u73af\u4fdd\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,109,140)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,101,14)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd\u516c\u79ef\u91d1\u60c5\u51b5\uff1a\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,158,151)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6d3b\u5343\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,116,22)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,141,43)"
                        }
                    }
                },
                {
                    "name": "\u5173\u7cfb\u548c\u8c10",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,50,107)"
                        }
                    }
                },
                {
                    "name": "\u5305\u53cc\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,152,105)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5229\u4e8e\u53d1\u8bba\u6587",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,16,145)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,75,37)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1(\u6700\u9ad8\u6bd4\u4f8b)",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,115,23)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u4e1c\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,145,160)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u4eb2\u81ea\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,28,152)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,68,160)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u516d\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,121,136)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,85,14)"
                        }
                    }
                },
                {
                    "name": "\u5168\u6808\u6280\u672f\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,76,131)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u843d\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,98,152)"
                        }
                    }
                },
                {
                    "name": "ai\u533b\u7597\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,66,133)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,80,77)"
                        }
                    }
                },
                {
                    "name": "\u5fae\u8f6f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,86,127)"
                        }
                    }
                },
                {
                    "name": "CTO\u7b97\u6cd5\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,49,52)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(60,49,55)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u5927\u4f6c\u4e00\u8d77\u53c2\u52a0\u56fd\u9645\u9876\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,27,84)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u4e0a\u4e0b\u73ed\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,30,66)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u664b\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,4,23)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,7,88)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbfAR\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,36,72)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d1f\u8d23\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,95,88)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u590d\u6742",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,102,105)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7814\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,80,106)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u5927\u4f6c\u5e26\u4f60\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,112,31)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,62,113)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u53d1\u5c55\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,7,76)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u7f8e\u5473\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,44,74)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u6f5c\u529b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,99,119)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,129,146)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,25,48)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u914d\u9001",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,131,132)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6709\u4f5c\u4e3a\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,121,7)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u4f53\u7cfb\u5b8c\u5584",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,106,103)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,146,10)"
                        }
                    }
                },
                {
                    "name": "\u529e\u516c\u73af\u5883\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,10,36)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u90e8\u95e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,46,130)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u539a\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,35,132)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,140,143)"
                        }
                    }
                },
                {
                    "name": "\u5171\u521b\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,57,158)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u8bc4\u4f18\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,75,136)"
                        }
                    }
                },
                {
                    "name": "Mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,55,38)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,28,43)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u578b\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,8,67)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,100,105)"
                        }
                    }
                },
                {
                    "name": "\u798f\u7530CBD",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,154,64)"
                        }
                    }
                },
                {
                    "name": "\u6574\u4f53\u89e3\u51b3\u65b9\u6848\u80fd\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,15,146)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u53ca\u85aa\u916c\u9ad8\u4e8e\u540c\u884c\u4e1a\u6c34\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,130,121)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,15,69)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1\u4e2d\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,129,146)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5e73\u53f0\u798f\u5229\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,120,117)"
                        }
                    }
                },
                {
                    "name": "13\u85aa+\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,1,133)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u524d\u6cbf\u7814\u7a76\u53ca\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,70,152)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,83,103)"
                        }
                    }
                },
                {
                    "name": "\u4f60\u7684\u6bcf\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,158,160)"
                        }
                    }
                },
                {
                    "name": "\u5927\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,145,125)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u73af\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,135,30)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u5316\u5f15\u64ce\u7684\u7cfb\u7edf\u67b6\u6784",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,73,94)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,71,45)"
                        }
                    }
                },
                {
                    "name": "\u591a\u6837\u5316\u7684\u5b66\u4e60\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,14,0)"
                        }
                    }
                },
                {
                    "name": "\u9662\u58eb\u5e26\u961f\u53c2\u4e0e\u9ad8\u6821\u8054\u5408\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,43,99)"
                        }
                    }
                },
                {
                    "name": "\u8282\u5047\u65e5\u52a0\u73ed\u4e09\u500d\u5de5\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,156,92)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7d20\u8d28\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(99,137,9)"
                        }
                    }
                },
                {
                    "name": "\u6280\u80fd\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,153,9)"
                        }
                    }
                },
                {
                    "name": "\u5927\u6570\u636e\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,50,78)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,142,29)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u98ce\u63a7\u5782\u76f4\u9886\u57df\u6df1\u5ea6\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,110,76)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316\u89c6\u91ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,131,101)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,152,139)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,46,159)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9ad8P",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,51,127)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21review\u664b\u5347\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,39,83)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,57,120)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7814\u53d1\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,2,124)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,5,72)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,74,62)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,86,138)"
                        }
                    }
                },
                {
                    "name": "12\u5929\u5e74\u5047\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,120,60)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u529e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,107,113)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5385",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,67,105)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u7a7a\u95f4\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,65,139)"
                        }
                    }
                },
                {
                    "name": "\u65af\u5766\u798f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,87,87)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u9971\u6ee1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,46,116)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,71,40)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,151,70)"
                        }
                    }
                },
                {
                    "name": "\u3010\u8304\u5b50\u5feb\u4f20\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,68,131)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5065\u589e\u957f\u7684\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,143,143)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u6c7d\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,20,85)"
                        }
                    }
                },
                {
                    "name": "3D\u89c6\u89c9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,52,22)"
                        }
                    }
                },
                {
                    "name": "\u8fd0\u7528\u8fd0\u7b79\u4f18\u5316\u77e5\u8bc6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,89,155)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,128,143)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,71,128)"
                        }
                    }
                },
                {
                    "name": "\u5b63\u5ea6\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,65,55)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u5316\u7ba1\u7406\u5de5\u4f5c\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,22,7)"
                        }
                    }
                },
                {
                    "name": "\u7a33\u5b9a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,47,98)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,77,100)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,120,115)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,102,120)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,124,16)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u989d\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,27,68)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8f6e\u5c97\u6216\u8f6c\u5c97\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,13,35)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5efa\u8bbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,26,30)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,129,46)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,133,137)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,6,3)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u8d8520\u5e74\u76f8\u5173\u7ecf\u9a8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,109,136)"
                        }
                    }
                },
                {
                    "name": "AI\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,135,54)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,97,24)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u671f\u805a\u9910~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,107,71)"
                        }
                    }
                },
                {
                    "name": "\u4e3b\u52a8\u52a0\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,57,154)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53e3\u7891\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,55,123)"
                        }
                    }
                },
                {
                    "name": "\u76c8\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,1,114)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u6570\u636e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,60,9)"
                        }
                    }
                },
                {
                    "name": "\u5173\u952e\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,6,73)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u4f1a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,157,122)"
                        }
                    }
                },
                {
                    "name": "\u7269\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,42,35)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u5feb\u624b\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,147,155)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u4fdd\u9669\u7b49\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,94,89)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,140,142)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u8282\u65e5\u798f\u5229\u5e74\u5ea6\u4f53\u68c0\u52a0\u73ed\u8865\u52a9\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,87,56)"
                        }
                    }
                },
                {
                    "name": "\u6709\u671f\u6743\u6388\u4e88",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,61,125)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u4eba\u5e26\u65b0\u624b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,96,57)"
                        }
                    }
                },
                {
                    "name": "\u671f\u6743\u80a1\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,119,153)"
                        }
                    }
                },
                {
                    "name": "\u516c\u79ef\u91d1\u5168\u989d\u6700\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,106,155)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,28,32)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u5bbf\u820d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,156,81)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,146,121)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,44,150)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u73ed\u5f00\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,90,129)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u516c\u53f8\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,127,11)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u9886\u57df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,155,102)"
                        }
                    }
                },
                {
                    "name": "\u6709\u66f4\u9ad8\u66f4\u5927\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,10,138)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,125,67)"
                        }
                    }
                },
                {
                    "name": "NICE\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,94,107)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,98,146)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,155,95)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,27,158)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u52a0\u5165",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,5,73)"
                        }
                    }
                },
                {
                    "name": "\u7f8e\u7684\u5173\u8054\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,141,101)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,135,14)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5b66\u4e60\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,80,29)"
                        }
                    }
                },
                {
                    "name": "\u6709\u8f83\u597d\u7684\u8d44\u6e90\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,73,124)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,3,58)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u53d1\u5c55\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,83,104)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,117,83)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u9910\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,159,72)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,75,134)"
                        }
                    }
                },
                {
                    "name": "\u3010\u611f\u77e5\u9636\u8dc3\u3011\u7b97\u6cd5\u5de5\u7a0b\u5e08",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,136,109)"
                        }
                    }
                },
                {
                    "name": "\u548c\u8c10\u7684\u56e2\u961f\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,88,54)"
                        }
                    }
                },
                {
                    "name": "AI\u533b\u7597\u9886\u57df\u72ec\u89d2\u517d\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,114,50)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f4f\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,32,23)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,156,7)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,157,84)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u5fc3\u7814\u7a76\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,20,157)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6548\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,83,90)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,103,105)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u9a71\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,128,108)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u5458\u5de5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,45,151)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u901a\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,66,83)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916SaaS\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,156,8)"
                        }
                    }
                },
                {
                    "name": "\u9910\u901a\u8baf\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,21,13)"
                        }
                    }
                },
                {
                    "name": "\u4ff1\u4e50\u90e8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,105,138)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u805a\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,70,16)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,116,127)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,138,85)"
                        }
                    }
                },
                {
                    "name": "\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,142,46)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u56e2\u961f\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,68,157)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,50,83)"
                        }
                    }
                },
                {
                    "name": "\u5f15\u9886\u884c\u4e1a\u8d70\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,77,138)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u4e2a\u5c97\u4f4d\u6210\u5c31\u4e00\u756a\u4e8b\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,14,34)"
                        }
                    }
                },
                {
                    "name": "\u56db\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,147,92)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,1,86)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,38,143)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,88,139)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,123,86)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u6e20\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,62,133)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,16,26)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,83,136)"
                        }
                    }
                },
                {
                    "name": "\u83b7\u591a\u5bb6**\u673a\u6784\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,15,150)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,136,128)"
                        }
                    }
                },
                {
                    "name": "5\u59298\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,154,129)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,159,154)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8bnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,124,56)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,59,140)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u5efa\u65c5\u6e38\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,65,85)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u5c0f\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,153,136)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403**\u79d1\u5b66\u5bb6\u8ddf\u6295",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,44,16)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a\u524d\u6cbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,72,38)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u4ea4\u901a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,90,81)"
                        }
                    }
                },
                {
                    "name": "\u5076\u5c14\u52a0\u73ed\u8c03\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,65,14)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,118,94)"
                        }
                    }
                },
                {
                    "name": "\u7a7a\u95f4\u4e09\u7ef4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,99,99)"
                        }
                    }
                },
                {
                    "name": "AI\u98ce\u53e3\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,119,15)"
                        }
                    }
                },
                {
                    "name": "\u535a\u5bfc\u5e26\u961f\u7684\u6df1\u5ea6\u5b66\u4e60\u4eba\u5de5\u667a\u80fd\u7814\u7a76\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,1,151)"
                        }
                    }
                },
                {
                    "name": "\u6536\u5165\u548c\u80fd\u529b\u6210\u957f\u6027\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,58,126)"
                        }
                    }
                },
                {
                    "name": "\u4ea4\u901a\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,75,69)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,93,33)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e24\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,93,90)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1+\u5b63\u5ea6\u7ee9\u6548\u5956\u91d1/\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,70,79)"
                        }
                    }
                },
                {
                    "name": "\u77e5\u540d\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,12,94)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u8d85\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,147,51)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,66,32)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,85,123)"
                        }
                    }
                },
                {
                    "name": "\u9519\u8fc7\u4e8610\u5e74\u7684\u624b\u6dd8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,127,104)"
                        }
                    }
                },
                {
                    "name": "\u8bd5\u7528\u671f\u4ea4\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,67,81)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4e07DAU",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,55,80)"
                        }
                    }
                },
                {
                    "name": "\u9876\u683c\u4f4f\u623f\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(4,95,52)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,141,1)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u8d44\u6e90\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,45,8)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u9ad8\u798f\u5229\u597d\u5927\u725b\u8eab\u8fb9\u7ed5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,16,157)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(72,96,69)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u8d77\u70b9",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,104,79)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u6027\u7684\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,65,35)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(139,134,113)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,151,53)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u81ea\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,120,39)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u5047\u671f14\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,146,139)"
                        }
                    }
                },
                {
                    "name": "\u6d41\u7a0b\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,40,149)"
                        }
                    }
                },
                {
                    "name": "B2B\u91d1\u878d\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,83,101)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,125,96)"
                        }
                    }
                },
                {
                    "name": "\u4eac\u6caa\u676d\u5747\u6709hc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,137,36)"
                        }
                    }
                },
                {
                    "name": "\u5341\u4e94\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,66,90)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5e7f\u9614\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,124,15)"
                        }
                    }
                },
                {
                    "name": "AI\u56e2\u961f\u7b79\u5efa\u4e2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,87,43)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6\u4f18\u5316\u5f15\u64ce\u7684\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,21,0)"
                        }
                    }
                },
                {
                    "name": "\u5317\u5927\u540d\u6821\u540c\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,41,93)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u597d\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,103,52)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,136,86)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,56,115)"
                        }
                    }
                },
                {
                    "name": "\u540d\u6821\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,81,128)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,3,74)"
                        }
                    }
                },
                {
                    "name": "\u6b22\u8fce\u60a8\u52a0\u5165\u4e00\u70b9\u5927\u5bb6\u5ead~",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,101,130)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,125,8)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u521b\u65b0\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,105,45)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u804c\u7ea7\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,80,127)"
                        }
                    }
                },
                {
                    "name": "\u957f\u671f\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,87,112)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6587\u6863\u968f\u4fbf\u770b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,12,32)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5348\u9910\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(80,152,74)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u7684\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,8,56)"
                        }
                    }
                },
                {
                    "name": "\u7535\u5546\u5bfc\u8d2d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,118,0)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4up",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,125,55)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,124,4)"
                        }
                    }
                },
                {
                    "name": "\u57f9\u8bad\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,6,41)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u62ff\u9f50\u805a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(37,156,15)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,54,147)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u7ed9\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,160,101)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,122,84)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,17,159)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5e72\u9884\u662f\u7f8e\u56e2\u9a91\u884c\u4e1a\u52a1\u6838\u5fc3\u90e8\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,145,148)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,84,125)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,157,16)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,159,86)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u65e0\u9650",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,84,57)"
                        }
                    }
                },
                {
                    "name": "\u91d1\u878d\u79d1\u6280\u884c\u4e1aTOP",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,117,103)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u8d28\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,119,69)"
                        }
                    }
                },
                {
                    "name": "\u6709\u5348\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,27,105)"
                        }
                    }
                },
                {
                    "name": "\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,68,12)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u8d5e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,58,82)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8bf1\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,3,72)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5c0f\u5468",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,115,132)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,88,26)"
                        }
                    }
                },
                {
                    "name": "\u8de8\u5883\u5962\u4f88\u54c1\u7535\u5546",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,81,139)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,74,48)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,64,109)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u725b\u4e91\u96c6\u9879\u76ee\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,32,39)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,8,69)"
                        }
                    }
                },
                {
                    "name": "\u522b\u518d\u9519\u8fc7Lazada",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,99,94)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,100,88)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,30,12)"
                        }
                    }
                },
                {
                    "name": "\u751f\u65e5\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,133,90)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,95,63)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883\u5bbd\u677e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,79,0)"
                        }
                    }
                },
                {
                    "name": "\u5f39\u6027\u5de5\u4f5c\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,131,46)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6311\u6218\u548c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,90,43)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u533b\u7597\u9886\u5934\u7f8a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(118,26,59)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u676d\u5dde\u5b9e\u5728\u667a\u80fd\u79d1\u6280\u6709\u9650\u516c\u53f8\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,27,137)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u9886",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,127,98)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,57,26)"
                        }
                    }
                },
                {
                    "name": "007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,150,151)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,62,146)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u4e1c\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,80,112)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,40,107)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u53d1\u5c55\u9636\u6bb5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,136,115)"
                        }
                    }
                },
                {
                    "name": "AI\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,157,143)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u578b\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,136,82)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u65b0\u6280\u672f\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,4,81)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e\u7814\u7a76\u9662",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,12,134)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u9614\u51ed\u9c7c\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,87,108)"
                        }
                    }
                },
                {
                    "name": "\u5404\u79cd\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,106,120)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u6587\u5316\u56e2\u961fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(116,61,70)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,28,112)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,27,101)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,51,32)"
                        }
                    }
                },
                {
                    "name": "\u767e\u4eba\u6280\u672f\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,113,154)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,96,142)"
                        }
                    }
                },
                {
                    "name": "\u5ba2\u6237\u8986\u76d6\u591a\u5bb6\u4e00\u7ebf\u5de8\u5934\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,68,45)"
                        }
                    }
                },
                {
                    "name": "\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,159,113)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u623f\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,86,133)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u5a92\u4f53/\u7535\u89c6\u53f0/\u4e92\u8054\u7f51",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,25,101)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5f71\u50cf\u884c\u4e1a\u7fd8\u695a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,123,152)"
                        }
                    }
                },
                {
                    "name": "\u8d1f\u8d23\u641c\u72d7\u6570\u5b57\u4eba\u76843D\u4eba\u8138\u7b97\u6cd5\u65b9\u9762\u7684\u7814\u7a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,23,150)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,68,103)"
                        }
                    }
                },
                {
                    "name": "\u535a\u58eb\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,103,29)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u9910\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,70,106)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,61,26)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u4e0e\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,79,93)"
                        }
                    }
                },
                {
                    "name": "\u5343\u4e07\u7ea7\u7528\u6237\u7684\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,12,42)"
                        }
                    }
                },
                {
                    "name": "\u8ddf\u725b\u4eba\u4e00\u8d77\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,16,94)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989c\u503c\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,144,30)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,75,118)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u8fd8\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,39,66)"
                        }
                    }
                },
                {
                    "name": "\u5982\u679c\u4f60\u6b63\u5728\u8ffd\u68a6\u7684\u8def\u4e0a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,82,64)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,73,105)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,13,29)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,125,21)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,98,109)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,23,91)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4e24\u4f4d\u79d1\u5b66\u5bb6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,152,153)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u8d2d\u4e70\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,112,40)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,124,147)"
                        }
                    }
                },
                {
                    "name": "\u5b5d\u987a\u57fa\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,145,59)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,88,143)"
                        }
                    }
                },
                {
                    "name": "\u6709\u826f\u597d\u7684\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,6,76)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,74,85)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,10,59)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u4e1a\u52a1\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,108,53)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u673a\u5668\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,74,12)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5bb6\u91cd\u70b9\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,116,68)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,139,100)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,142,100)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u8f7b\u56e2\u961f\u5e26\u85aa\u5e74\u5047\u505a\u4e94\u4f11\u4e8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,136,38)"
                        }
                    }
                },
                {
                    "name": "\u5546\u4e1a\u6c14\u8c61\u5934\u90e8\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,102,131)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,26,75)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u664b\u5347\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,142,33)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u7b97\u6cd5\u9a71\u52a8\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,103,93)"
                        }
                    }
                },
                {
                    "name": "AI\u7b97\u6cd5\u843d\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,123,35)"
                        }
                    }
                },
                {
                    "name": "\u81ea\u6211\u53d1\u6398",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,31,21)"
                        }
                    }
                },
                {
                    "name": "\u63a2\u7d22\u524d\u6cbf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,58,23)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5e26\u85aa\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,89,128)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u699c****",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,75,130)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,49,62)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u9760",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,99,129)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677fnice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,86,86)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,18,37)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u957f\u5047\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,28,111)"
                        }
                    }
                },
                {
                    "name": "\u5b9a\u5047\u65e5\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,111,37)"
                        }
                    }
                },
                {
                    "name": "0-1\u65b0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,40,156)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u9879\u76ee\u6709\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,85,6)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,100,32)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,121,63)"
                        }
                    }
                },
                {
                    "name": "\u521b\u9020\u524d\u6cbfAI\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,60,106)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u538b\u529b\u5c0f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,114,24)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u6df1\u5927\u725b\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,6,149)"
                        }
                    }
                },
                {
                    "name": "\u5c11\u52a0\u73ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,58,65)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,60,160)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u548c\u5e26\u85aa\u75c5\u5047\u540415\u5929",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,95,44)"
                        }
                    }
                },
                {
                    "name": "\u5e26\u85aa\u5e74\u5047\u8bd5\u7528\u671f\u540c\u85aa\u4e94\u9669\u4e00\u91d1\u957f\u671f\u6fc0\u52b1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,20,96)"
                        }
                    }
                },
                {
                    "name": "\u6253\u8f66\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,97,153)"
                        }
                    }
                },
                {
                    "name": "\u91cd\u70b9\u53d1\u5c55\u7684\u53d8\u73b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,10,126)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,156,29)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u786c\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,134,31)"
                        }
                    }
                },
                {
                    "name": "\u5177\u6709\u5e02\u573a\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,85,145)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(120,33,7)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5148\u8fdb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,38,65)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5c0f\u800c\u7cbe",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,100,45)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u8350\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,85,140)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u56e2\u5efa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,85,11)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f\u975e\u5e38\u597d\u3002\u5458\u5de5\u85aa\u8d44\u798f\u5229\u5f88\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,27,158)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u7ea2\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,137,82)"
                        }
                    }
                },
                {
                    "name": "\u6c14\u6c1b\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,149,104)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,97,150)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,88,84)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u5e7f\u544a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,111,58)"
                        }
                    }
                },
                {
                    "name": "\u7814\u7a76\u548c\u5b9e\u9645\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,112,72)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u65e0\u9650\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,109,134)"
                        }
                    }
                },
                {
                    "name": "\u6d59\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,39,82)"
                        }
                    }
                },
                {
                    "name": "AI\u672a\u6765",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,147,75)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,10,114)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u4e1a\u56fe\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,133,136)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5e38\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,156,2)"
                        }
                    }
                },
                {
                    "name": "\u5145\u6ee1\u6d3b\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,101,114)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,157,48)"
                        }
                    }
                },
                {
                    "name": "slam\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,28,108)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6e38\u620f\u5927\u5382",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,64,76)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,43,117)"
                        }
                    }
                },
                {
                    "name": "Pro\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,130,57)"
                        }
                    }
                },
                {
                    "name": "\u4f18\u79c0\u5019\u9009\u4eba\u53ef\u4ee5\u6210\u4e3a\u6280\u672f\u5408\u4f19\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,74,130)"
                        }
                    }
                },
                {
                    "name": "\u5df2\u83b7\u591a\u5bb6\u4e00\u7ebfVC\u6295\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,16,134)"
                        }
                    }
                },
                {
                    "name": "\u5927\u4f6c\u5e26",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,13,72)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5b9e\u529b\uff1a\u957f\u671f\u6280\u672f\u79ef\u6dc0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,16,154)"
                        }
                    }
                },
                {
                    "name": "\u73af\u5883open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,115,136)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u4f01\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,58,24)"
                        }
                    }
                },
                {
                    "name": "14-18\u85aa+\u4e30\u539a\u798f\u5229",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,138,142)"
                        }
                    }
                },
                {
                    "name": "\u6d53\u539a\u7684\u6280\u672f\u5b66\u4e60\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,85,122)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,107,109)"
                        }
                    }
                },
                {
                    "name": "\u5171\u540c\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,49,25)"
                        }
                    }
                },
                {
                    "name": "\u597d\u73a9\u7684\u6e38\u620f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,105,136)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,155,37)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u98df\u5bbf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,64,38)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u6280\u672f\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,137,28)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1a\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,99,41)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f17\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(141,26,114)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u6325\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,134,156)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u798f\u5229\u5f85\u9047\u4f18\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,73,117)"
                        }
                    }
                },
                {
                    "name": "\u6570\u636e\u91cf\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,57,47)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u9614\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,8,119)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u8c08\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,20,48)"
                        }
                    }
                },
                {
                    "name": "\u6587\u827a\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,90,110)"
                        }
                    }
                },
                {
                    "name": "A\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,58,20)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956+\u53cc\u4f11+\u516d\u9669\u4e00\u91d1+\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,17,130)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u672f\u548c\u5de5\u4f5c\u80cc\u666f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,125,59)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u65b9\u5f0f\u7075\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,70,129)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5496\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(105,129,146)"
                        }
                    }
                },
                {
                    "name": "\u6e05\u534e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,67,149)"
                        }
                    }
                },
                {
                    "name": "CBA\u660e\u661f\u521b\u4e1a\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,54,96)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u9690\u5f62**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,116,60)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,116,52)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u671f\u521b\u4e1a\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,53,144)"
                        }
                    }
                },
                {
                    "name": "\u5404\u7c7b\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,16,48)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u8d5b\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,147,62)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,153,137)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,153,27)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df10+\u7ecf\u9a8c\u7b97\u6cd5\u548cC++\u7684\u53cc\u5bfc\u5e08\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,105,51)"
                        }
                    }
                },
                {
                    "name": "\u6559\u80b2\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,12,127)"
                        }
                    }
                },
                {
                    "name": "\u670d\u52a1\u5168\u7403\u5316\u548c\u591a\u6d3b\u6280\u672f\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,44,108)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u8c03\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,145,43)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4e0e\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,141,1)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,98,154)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u5f88\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,97,74)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5e73\u53f0\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,94,25)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u771f\u8bda",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,58,123)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u6d53\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(48,4,78)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9ad8\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,14,16)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u7684\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,80,116)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,25,154)"
                        }
                    }
                },
                {
                    "name": "\u98df\u5802\u7528\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,144,137)"
                        }
                    }
                },
                {
                    "name": "\u957f\u5b89\u6c7d\u8f66\uff08\u730e\u5934\u5c97\u4f4d\uff09",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,148,57)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4ece\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,94,111)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,65,68)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u6307\u5bfc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,155,89)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u53ef\u89c2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,72,152)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u5e02\u573a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,25,139)"
                        }
                    }
                },
                {
                    "name": "\u65e0007",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,39,122)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(3,101,57)"
                        }
                    }
                },
                {
                    "name": "\u6311\u6218\u81ea\u6211",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,112,94)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u591a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,57,129)"
                        }
                    }
                },
                {
                    "name": "\u91c7\u7f16\u5236\u64ad\u5b58",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,122,29)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u573a\u9762\u8bd5\u6d41\u7a0b\u4e00\u6b21\u8d70\u5b8c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,47,54)"
                        }
                    }
                },
                {
                    "name": "\u8fd1\u4e07\u4eba\u89c4\u6a21",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,148,27)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u6216\u4ea4\u901a\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,16,117)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u6709\u529b\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,66,141)"
                        }
                    }
                },
                {
                    "name": "\u505a\u6700\u524d\u6cbf\u7684\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,70,140)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,107,156)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,153,4)"
                        }
                    }
                },
                {
                    "name": "\u6e38\u620fUGC",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,7,150)"
                        }
                    }
                },
                {
                    "name": "\u9633\u5149\u900f\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,75,22)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5\u5f00\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,132,113)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5f85\u9047\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,69,99)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u533b\u7597",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,120,57)"
                        }
                    }
                },
                {
                    "name": "\u76ee\u6807\u5e74\u7ec8\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,75,150)"
                        }
                    }
                },
                {
                    "name": "\u4e30\u5bcc\u7684\u5458\u5de5\u6d3b\u52a8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,119,93)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,153,128)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,31,55)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5e74\u4e24\u6b21\u8c03\u85aa\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,149,68)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(9,141,146)"
                        }
                    }
                },
                {
                    "name": "\u4e0b\u5348\u8336\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,144,4)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u7ee9\u4f18\u79c0+\u5e74\u7ec8\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,1,14)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,81,128)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u5927\u6570\u636e\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,60,88)"
                        }
                    }
                },
                {
                    "name": "\u641c\u72d7\u5730\u56fe\u6838\u5fc3\u4e1a\u52a1\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,46,2)"
                        }
                    }
                },
                {
                    "name": "\u5341\u56db\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,13,56)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u4eba\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,66,39)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u673a\u5236\u8f83\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,132,47)"
                        }
                    }
                },
                {
                    "name": "\u51fa\u56fd\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,50,39)"
                        }
                    }
                },
                {
                    "name": "\u9910\u8865\u8bdd\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,54,31)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u6da8\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,134,125)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u5927\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,125,126)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u4f9b\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,60,152)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,116,61)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316\u7684\u4f01\u4e1a\u7ba1\u7406\u65b9\u5f0f\u548c\u8f7b\u677e\u6d3b\u6cfc\u7684\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,145,94)"
                        }
                    }
                },
                {
                    "name": "9\u70b9\u6253\u8f66\u62a5\u9500",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,63,153)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,135,47)"
                        }
                    }
                },
                {
                    "name": "\u5e7f\u6cdb\u6210\u957f\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(142,150,0)"
                        }
                    }
                },
                {
                    "name": "\u8c03\u85aa\u673a\u5236",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,66,2)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8fc7\u4ebf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,18,81)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u5148\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,122,29)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,101,103)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,108,115)"
                        }
                    }
                },
                {
                    "name": "\u5305\u5403\u5305\u4f4f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,98,117)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,26,125)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u90e8\u95e8\u6838\u5fc3\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,152,71)"
                        }
                    }
                },
                {
                    "name": "\u534e\u5927\u57fa\u56e0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,159,140)"
                        }
                    }
                },
                {
                    "name": "\u6709\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,86,77)"
                        }
                    }
                },
                {
                    "name": "\u660e\u661f\u8d44\u672c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,100,19)"
                        }
                    }
                },
                {
                    "name": "\u7f51\u6613\u6709\u9053",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,56,98)"
                        }
                    }
                },
                {
                    "name": "\u97f3\u89c6\u9891\u9886\u57df\u7814\u53d1\u9886\u5148",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,56,35)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u591a\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,26,84)"
                        }
                    }
                },
                {
                    "name": "\u4e03\u9669\u4e8c\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(154,125,152)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e9514\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,133,101)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u4e00\u4ee3\u6587\u5a31\u98ce\u53e3\u9886\u822a\u8005",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,121,36)"
                        }
                    }
                },
                {
                    "name": "\u5185\u90e8\u53d1\u5c55\u7a7a\u95f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,38,71)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4\u68d2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,131,77)"
                        }
                    }
                },
                {
                    "name": "\u4e91\u89c6\u9891",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,48,71)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(52,29,121)"
                        }
                    }
                },
                {
                    "name": "\u7ee9\u6548\u5956\u91d1\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,156,110)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,153,100)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,101,26)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4OPEN",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,50,69)"
                        }
                    }
                },
                {
                    "name": "\u5927\u725b\u5e26\u961f\uff01\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,116,90)"
                        }
                    }
                },
                {
                    "name": "\u6709\u6311\u6218",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,87,31)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,102,41)"
                        }
                    }
                },
                {
                    "name": "\u811a\u8e0f\u5b9e\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,84,110)"
                        }
                    }
                },
                {
                    "name": "\u878d\u8d44\u8d8510\u4ebf\u7f8e\u5143",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,106,15)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(153,79,124)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u578b\u7ec4\u7ec7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(21,114,90)"
                        }
                    }
                },
                {
                    "name": "\u5916\u4f01\u98ce\u683c\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,52,106)"
                        }
                    }
                },
                {
                    "name": "\u5bbd\u5e7f\u7684\u53d1\u5c55\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,30,8)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u5de5\u4f5c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(74,87,134)"
                        }
                    }
                },
                {
                    "name": "\u6625\u8282\u957f\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,149,1)"
                        }
                    }
                },
                {
                    "name": "\u624e\u624e\u5b9e\u5b9e\u505a\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(91,133,118)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u80fd\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,1,29)"
                        }
                    }
                },
                {
                    "name": "\u4e0d\u5b9a\u671f\u6280\u672f\u4ea4\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,133,79)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u5b9e\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,93,52)"
                        }
                    }
                },
                {
                    "name": "\u8f6c\u6b63\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(115,68,143)"
                        }
                    }
                },
                {
                    "name": "\u89c6\u9891\u63a8\u8350\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,148,93)"
                        }
                    }
                },
                {
                    "name": "\u51c6\u5907\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,129,26)"
                        }
                    }
                },
                {
                    "name": "\u7b80\u5355\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(8,138,137)"
                        }
                    }
                },
                {
                    "name": "\u961f\u53cb\u5948\u65af",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(95,69,102)"
                        }
                    }
                },
                {
                    "name": "\u6c1b\u56f4Nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,0,92)"
                        }
                    }
                },
                {
                    "name": "***\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,110,37)"
                        }
                    }
                },
                {
                    "name": "\u7eff\u8c37\u5236\u836f\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,156,84)"
                        }
                    }
                },
                {
                    "name": "\u4fe1\u606f\u5b89\u5168\u4e1a\u52a1\u5b89\u5168\u65b9\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(39,14,53)"
                        }
                    }
                },
                {
                    "name": "\u8db3\u989d\u4fdd\u9669\u516c\u79ef\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,137,67)"
                        }
                    }
                },
                {
                    "name": "B\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(155,146,73)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,150,11)"
                        }
                    }
                },
                {
                    "name": "**\u751f\u7269\u533b\u5b66\u4fe1\u606f\u4e13\u5bb6\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,8,143)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u9650\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,68,56)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1;\u8282\u65e5\u8865\u8d34;\u7ee9\u6548\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(133,3,70)"
                        }
                    }
                },
                {
                    "name": "\u80a1\u6743\u8ba1\u5212",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,77,139)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u4ea4\u8865",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,48,52)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,73,21)"
                        }
                    }
                },
                {
                    "name": "\u7528\u6237\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,10,67)"
                        }
                    }
                },
                {
                    "name": "\u3010\u6b63\u96c5\u9f7f\u79d1\u3011\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,69,79)"
                        }
                    }
                },
                {
                    "name": "\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,68,31)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(84,102,129)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u793c\u7269",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,159,85)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u51fa\u6d77\u4f01\u4e1a\u6807\u6746",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,45,153)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u50478\u5929\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,54,98)"
                        }
                    }
                },
                {
                    "name": "E\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(26,71,114)"
                        }
                    }
                },
                {
                    "name": "C\u8f6e\u878d\u8d44",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,144,28)"
                        }
                    }
                },
                {
                    "name": "\u5c97\u4f4d\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(134,123,12)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u4e00\u6d41",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,137,20)"
                        }
                    }
                },
                {
                    "name": "\u72ec\u7acb\u8d1f\u8d23",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(43,119,73)"
                        }
                    }
                },
                {
                    "name": "\u7528\u524d\u6cbf\u6280\u672f\u53d8\u9769\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,155,137)"
                        }
                    }
                },
                {
                    "name": "AI\u667a\u80fd\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,62,120)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u5373\u4e0a\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(38,93,98)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u7a33\u5b9a\u5feb\u901f\u589e\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(73,95,15)"
                        }
                    }
                },
                {
                    "name": "\u65b0\u96f6\u552e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,114,107)"
                        }
                    }
                },
                {
                    "name": "\u6301\u7eed\u521b\u65b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,36,54)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u5de8\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,58,157)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u4e0b\u5348\u8336outing\u4e0d\u505c\u6b47",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,31,35)"
                        }
                    }
                },
                {
                    "name": "\u540c\u4e8b\u597d\u76f8\u5904",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,130,84)"
                        }
                    }
                },
                {
                    "name": "\u5f3a\u5927\u7684\u56e2\u961f\u5de5\u7a0b\u548c\u7b97\u6cd5\u5b9e\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(109,156,115)"
                        }
                    }
                },
                {
                    "name": "\u9769\u65b0\u7684\u9879\u76ee\u673a\u4f1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,86,113)"
                        }
                    }
                },
                {
                    "name": "\u53cc\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(33,107,86)"
                        }
                    }
                },
                {
                    "name": "\u603b\u5e74\u85aa32-80\u4e07",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,70,108)"
                        }
                    }
                },
                {
                    "name": "\u5373\u5c06\u4e0a\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,137,31)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,7,37)"
                        }
                    }
                },
                {
                    "name": "\u5927\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,103,19)"
                        }
                    }
                },
                {
                    "name": "\u672a\u6765\u53ef\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(135,122,151)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f73\u7b49\u7b49",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,91,147)"
                        }
                    }
                },
                {
                    "name": "\u8d85\u6709\u7231\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,110,142)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,3,152)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5458mac",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,79,35)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u98ce\u6295\u52a0\u6301",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,37,133)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u989d\u9910\u8865/TB\u8d39\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,157,33)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u53d1\u5c55\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,34,18)"
                        }
                    }
                },
                {
                    "name": "\u5c0f\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,126,137)"
                        }
                    }
                },
                {
                    "name": "\u4e13\u4e1a\u4e13\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,55,73)"
                        }
                    }
                },
                {
                    "name": "\u516d\u9669\u4e00\u91d1\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,114,36)"
                        }
                    }
                },
                {
                    "name": "\u6709\u80a1\u7968\u671f\u6743\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,75,14)"
                        }
                    }
                },
                {
                    "name": "15-20\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,22,18)"
                        }
                    }
                },
                {
                    "name": "\u821e\u53f0\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,48,93)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,4,30)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4f4d\u7a33\u5b9a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,141,124)"
                        }
                    }
                },
                {
                    "name": "\u9ed1\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,111,70)"
                        }
                    }
                },
                {
                    "name": "\u4ebf\u7ea7\u65e5\u6d3b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(30,118,14)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,95,69)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98df\u5802",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,87,66)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u5e94\u7528",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,79,128)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u6e38\u6216\u6237\u5916\u62d3\u5c55\u57f9\u8bad",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,73,91)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5916\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(130,23,154)"
                        }
                    }
                },
                {
                    "name": "\u7814\u53d1\u4eba\u5458300\u4eba",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,112,62)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u4f18\u52bf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,54,34)"
                        }
                    }
                },
                {
                    "name": "\u65e5\u6570\u636e\u767e\u4ebf\u7ea7",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,56,140)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(119,145,16)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u5bf9\u4e00\u5e26\u6559",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,78,18)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u89c4\u6a21\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,23,143)"
                        }
                    }
                },
                {
                    "name": "\u6709XLNet\u4e00\u4f5c\u5927\u795e\u5e26\u60a8\u5728\u7b97\u6cd5\u91cc\u6df1\u8015",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,146,124)"
                        }
                    }
                },
                {
                    "name": "\u505a\u4e8b\u81ea\u7531\u5ea6\u8db3\u591f\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,66,124)"
                        }
                    }
                },
                {
                    "name": "\u8001\u677f\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,31,31)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u754c\u4e0e\u5b66\u672f\u754c\u76f8\u7ed3\u5408\u7684\u6700\u4f73\u9635\u5730",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,51,107)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f00\u653e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,66,53)"
                        }
                    }
                },
                {
                    "name": "\u4e2d\u5916\u5408\u8d44\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,50,159)"
                        }
                    }
                },
                {
                    "name": "\u6211\u53f8\u4e0e\u4eac\u4e1c\u96f6\u552e\u5408\u4f5c\u62db\u52df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(68,64,28)"
                        }
                    }
                },
                {
                    "name": "\u817e\u8baf\u97f3\u4e50\u730e\u5934\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,99,134)"
                        }
                    }
                },
                {
                    "name": "\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,45,43)"
                        }
                    }
                },
                {
                    "name": "\u6709\u4eba\u624d\u4f4f\u623f\u63d0\u4f9b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(117,134,124)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u6c1b\u56f4\u7b80\u5355",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,95,3)"
                        }
                    }
                },
                {
                    "name": "\u6f5c\u529b\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(31,62,87)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6e29\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,51,123)"
                        }
                    }
                },
                {
                    "name": "\u4f4f\u623f\u514d\u606f\u8d37",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,91,123)"
                        }
                    }
                },
                {
                    "name": "\u7d27\u6025",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,33,121)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f18",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(132,36,51)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u5065\u8eab\u623f\u7b49\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,126,78)"
                        }
                    }
                },
                {
                    "name": "\u5165\u804c\u83b7\u5f97\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(41,69,139)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u56e2\u961f\u4f18\u79c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,60,73)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(83,20,32)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,119,92)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,104,148)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u8d70\u8fdb\u5343\u5bb6\u4e07\u6237",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,84,133)"
                        }
                    }
                },
                {
                    "name": "\u6838\u5fc3\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,157,142)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u94fe\u91d1\u878d\u79d1\u6280\u5934\u90e8\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(25,68,22)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5165\u63a5\u89e6\u4e1a\u754c\u6700\u524d\u6cbf\u4eba\u5de5\u667a\u80fd\u6838\u5fc3\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(113,62,142)"
                        }
                    }
                },
                {
                    "name": "\u7535\u89c6\u53f0\u4e1a\u52a1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(88,144,85)"
                        }
                    }
                },
                {
                    "name": "\u7ed3\u679c\u5bfc\u5411",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(19,8,136)"
                        }
                    }
                },
                {
                    "name": "\u63a8\u52a8\u4e2d\u56fd\u533b\u7597\u6539\u53d8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,37,110)"
                        }
                    }
                },
                {
                    "name": "\u76f4\u63a5\u8ddf\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(102,34,61)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u5f52\u79d1\u7814\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,73,66)"
                        }
                    }
                },
                {
                    "name": "\u53ef\u53e3\u5348\u665a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,0,71)"
                        }
                    }
                },
                {
                    "name": "\u7cbe\u81f4\u8212\u9002\u7684\u529e\u516c\u73af\u5883",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,91,123)"
                        }
                    }
                },
                {
                    "name": "\u8f85\u52a9\u9a7e\u9a76",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,51,140)"
                        }
                    }
                },
                {
                    "name": "\u771f\u5b9e\u4e30\u5bcc\u7684\u5e94\u7528\u573a\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,32,133)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(65,109,11)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,18,144)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u524d\u666f\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(78,99,105)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5927\u795e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,135,22)"
                        }
                    }
                },
                {
                    "name": "\u5168\u989d\u793e\u4fdd",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(6,55,83)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u5e26\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,51,77)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u5185\u4ea7\u54c1\u5f71\u54cd\u529b\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,16,18)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(55,16,57)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u725b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,109,19)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6c1b\u56f4\u5411\u4e0a\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,54,88)"
                        }
                    }
                },
                {
                    "name": "\u725b\u4eba\u56e2\u961f\u80cc\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(143,152,62)"
                        }
                    }
                },
                {
                    "name": "\u7075\u6d3b\u5de5\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(46,6,65)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u81ea\u6211\u5b66\u4e60",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,59,160)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u5feb\u901f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,110,32)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,3,107)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u7f51\u8054",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,155,86)"
                        }
                    }
                },
                {
                    "name": "\u4f01\u4e1a\u5feb\u901f\u6210\u957f\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,159,104)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u53d1\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,123,11)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u9645\u5316\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,22,17)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,22,98)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4e1a\u9886\u57df\u7684\u4eba\u5de5\u667a\u80fd\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,44,32)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e94\u8fbe\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,55,91)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u9a71\u52a8\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,29,80)"
                        }
                    }
                },
                {
                    "name": "90\u540e\u5e74\u8f7b\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,159,142)"
                        }
                    }
                },
                {
                    "name": "\u52a0\u73ed\u8d39\u53e6\u7b97",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,19,151)"
                        }
                    }
                },
                {
                    "name": "\u4f9b\u5e94\u4e09\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,6,93)"
                        }
                    }
                },
                {
                    "name": "\u8282\u65e5\u798f\u5229\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(58,125,103)"
                        }
                    }
                },
                {
                    "name": "\u5468\u672b\u53cc\u4f118\u5c0f\u65f6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,41,95)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u85aa\u7b97\u6cd5\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,50,50)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,160,98)"
                        }
                    }
                },
                {
                    "name": "\u673a\u5668\u4eba\u884c\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,118,119)"
                        }
                    }
                },
                {
                    "name": "\u6ce8\u91cd\u4e2a\u4eba\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,46,97)"
                        }
                    }
                },
                {
                    "name": "\u963f\u91cc\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,147,140)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u4e60\u8bc1\u660e",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,13,42)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,28,68)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u6709\u7ade\u4e89\u529b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,41,92)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u73af\u5883\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(10,27,14)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u6838\u5fc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,135,151)"
                        }
                    }
                },
                {
                    "name": "\u96f6\u98df\u996e\u6599\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,128,150)"
                        }
                    }
                },
                {
                    "name": "\u4e94\u9669\u4e00\u91d1\u4e00\u6863",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(27,64,23)"
                        }
                    }
                },
                {
                    "name": "\u6ca1\u6709KPI",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,48,19)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5206\u4eab",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,37,53)"
                        }
                    }
                },
                {
                    "name": "AI\u72ec\u89d2\u517d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,1,66)"
                        }
                    }
                },
                {
                    "name": "\u8f6f\u4ef6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,66,104)"
                        }
                    }
                },
                {
                    "name": "\u90e8\u95e8\u4f18\u80dc\u5956",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,59,18)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u6625\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,67,46)"
                        }
                    }
                },
                {
                    "name": "500\u5f3a\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(63,53,116)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(2,32,159)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5148\u7684\u4eba\u5de5\u667a\u80fd\u5b66\u4e60\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,95,4)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,82,24)"
                        }
                    }
                },
                {
                    "name": "1.\u56e2\u961f\u4e1a\u52a1\u7d27\u8ddf\u96c6\u56e2\u7684\u4e1a\u52a1\u76ee\u6807",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,143,141)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(157,158,59)"
                        }
                    }
                },
                {
                    "name": "\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,5,129)"
                        }
                    }
                },
                {
                    "name": "\u6d77\u91cf\u6d41\u91cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,148,57)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u80a1\u4e1c\u9760\u8c31",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,91,131)"
                        }
                    }
                },
                {
                    "name": "\u56fa\u5b9a\u53cc\u4f11",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,22,141)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u54c8\u5570\u51fa\u884c\u8054\u5408\u62db\u8058",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,28,24)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,56,37)"
                        }
                    }
                },
                {
                    "name": "nice",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,157,94)"
                        }
                    }
                },
                {
                    "name": "\u6df1\u5ea6\u5b66\u4e60\u5c97\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,119,132)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0\u805a\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(126,152,43)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(77,139,153)"
                        }
                    }
                },
                {
                    "name": "\u884c\u4e1a\u9886\u519b\u4f01\u4e1a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(79,4,119)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5185**\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,0,46)"
                        }
                    }
                },
                {
                    "name": "\u6241\u5e73\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,55,49)"
                        }
                    }
                },
                {
                    "name": "\u5927\u5382\u798f\u5229\u5f85\u9047\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,53,82)"
                        }
                    }
                },
                {
                    "name": "\u5956\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,72,153)"
                        }
                    }
                },
                {
                    "name": "\u805a\u4e00\u7fa4\u6709\u60c5\u4e49\u7684\u4eba\u505a\u6210\u6709\u610f\u4e49\u7684\u4e8b\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,88,98)"
                        }
                    }
                },
                {
                    "name": "\u9886\u5bfcNic",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(35,106,114)"
                        }
                    }
                },
                {
                    "name": "\u5496\u5561\u6c34\u679c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(146,81,110)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u98de\u901f\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,28,43)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u6210\u957f\u6027",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,13,117)"
                        }
                    }
                },
                {
                    "name": "\u5bfc\u5e08\u4e00\u5e26\u4e00",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(29,4,6)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u524d\u666f\u4e0d\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,31,146)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u5e74\u8f7b\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(54,120,32)"
                        }
                    }
                },
                {
                    "name": "6\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(64,58,149)"
                        }
                    }
                },
                {
                    "name": "\u80cc\u666f\u6280\u672f\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(111,80,157)"
                        }
                    }
                },
                {
                    "name": "\u590d\u6742\u7cfb\u7edf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(28,132,110)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,36,95)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u5e74\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,156,89)"
                        }
                    }
                },
                {
                    "name": "\u6253\u9020\u4e16\u754c**\u7684\u6df7\u6c8c\u5de5\u7a0b\u4e50\u56ed",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,137,32)"
                        }
                    }
                },
                {
                    "name": "\u5feb\u901f\u7684\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,60,127)"
                        }
                    }
                },
                {
                    "name": "\u65bd\u5c55\u7a7a\u95f4\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(93,102,116)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u9886\u5148\u5546\u7528\u670d\u52a1\u673a\u5668\u4eba\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,149,39)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u7ec8\u5956\u516d\u9669\u4e00\u91d1\u996d\u8d34\u8f66\u8d34\u7ee9\u6548\u5956\u5b9a\u671f\u4f53\u68c0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(42,106,108)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u914d\u7f6e\u671f\u6743",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,1,145)"
                        }
                    }
                },
                {
                    "name": "AI\u4ea7\u54c1\u7814\u53d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(34,144,160)"
                        }
                    }
                },
                {
                    "name": "\u7b97\u6cd5\u5b9e\u4e60\u751f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,159,90)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u8bd5\u9519",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(45,24,47)"
                        }
                    }
                },
                {
                    "name": "\u54e5\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(69,96,104)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u6c1b\u56f4\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(150,70,44)"
                        }
                    }
                },
                {
                    "name": "\u4f30\u503c\u8fd1\u767e\u4ebf\u7f8e\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,39,73)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u9738",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(18,96,114)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u4e16\u754c\u9886\u5148\u7684AI\u7814\u53d1\u56e2\u961f\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,105,65)"
                        }
                    }
                },
                {
                    "name": "\u5305\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(145,4,48)"
                        }
                    }
                },
                {
                    "name": "\u8865\u5145\u533b\u7597\u4fdd\u9669",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,96,117)"
                        }
                    }
                },
                {
                    "name": "\u7eaf\u6280\u672f\u80cc\u4e66\u7684\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,95,9)"
                        }
                    }
                },
                {
                    "name": "\u573a\u666f\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(75,106,23)"
                        }
                    }
                },
                {
                    "name": "\u524d\u6cbf\u79d1\u6280",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,4,134)"
                        }
                    }
                },
                {
                    "name": "\u5c31\u6765\u641c\u72d7\u5546\u4e1a\u641c\u7d22\u5427\uff01",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,100,148)"
                        }
                    }
                },
                {
                    "name": "\u9053\u8def\u68c0\u6d4b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,50,98)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u81ea\u7531\u5ea6\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,74,106)"
                        }
                    }
                },
                {
                    "name": "\u5de5\u4f5c\u6c1b\u56f4\u6d3b\u8dc3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,74,67)"
                        }
                    }
                },
                {
                    "name": "Geek\u6587\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,107,42)"
                        }
                    }
                },
                {
                    "name": "\u63d0\u5347\u4e2a\u4eba\u4ef7\u503c\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(128,129,40)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u524d\u77bb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(86,24,77)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u6ee1\u5206",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(56,50,101)"
                        }
                    }
                },
                {
                    "name": "\u56fd\u5b9a\u8282\u5047\u65e5\u653e\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(14,113,110)"
                        }
                    }
                },
                {
                    "name": "\u805a\u96c6\u540c\u884c\u4e1a\u9ad8\u6d45\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,99,131)"
                        }
                    }
                },
                {
                    "name": "\u8d44\u91d1\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(82,3,30)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u81ea\u52a9\u5348\u9910",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,127,19)"
                        }
                    }
                },
                {
                    "name": "\u664b\u5347\u89c4\u8303",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(137,19,144)"
                        }
                    }
                },
                {
                    "name": "\u804c\u4e1a\u53d1\u5c55\u826f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(13,146,13)"
                        }
                    }
                },
                {
                    "name": "\u533b\u7597\u56fe\u50cf",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,149,133)"
                        }
                    }
                },
                {
                    "name": "\u5305\u4e09\u9910\u96f6\u98df",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,121,143)"
                        }
                    }
                },
                {
                    "name": "\u6fc0\u52b1\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(85,13,113)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9886\u57df\u5927\u725b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,49,61)"
                        }
                    }
                },
                {
                    "name": "\u5065\u8eab\u623f\u8865\u8d34",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(149,71,106)"
                        }
                    }
                },
                {
                    "name": "\u5929\u9ad8\u4efb\u9e1f\u98de",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,85,29)"
                        }
                    }
                },
                {
                    "name": "\u53d1\u5c55\u7a7a\u95f4\u5e7f\u9614",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,32,28)"
                        }
                    }
                },
                {
                    "name": "7\u5c0f\u65f6\u5de5\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,34,58)"
                        }
                    }
                },
                {
                    "name": "\u9f13\u52b1\u7814\u7a76\u65b0\u6280\u672f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(101,131,149)"
                        }
                    }
                },
                {
                    "name": "\u4e1a\u52a1\u53d1\u5c55\u524d\u666f\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(152,98,97)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u7cbe\u6e5b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,60,126)"
                        }
                    }
                },
                {
                    "name": "\u79d1\u7814\u548c\u5e94\u7528\u7ed3\u5408",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(160,146,156)"
                        }
                    }
                },
                {
                    "name": "\u667a\u6167\u57ce\u5e02",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(53,139,149)"
                        }
                    }
                },
                {
                    "name": "\u65e0\u6742\u4e8b",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,72,152)"
                        }
                    }
                },
                {
                    "name": "\u4e0e\u5f88\u5f3a\u7684\u540c\u4e8b\u4e00\u8d77\u6210\u957f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(40,100,57)"
                        }
                    }
                },
                {
                    "name": "\u4f20\u97f3\u63a7\u80a1\u5168\u8d44\u5b50\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,74,65)"
                        }
                    }
                },
                {
                    "name": "\u5e02\u573a\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,113,47)"
                        }
                    }
                },
                {
                    "name": "open",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(129,124,114)"
                        }
                    }
                },
                {
                    "name": "\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(87,28,133)"
                        }
                    }
                },
                {
                    "name": "\u8c37\u6b4c\u7b49\u884c\u4e1a\u6700\u4f18\u79c0\u4eba\u624d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(89,61,62)"
                        }
                    }
                },
                {
                    "name": "\u7ec6\u5206\u9886\u57df\u884c\u4e1a**",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(148,76,0)"
                        }
                    }
                },
                {
                    "name": "\u516c\u53f8\u7814\u53d1\u5b9e\u529b\u5f3a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(61,101,46)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u5927\u5496\u4e91\u96c6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,20,150)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u597d\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,36,152)"
                        }
                    }
                },
                {
                    "name": "\u4f53\u68c0/\u5f39\u6027\u4e0a\u4e0b\u73ed/\u5e74\u7ec8\u7ee9\u6548/\u514d\u8d39\u5348\u665a\u9910\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(47,98,31)"
                        }
                    }
                },
                {
                    "name": "\u4e09\u9910\u514d\u8d39",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(22,85,48)"
                        }
                    }
                },
                {
                    "name": "LayaAir\u5f15\u64ce\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(70,156,160)"
                        }
                    }
                },
                {
                    "name": "\u4e0a\u5e02\u51c6\u5907\u671f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,27,126)"
                        }
                    }
                },
                {
                    "name": "\u8682\u8681\u96c6\u56e2",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(138,142,145)"
                        }
                    }
                },
                {
                    "name": "\u653f\u5e9c\u91cd\u70b9\u652f\u6301\u9879\u76ee",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(127,46,35)"
                        }
                    }
                },
                {
                    "name": "\u7ba1\u7406\u6241\u5e73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(11,30,19)"
                        }
                    }
                },
                {
                    "name": "10\u5929\u5e26\u85aa\u75c5\u5047",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(100,71,48)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5ea6\u7ee9\u6548",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(24,129,19)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u916c\u798f\u5229\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(92,118,56)"
                        }
                    }
                },
                {
                    "name": "\u5e74\u5e95\u53cc\u85aa-\u5e74\u7ec8\u5956-\u6241\u5e73\u5316\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,74,108)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u6027\u5316",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(0,78,72)"
                        }
                    }
                },
                {
                    "name": "\u5e73\u53f0\u6210\u719f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(110,108,70)"
                        }
                    }
                },
                {
                    "name": "\u667a\u80fd\u5236\u9020",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(20,32,39)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e742\u6b21\u8c03\u85aa\u7a97\u53e3",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,120,82)"
                        }
                    }
                },
                {
                    "name": "\u798f\u5229\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,106,48)"
                        }
                    }
                },
                {
                    "name": "\u5173\u6ce8\u5458\u5de5\u53d1\u5c55",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,51,88)"
                        }
                    }
                },
                {
                    "name": "\u4e92\u8054\u7f51\u91d1\u878d\u9886\u57df\u524d\u6cbf\u7b97\u6cd5\u7814\u7a76\u548c\u5b9e\u73b0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(112,72,20)"
                        }
                    }
                },
                {
                    "name": "\u514d\u8d39\u505c\u8f66",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(131,31,154)"
                        }
                    }
                },
                {
                    "name": "\u7f34\u7eb3\u4e94\u9669\u4e00\u91d1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(50,109,74)"
                        }
                    }
                },
                {
                    "name": "\u5458\u5de5\u65c5\u6e38\u4e0b\u5348\u8336",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(107,132,100)"
                        }
                    }
                },
                {
                    "name": "\u4ea7\u54c1\u7814\u53d1\u4eba\u6570\u5360\u6bd470%",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(23,135,153)"
                        }
                    }
                },
                {
                    "name": "\u8fdc\u7a0b\u529e\u516c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(159,44,129)"
                        }
                    }
                },
                {
                    "name": "\u504f\u5e73\u7ba1\u7406",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(67,48,24)"
                        }
                    }
                },
                {
                    "name": "\u5168\u5e7416-18\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(90,105,46)"
                        }
                    }
                },
                {
                    "name": "\u5f85\u9047\u4f73",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(5,118,46)"
                        }
                    }
                },
                {
                    "name": "\u6210\u957f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(94,60,128)"
                        }
                    }
                },
                {
                    "name": "\u9879\u76ee\u4e30\u5bcc",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,17,98)"
                        }
                    }
                },
                {
                    "name": "\u6280\u672f\u63d0\u5347\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(66,5,0)"
                        }
                    }
                },
                {
                    "name": "\u6bcf\u5e74\u591a\u6b21\u8c03\u85aa",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(125,94,43)"
                        }
                    }
                },
                {
                    "name": "\u7ade\u4e89\u529b\u7684\u85aa\u916c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(62,18,39)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u4ea7\u54c1",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(49,0,76)"
                        }
                    }
                },
                {
                    "name": "\u6587\u5316\u6c1b\u56f4",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(59,74,27)"
                        }
                    }
                },
                {
                    "name": "\u53cd\u9988\u5feb",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(81,139,117)"
                        }
                    }
                },
                {
                    "name": "\u521b\u65b0\u56e2\u961f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,37,73)"
                        }
                    }
                },
                {
                    "name": "\u9ad8\u53d1\u5c55\u524d\u666f",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(32,142,64)"
                        }
                    }
                },
                {
                    "name": "\u4eba\u5de5\u667a\u80fd\u9879\u76ee\u7814\u7a76\u524d\u6cbf\u7b97\u6cd5",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(147,79,64)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6210\u5458\u6765\u81ea\u56fd\u5185\u5916\u540d\u6821",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(51,70,68)"
                        }
                    }
                },
                {
                    "name": "\u85aa\u8d44\u5f85\u9047\u5f88\u9ad8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,26,85)"
                        }
                    }
                },
                {
                    "name": "\u826f\u597d\u7684\u884c\u4e1a\u524d\u666f\u3002",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(7,123,155)"
                        }
                    }
                },
                {
                    "name": "\u65c5\u884c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(96,25,6)"
                        }
                    }
                },
                {
                    "name": ".",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(114,137,11)"
                        }
                    }
                },
                {
                    "name": "\u5b66\u4e60\u673a\u4f1a\u591a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,77,80)"
                        }
                    }
                },
                {
                    "name": "\u4e00\u7ebf\u4e92\u8054\u7f51\u516c\u53f8\u7d27\u6025\u804c\u4f4d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(156,51,103)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u80cc\u666f\u5f3a\u5927",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(98,28,90)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u4eba\u5458\u5b9e\u529b\u96c4\u539a",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,141,137)"
                        }
                    }
                },
                {
                    "name": "\u5168\u7403\u6700\u5927\u4e09\u65b9\u5e7f\u544a\u5e73\u53f0",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(103,95,61)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6280\u672f\u6c1b\u56f4\u597d",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(57,50,83)"
                        }
                    }
                },
                {
                    "name": "**\u533b\u9662\u5408\u4f5c",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(17,70,89)"
                        }
                    }
                },
                {
                    "name": "\u56e2\u961f\u6709\u4f18\u5f02\u7684\u6280\u672f\u6df1\u5ea6",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(140,120,90)"
                        }
                    }
                },
                {
                    "name": "\u521b\u4e1aAI\u516c\u53f8",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(108,46,35)"
                        }
                    }
                },
                {
                    "name": "\u975e\u5916\u5305",
                    "value": 1,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(121,77,34)"
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
        chart_0f1ba153e9cd452c958efa8579768e62.setOption(option_0f1ba153e9cd452c958efa8579768e62);
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
