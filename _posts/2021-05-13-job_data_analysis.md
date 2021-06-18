---
title: 算法招聘数据分析
---



<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
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

<h2>（2021-06-18更新）</h2>

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
            <button class="tablinks" onclick="showChart(event, '5e02a56b80324ef180f84b610d1e7766')">薪资</button>
            <button class="tablinks" onclick="showChart(event, '87fe3fbdd2174c0fa1734041ab390c93')">实习薪资分布</button>
            <button class="tablinks" onclick="showChart(event, '2bc439eabae04850a7c98fc792f3bf1d')">社招薪资分布</button>
            <button class="tablinks" onclick="showChart(event, '934029527292470ca72c52d22d491b7b')">城市&薪资</button>
            <button class="tablinks" onclick="showChart(event, '64c48c03bcbc4508873dd952df2e8cfc')">薪资地图</button>
            <button class="tablinks" onclick="showChart(event, 'ce8f0f460166412dbf12b398ba2d592a')">区域&薪资</button>
            <button class="tablinks" onclick="showChart(event, '9e316c6369734fb1a172c8334b8b8301')">行业&薪资</button>
            <button class="tablinks" onclick="showChart(event, '95596c80032941c0a99c21d374f05c62')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'a675ea15cf0b41ffa59a4ba7d7e6062d')">学历&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'e40ca01e02994696a3b671d3df01e7e4')">经验&薪资</button>
            <button class="tablinks" onclick="showChart(event, '485766e1c53642bc907ce95881509e2a')">top10薪资招聘</button>
    </div>

    <div class="box">
                <div id="5e02a56b80324ef180f84b610d1e7766" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5e02a56b80324ef180f84b610d1e7766 = echarts.init(
            document.getElementById('5e02a56b80324ef180f84b610d1e7766'), 'white', {renderer: 'canvas'});
            
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
    
        var option_5e02a56b80324ef180f84b610d1e7766 = {
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
                320,
                192,
                158,
                133,
                92,
                85,
                77,
                62,
                60,
                48
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
                    "name": "20k-40k",
                    "value": 320
                },
                {
                    "name": "25k-50k",
                    "value": 192
                },
                {
                    "name": "15k-30k",
                    "value": 158
                },
                {
                    "name": "30k-60k",
                    "value": 133
                },
                {
                    "name": "30k-50k",
                    "value": 92
                },
                {
                    "name": "15k-25k",
                    "value": 85
                },
                {
                    "name": "20k-30k",
                    "value": 77
                },
                {
                    "name": "20k-35k",
                    "value": 62
                },
                {
                    "name": "25k-40k",
                    "value": 60
                },
                {
                    "name": "25k-45k",
                    "value": 48
                }
            ],
            "radius": [
                "10%",
                "35%"
            ],
            "center": [
                "70%",
                "25%"
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
                    "name": "20k-40k",
                    "value": 320
                },
                {
                    "name": "25k-50k",
                    "value": 192
                },
                {
                    "name": "15k-30k",
                    "value": 158
                },
                {
                    "name": "30k-60k",
                    "value": 133
                },
                {
                    "name": "30k-50k",
                    "value": 92
                },
                {
                    "name": "15k-25k",
                    "value": 85
                },
                {
                    "name": "20k-30k",
                    "value": 77
                },
                {
                    "name": "20k-35k",
                    "value": 62
                },
                {
                    "name": "25k-40k",
                    "value": 60
                },
                {
                    "name": "25k-45k",
                    "value": 48
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
                "20k-40k",
                "25k-50k",
                "15k-30k",
                "30k-60k",
                "30k-50k",
                "15k-25k",
                "20k-30k",
                "20k-35k",
                "25k-40k",
                "25k-45k"
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
                "20k-40k",
                "25k-50k",
                "15k-30k",
                "30k-60k",
                "30k-50k",
                "15k-25k",
                "20k-30k",
                "20k-35k",
                "25k-40k",
                "25k-45k"
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
            "text": "\u85aa\u8d44\u5206\u5e03",
            "subtext": "\u9ad8\u9891\u533a\u95f4\u6bb5\u5206\u5e03",
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
        chart_5e02a56b80324ef180f84b610d1e7766.setOption(option_5e02a56b80324ef180f84b610d1e7766);
    </script>
                <div id="87fe3fbdd2174c0fa1734041ab390c93" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_87fe3fbdd2174c0fa1734041ab390c93 = echarts.init(
            document.getElementById('87fe3fbdd2174c0fa1734041ab390c93'), 'white', {renderer: 'canvas'});
            
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
    
        var option_87fe3fbdd2174c0fa1734041ab390c93 = {
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
            "type": "boxplot",
            "name": "\u85aa\u8d44\u4e0b\u9650",
            "data": [
                [
                    2,
                    4.5,
                    8,
                    13.5,
                    30
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        },
        {
            "type": "boxplot",
            "name": "\u85aa\u8d44\u4e0a\u9650",
            "data": [
                [
                    3,
                    6.25,
                    11.5,
                    19.5,
                    50
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        },
        {
            "type": "boxplot",
            "name": "\u5e73\u5747\u85aa\u8d44",
            "data": [
                [
                    2.5,
                    5.0,
                    6.0,
                    8.0,
                    40.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44\u4e0b\u9650",
                "\u85aa\u8d44\u4e0a\u9650",
                "\u5e73\u5747\u85aa\u8d44"
            ],
            "selected": {
                "\u85aa\u8d44\u4e0b\u9650": true,
                "\u85aa\u8d44\u4e0a\u9650": true,
                "\u5e73\u5747\u85aa\u8d44": true
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
                "\u5b9e\u4e60\u85aa\u8d44"
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
            "text": "\u85aa\u8d44\u5206\u5e03",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_87fe3fbdd2174c0fa1734041ab390c93.setOption(option_87fe3fbdd2174c0fa1734041ab390c93);
    </script>
                <div id="2bc439eabae04850a7c98fc792f3bf1d" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_2bc439eabae04850a7c98fc792f3bf1d = echarts.init(
            document.getElementById('2bc439eabae04850a7c98fc792f3bf1d'), 'white', {renderer: 'canvas'});
            
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
    
        var option_2bc439eabae04850a7c98fc792f3bf1d = {
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
            "type": "boxplot",
            "name": "\u85aa\u8d44\u4e0b\u9650",
            "data": [
                [
                    8,
                    15.75,
                    24.5,
                    36.25,
                    70
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        },
        {
            "type": "boxplot",
            "name": "\u85aa\u8d44\u4e0a\u9650",
            "data": [
                [
                    15,
                    27.25,
                    41.0,
                    63.0,
                    120
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        },
        {
            "type": "boxplot",
            "name": "\u5e73\u5747\u85aa\u8d44",
            "data": [
                [
                    12.0,
                    24.5,
                    30.0,
                    40.0,
                    90.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44\u4e0b\u9650",
                "\u85aa\u8d44\u4e0a\u9650",
                "\u5e73\u5747\u85aa\u8d44"
            ],
            "selected": {
                "\u85aa\u8d44\u4e0b\u9650": true,
                "\u85aa\u8d44\u4e0a\u9650": true,
                "\u5e73\u5747\u85aa\u8d44": true
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
                "\u793e\u62db\u85aa\u8d44"
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
            "text": "\u85aa\u8d44\u5206\u5e03",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_2bc439eabae04850a7c98fc792f3bf1d.setOption(option_2bc439eabae04850a7c98fc792f3bf1d);
    </script>
                <div id="934029527292470ca72c52d22d491b7b" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_934029527292470ca72c52d22d491b7b = echarts.init(
            document.getElementById('934029527292470ca72c52d22d491b7b'), 'white', {renderer: 'canvas'});
        var option_934029527292470ca72c52d22d491b7b = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                35.0,
                30.0,
                30.0,
                30.0,
                25.0,
                22.5,
                20.0,
                30.0,
                30.0,
                20.0,
                20.0
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    12.0,
                    30.0,
                    35.0,
                    42.5,
                    90.0
                ],
                [
                    12.5,
                    25.0,
                    30.0,
                    40.0,
                    85.0
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    37.5,
                    90.0
                ],
                [
                    12.5,
                    23.5,
                    30.0,
                    40.0,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    25.0,
                    30.0,
                    70.0
                ],
                [
                    12.5,
                    20.0,
                    22.5,
                    27.5,
                    50.0
                ],
                [
                    12.5,
                    17.0,
                    20.0,
                    24.5,
                    37.5
                ],
                [
                    15.0,
                    20.0,
                    22.75,
                    30.0,
                    50.0
                ],
                [
                    19.5,
                    20.0,
                    30.0,
                    32.5,
                    35.0
                ],
                [
                    25.0,
                    30.0,
                    30.0,
                    37.5,
                    37.5
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u4f5b\u5c71",
                "\u897f\u5b89",
                "\u5408\u80a5"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_934029527292470ca72c52d22d491b7b.setOption(option_934029527292470ca72c52d22d491b7b);
    </script>
                <div id="64c48c03bcbc4508873dd952df2e8cfc" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_64c48c03bcbc4508873dd952df2e8cfc = echarts.init(
            document.getElementById('64c48c03bcbc4508873dd952df2e8cfc'), 'white', {renderer: 'canvas'});
            
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
    
        var option_64c48c03bcbc4508873dd952df2e8cfc = {
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
            "name": "\u57ce\u5e02\u85aa\u8d44\u5206\u5e03",
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
                        35.0
                    ]
                },
                {
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        30.0
                    ]
                },
                {
                    "name": "\u6df1\u5733",
                    "value": [
                        114.07,
                        22.62,
                        30.0
                    ]
                },
                {
                    "name": "\u676d\u5dde",
                    "value": [
                        120.19,
                        30.26,
                        30.0
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        25.0
                    ]
                },
                {
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        22.5
                    ]
                },
                {
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        20.0
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        30.0
                    ]
                },
                {
                    "name": "\u4f5b\u5c71",
                    "value": [
                        113.11,
                        23.05,
                        30.0
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        20.0
                    ]
                },
                {
                    "name": "\u5408\u80a5",
                    "value": [
                        117.27,
                        31.86,
                        20.0
                    ]
                },
                {
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        22.5
                    ]
                },
                {
                    "name": "\u5609\u5174",
                    "value": [
                        120.76,
                        30.77,
                        30.0
                    ]
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        15.0
                    ]
                },
                {
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        20.0
                    ]
                },
                {
                    "name": "\u60e0\u5dde",
                    "value": [
                        114.4,
                        23.09,
                        30.0
                    ]
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        15.0
                    ]
                },
                {
                    "name": "\u798f\u5dde",
                    "value": [
                        119.3,
                        26.08,
                        12.0
                    ]
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": [
                        113.75,
                        23.04,
                        21.0
                    ]
                },
                {
                    "name": "\u592a\u539f",
                    "value": [
                        112.53,
                        37.87,
                        50.0
                    ]
                }
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u57ce\u5e02\u85aa\u8d44\u5206\u5e03"
            ],
            "selected": {
                "\u57ce\u5e02\u85aa\u8d44\u5206\u5e03": true
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
            "text": "\u57ce\u5e02\u85aa\u8d44\u5206\u5e03",
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
        chart_64c48c03bcbc4508873dd952df2e8cfc.setOption(option_64c48c03bcbc4508873dd952df2e8cfc);
    </script>
                <div id="ce8f0f460166412dbf12b398ba2d592a" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_ce8f0f460166412dbf12b398ba2d592a = echarts.init(
            document.getElementById('ce8f0f460166412dbf12b398ba2d592a'), 'white', {renderer: 'canvas'});
        var option_ce8f0f460166412dbf12b398ba2d592a = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                37.5,
                30.0,
                30.0,
                30.0,
                30.0,
                37.5,
                22.5,
                40.0,
                35.0,
                25.0,
                30.0
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    12.0,
                    29.375,
                    33.75,
                    42.5,
                    83.0
                ],
                [
                    13.5,
                    30.0,
                    37.5,
                    45.0,
                    80.0
                ],
                [
                    12.5,
                    30.0,
                    30.0,
                    37.5,
                    90.0
                ],
                [
                    12.5,
                    23.5,
                    31.25,
                    39.375,
                    75.0
                ],
                [
                    12.5,
                    27.5,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    45.0,
                    60.0
                ],
                [
                    19.5,
                    25.0,
                    30.0,
                    39.0,
                    45.0
                ],
                [
                    20.0,
                    30.0,
                    37.5,
                    43.75,
                    85.0
                ],
                [
                    12.5,
                    20.0,
                    22.5,
                    26.75,
                    50.0
                ],
                [
                    17.5,
                    31.25,
                    40.0,
                    50.625,
                    65.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u671d\u9633\u533a",
                "\u5357\u5c71\u533a",
                "\u79d1\u6280\u56ed",
                "\u671b\u4eac",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u897f\u5317\u65fa",
                "\u9ad8\u65b0\u533a",
                "\u95f5\u884c\u533a",
                "\u6768\u6d66\u533a",
                "\u798f\u7530\u533a",
                "\u5b9d\u5b89\u533a"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
                "\u671b\u4eac",
                "\u6d66\u4e1c\u65b0\u2026",
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_ce8f0f460166412dbf12b398ba2d592a.setOption(option_ce8f0f460166412dbf12b398ba2d592a);
    </script>
                <div id="9e316c6369734fb1a172c8334b8b8301" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_9e316c6369734fb1a172c8334b8b8301 = echarts.init(
            document.getElementById('9e316c6369734fb1a172c8334b8b8301'), 'white', {renderer: 'canvas'});
        var option_9e316c6369734fb1a172c8334b8b8301 = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                40.0,
                37.5,
                37.5,
                32.5,
                30.0,
                20.0,
                20.0
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    12.0,
                    22.5,
                    30.0,
                    40.0,
                    85.0
                ],
                [
                    12.5,
                    25.0,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    85.0
                ],
                [
                    15.0,
                    27.0,
                    32.5,
                    40.0,
                    85.0
                ],
                [
                    12.0,
                    22.5,
                    27.5,
                    32.5,
                    70.0
                ],
                [
                    12.0,
                    24.0,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    60.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u76f4\u64ad\u5e73\u53f0",
                "\u7535\u5546\u5e73\u53f0",
                "\u7535\u5546",
                "\u751f\u6d3b\u670d\u52a1",
                "IT\u6280\u672f\u670d\u52a1",
                "\u77ff\u4ea7",
                "\u73af\u4fdd"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
                "IT\u6280\u672f\u670d\u52a1",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u54a8\u8be2",
                "\u5de5\u5177\u7c7b\u4ea7\u54c1",
                "\u6570\u636e\u670d\u52a1",
                "\u667a\u80fd\u786c\u4ef6",
                "\u8f6f\u4ef6\u670d\u52a1"
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_9e316c6369734fb1a172c8334b8b8301.setOption(option_9e316c6369734fb1a172c8334b8b8301);
    </script>
                <div id="95596c80032941c0a99c21d374f05c62" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_95596c80032941c0a99c21d374f05c62 = echarts.init(
            document.getElementById('95596c80032941c0a99c21d374f05c62'), 'white', {renderer: 'canvas'});
        var option_95596c80032941c0a99c21d374f05c62 = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                33.75,
                30.0,
                30.0,
                30.0,
                30.0,
                30.0,
                30.0
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    12.5,
                    22.5,
                    30.0,
                    35.625,
                    55.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    35.0,
                    75.0
                ],
                [
                    12.0,
                    24.0,
                    30.0,
                    37.5,
                    90.0
                ],
                [
                    15.0,
                    22.5,
                    30.0,
                    35.625,
                    90.0
                ],
                [
                    13.5,
                    22.5,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    15.0,
                    26.5,
                    33.75,
                    40.0,
                    90.0
                ],
                [
                    12.5,
                    23.0,
                    30.0,
                    37.5,
                    90.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u673a\u5668\u5b66\u4e60",
                "\u6df1\u5ea6\u5b66\u4e60",
                "\u6570\u636e\u6316\u6398",
                "C/C++",
                "\u56fe\u7247\u8bc6\u522b",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "Python"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
                "C/C++",
                "Python",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u56fe\u7247\u8bc6\u522b",
                "\u6570\u636e\u6316\u6398",
                "\u673a\u5668\u5b66\u4e60",
                "\u6df1\u5ea6\u5b66\u4e60"
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_95596c80032941c0a99c21d374f05c62.setOption(option_95596c80032941c0a99c21d374f05c62);
    </script>
                <div id="a675ea15cf0b41ffa59a4ba7d7e6062d" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_a675ea15cf0b41ffa59a4ba7d7e6062d = echarts.init(
            document.getElementById('a675ea15cf0b41ffa59a4ba7d7e6062d'), 'white', {renderer: 'canvas'});
        var option_a675ea15cf0b41ffa59a4ba7d7e6062d = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                45.0,
                35.0,
                35.0,
                30.0,
                30.0,
                22.5,
                22.5,
                19.0
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    16.0,
                    30.0,
                    35.0,
                    40.0,
                    60.0
                ],
                [
                    24.0,
                    40.0,
                    45.0,
                    50.0,
                    80.0
                ],
                [
                    12.0,
                    20.0,
                    22.5,
                    26.5,
                    40.0
                ],
                [
                    12.0,
                    15.0,
                    22.5,
                    25.0,
                    90.0
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    40.0,
                    90.0
                ],
                [
                    12.5,
                    26.5,
                    30.0,
                    40.0,
                    75.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u535a\u58eb",
                "\u4e0d\u9650",
                "\u5e94\u5c4a / \u535a\u58eb",
                "\u672c\u79d1",
                "\u7855\u58eb",
                "\u5e94\u5c4a / \u672c\u79d1",
                "\u5e94\u5c4a / \u7855\u58eb",
                "\u5e94\u5c4a / \u4e0d\u9650"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
                "\u4e0d\u9650",
                "\u535a\u58eb",
                "\u5e94\u5c4a / \u672c\u79d1",
                "\u5e94\u5c4a / \u7855\u58eb",
                "\u672c\u79d1",
                "\u7855\u58eb"
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_a675ea15cf0b41ffa59a4ba7d7e6062d.setOption(option_a675ea15cf0b41ffa59a4ba7d7e6062d);
    </script>
                <div id="e40ca01e02994696a3b671d3df01e7e4" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_e40ca01e02994696a3b671d3df01e7e4 = echarts.init(
            document.getElementById('e40ca01e02994696a3b671d3df01e7e4'), 'white', {renderer: 'canvas'});
        var option_e40ca01e02994696a3b671d3df01e7e4 = {
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
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 0,
            "yAxisIndex": 0,
            "legendHoverLink": true,
            "data": [
                57.5,
                43.75,
                31.0,
                30.0,
                27.5,
                22.5,
                22.5
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
            "type": "boxplot",
            "name": "\u85aa\u8d44(k)",
            "xAxisIndex": 1,
            "yAxisIndex": 1,
            "data": [
                [
                    12.0,
                    22.5,
                    27.5,
                    32.5,
                    80.0
                ],
                [
                    30.0,
                    37.5,
                    57.5,
                    65.0,
                    65.0
                ],
                [
                    13.5,
                    16.25,
                    22.5,
                    25.0,
                    40.0
                ],
                [
                    15.0,
                    27.5,
                    31.0,
                    37.5,
                    80.0
                ],
                [
                    12.5,
                    36.875,
                    43.75,
                    52.5,
                    90.0
                ],
                [
                    12.5,
                    24.0,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    12.0,
                    16.0,
                    22.5,
                    26.5,
                    90.0
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                }
            },
            "markLine": {
                "silent": false,
                "precision": 2,
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                }
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        },
        {
            "data": [
                "\u85aa\u8d44(k)"
            ],
            "selected": {
                "\u85aa\u8d44(k)": true
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
                "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c3-5\u5e74",
                "\u7ecf\u9a8c\u4e0d\u9650",
                "\u7ecf\u9a8c1-3\u5e74",
                "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                "\u7ecf\u9a8c\u5728\u6821"
            ]
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
                "\u7ecf\u9a8c1-3\u5e74",
                "\u7ecf\u9a8c10\u5e74\u4ee5\u4e0a",
                "\u7ecf\u9a8c1\u5e74\u4ee5\u4e0b",
                "\u7ecf\u9a8c3-5\u5e74",
                "\u7ecf\u9a8c5-10\u5e74",
                "\u7ecf\u9a8c\u4e0d\u9650",
                "\u7ecf\u9a8c\u5728\u6821"
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
        },
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 1,
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
            "padding": 5,
            "itemGap": 10
        }
    ],
    "grid": [
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "bottom": "60%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        },
        {
            "show": false,
            "zlevel": 0,
            "z": 2,
            "top": "45%",
            "containLabel": false,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderWidth": 1
        }
    ]
};
        chart_e40ca01e02994696a3b671d3df01e7e4.setOption(option_e40ca01e02994696a3b671d3df01e7e4);
    </script>
                        <style>
            .fl-table {
                margin: 20px;
                border-radius: 5px;
                font-size: 12px;
                border: none;
                border-collapse: collapse;
                max-width: 100%;
                white-space: nowrap;
                word-break: keep-all;
            }

            .fl-table th {
                text-align: left;
                font-size: 20px;
            }

            .fl-table tr {
                display: table-row;
                vertical-align: inherit;
                border-color: inherit;
            }

            .fl-table tr:hover td {
                background: #00d1b2;
                color: #F8F8F8;
            }

            .fl-table td, .fl-table th {
                border-style: none;
                border-top: 1px solid #dbdbdb;
                border-left: 1px solid #dbdbdb;
                border-bottom: 3px solid #dbdbdb;
                border-right: 1px solid #dbdbdb;
                padding: .5em .55em;
                font-size: 15px;
            }

            .fl-table td {
                border-style: none;
                font-size: 15px;
                vertical-align: center;
                border-bottom: 1px solid #dbdbdb;
                border-left: 1px solid #dbdbdb;
                border-right: 1px solid #dbdbdb;
                height: 30px;
            }

            .fl-table tr:nth-child(even) {
                background: #F8F8F8;
            }
        </style>
        <div id="485766e1c53642bc907ce95881509e2a" class="chart-container" style="">
            <p class="title" style="font-size: 18px; font-weight:bold;" > top10高薪岗位</p>
            <p class="subtitle" style="font-size: 12px;" > </p>
            <table class="fl-table">
    <tr>
        <th>标题</th>
        <th>公司地址</th>
        <th>公司名</th>
        <th>学历要求</th>
        <th>经验年限</th>
        <th>公司行业</th>
        <th>公司规模</th>
        <th>人员规模</th>
        <th>薪资</th>
    </tr>
    <tr>
        <td>算法工程师</td>
        <td>北京·通州区</td>
        <td>京东集团</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>电商平台</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>60k-120k</td>
    </tr>
    <tr>
        <td>算法负责人</td>
        <td>深圳·南山区</td>
        <td>德聚智能</td>
        <td>应届 / 硕士</td>
        <td>经验在校</td>
        <td>移动互联网,企业服务</td>
        <td>不需要融资</td>
        <td>150-500人</td>
        <td>60k-120k</td>
    </tr>
    <tr>
        <td>资深推荐算法专家（广告方向）</td>
        <td>北京·西北旺</td>
        <td>网易</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>内容资讯,游戏,音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>70k-100k</td>
    </tr>
    <tr>
        <td>算法工程师</td>
        <td>上海·杨浦区</td>
        <td>北京如秄</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>工具类产品,IT技术服务｜咨询,专业服务｜咨询</td>
        <td>不需要融资</td>
        <td>50-150人</td>
        <td>70k-100k</td>
    </tr>
    <tr>
        <td>图像算法负责人（LB）</td>
        <td>北京·海淀区</td>
        <td>北京如秄</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>工具类产品,IT技术服务｜咨询,专业服务｜咨询</td>
        <td>不需要融资</td>
        <td>50-150人</td>
        <td>66k-100k</td>
    </tr>
    <tr>
        <td>算法专家（3D视觉方向）</td>
        <td>深圳·科技园</td>
        <td>信润富联</td>
        <td>博士</td>
        <td>经验1-3年</td>
        <td>软件开发</td>
        <td>不需要融资</td>
        <td>50-150人</td>
        <td>60k-100k</td>
    </tr>
    <tr>
        <td>搜索高级算法工程师</td>
        <td>北京·朝阳区</td>
        <td>寺库</td>
        <td>本科</td>
        <td>经验3-5年</td>
        <td>电商,消费生活</td>
        <td>D轮及以上</td>
        <td>500-2000人</td>
        <td>60k-100k</td>
    </tr>
    <tr>
        <td>本地生活-推荐算法专家-大盘提效</td>
        <td>上海·长征</td>
        <td>饿了么</td>
        <td>硕士</td>
        <td>经验5-10年</td>
        <td>消费生活</td>
        <td>D轮及以上</td>
        <td>2000人以上</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>算法开发工程师(物流方向)</td>
        <td>北京</td>
        <td>北京如秄</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>工具类产品,IT技术服务｜咨询,专业服务｜咨询</td>
        <td>不需要融资</td>
        <td>50-150人</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>调度算法工程师</td>
        <td>北京·大兴区</td>
        <td>京东物流</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>物流｜运输</td>
        <td>A轮</td>
        <td>2000人以上</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>资深算法和大数据工程师/专家【岗位编号003】</td>
        <td>北京·宣武门</td>
        <td>UMU</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>社交平台</td>
        <td>C轮</td>
        <td>50-150人</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>技术总监（数据算法类）</td>
        <td>北京·朝阳区</td>
        <td>火眼云</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>营销服务｜咨询</td>
        <td>A轮</td>
        <td>50-150人</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>高级/资深图像算法工程师</td>
        <td>北京·西北旺</td>
        <td>网易</td>
        <td>本科</td>
        <td>经验3-5年</td>
        <td>内容资讯,游戏,音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>算法专家(011341)</td>
        <td>深圳·福田区</td>
        <td>vivo</td>
        <td>硕士</td>
        <td>经验5-10年</td>
        <td>智能硬件</td>
        <td>不需要融资</td>
        <td>2000人以上</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>机器学习算法工程师</td>
        <td>深圳·新安</td>
        <td>惠蓉</td>
        <td>本科</td>
        <td>经验3-5年</td>
        <td>金融,移动互联网</td>
        <td>未融资</td>
        <td>15-50人</td>
        <td>50k-100k</td>
    </tr>
</table>
        </div>

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
