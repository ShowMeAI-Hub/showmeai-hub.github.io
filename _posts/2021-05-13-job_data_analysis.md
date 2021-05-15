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
            <button class="tablinks" onclick="showChart(event, '04af7dbded8e4fb4bf5bf7114ae92b2c')">薪资</button>
            <button class="tablinks" onclick="showChart(event, '6665ff6d28204163aa1e2e723d84892b')">实习薪资分布</button>
            <button class="tablinks" onclick="showChart(event, 'f7584a1e50ac4c6f836196b4d35e3a6f')">社招薪资分布</button>
            <button class="tablinks" onclick="showChart(event, '2673e5234e7f49d3abca4b660b2b450f')">城市&薪资</button>
            <button class="tablinks" onclick="showChart(event, '3f29371aae2a45f69b2178cbbb0cd5f5')">薪资地图</button>
            <button class="tablinks" onclick="showChart(event, '555eba165561415db66ddabc287d873c')">区域&薪资</button>
            <button class="tablinks" onclick="showChart(event, '9e52aa4ae2c344eaa93402170d1559e0')">行业&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'f94cd51e3f9749f793137ab90c19ac3b')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'c3430735b542497499adefc87c5f3c91')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, '132943f4932d4f4e9113bf5fe42e4280')">经验&薪资</button>
            <button class="tablinks" onclick="showChart(event, '0d121a38cd394fbe824d10955950aa9c')">top10薪资招聘</button>
    </div>

    <div class="box">
                <div id="04af7dbded8e4fb4bf5bf7114ae92b2c" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_04af7dbded8e4fb4bf5bf7114ae92b2c = echarts.init(
            document.getElementById('04af7dbded8e4fb4bf5bf7114ae92b2c'), 'white', {renderer: 'canvas'});
        var option_04af7dbded8e4fb4bf5bf7114ae92b2c = {
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
                179,
                117,
                116,
                87,
                75,
                63,
                58,
                53,
                46,
                43
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
                    "value": 179
                },
                {
                    "name": "25k-50k",
                    "value": 117
                },
                {
                    "name": "15k-30k",
                    "value": 116
                },
                {
                    "name": "30k-60k",
                    "value": 87
                },
                {
                    "name": "30k-50k",
                    "value": 75
                },
                {
                    "name": "20k-30k",
                    "value": 63
                },
                {
                    "name": "15k-25k",
                    "value": 58
                },
                {
                    "name": "25k-40k",
                    "value": 53
                },
                {
                    "name": "20k-35k",
                    "value": 46
                },
                {
                    "name": "25k-45k",
                    "value": 43
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
                    "value": 179
                },
                {
                    "name": "25k-50k",
                    "value": 117
                },
                {
                    "name": "15k-30k",
                    "value": 116
                },
                {
                    "name": "30k-60k",
                    "value": 87
                },
                {
                    "name": "30k-50k",
                    "value": 75
                },
                {
                    "name": "20k-30k",
                    "value": 63
                },
                {
                    "name": "15k-25k",
                    "value": 58
                },
                {
                    "name": "25k-40k",
                    "value": 53
                },
                {
                    "name": "20k-35k",
                    "value": 46
                },
                {
                    "name": "25k-45k",
                    "value": 43
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
                "20k-30k",
                "15k-25k",
                "25k-40k",
                "20k-35k",
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
                "20k-30k",
                "15k-25k",
                "25k-40k",
                "20k-35k",
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
        chart_04af7dbded8e4fb4bf5bf7114ae92b2c.setOption(option_04af7dbded8e4fb4bf5bf7114ae92b2c);
    </script>
                <div id="6665ff6d28204163aa1e2e723d84892b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_6665ff6d28204163aa1e2e723d84892b = echarts.init(
            document.getElementById('6665ff6d28204163aa1e2e723d84892b'), 'white', {renderer: 'canvas'});
        var option_6665ff6d28204163aa1e2e723d84892b = {
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
                    3,
                    4.25,
                    6.5,
                    9.5,
                    20
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
                    4,
                    6,
                    10,
                    15,
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
            "name": "\u5e73\u5747\u85aa\u8d44",
            "data": [
                [
                    3.5,
                    5.0,
                    6.0,
                    8.0,
                    25.0
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
        chart_6665ff6d28204163aa1e2e723d84892b.setOption(option_6665ff6d28204163aa1e2e723d84892b);
    </script>
                <div id="f7584a1e50ac4c6f836196b4d35e3a6f" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_f7584a1e50ac4c6f836196b4d35e3a6f = echarts.init(
            document.getElementById('f7584a1e50ac4c6f836196b4d35e3a6f'), 'white', {renderer: 'canvas'});
        var option_f7584a1e50ac4c6f836196b4d35e3a6f = {
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
                    14.75,
                    22.5,
                    35.5,
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
                    14,
                    25,
                    37,
                    50,
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
                    22.5,
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
        chart_f7584a1e50ac4c6f836196b4d35e3a6f.setOption(option_f7584a1e50ac4c6f836196b4d35e3a6f);
    </script>
                <div id="2673e5234e7f49d3abca4b660b2b450f" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_2673e5234e7f49d3abca4b660b2b450f = echarts.init(
            document.getElementById('2673e5234e7f49d3abca4b660b2b450f'), 'white', {renderer: 'canvas'});
        var option_2673e5234e7f49d3abca4b660b2b450f = {
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
                30.0,
                35.0,
                22.5,
                27.5,
                22.5,
                30.0,
                22.5,
                30.0,
                23.75,
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
                    23.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    30.0,
                    35.0,
                    42.5,
                    90.0
                ],
                [
                    15.0,
                    17.75,
                    22.5,
                    33.75,
                    50.0
                ],
                [
                    12.5,
                    20.5,
                    27.5,
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    15.0,
                    22.5,
                    27.0,
                    40.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    15.0,
                    18.125,
                    22.5,
                    25.125,
                    37.5
                ],
                [
                    12.5,
                    24.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    15.0,
                    19.875,
                    23.75,
                    30.625,
                    45.0
                ],
                [
                    15.0,
                    19.5,
                    22.5,
                    27.5,
                    32.5
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
                "\u4e0a\u6d77",
                "\u5317\u4eac",
                "\u5357\u4eac",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u676d\u5dde",
                "\u6b66\u6c49",
                "\u6df1\u5733",
                "\u82cf\u5dde",
                "\u897f\u5b89"
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
                "\u4e0a\u6d77",
                "\u5317\u4eac",
                "\u5357\u4eac",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u676d\u5dde",
                "\u6b66\u6c49",
                "\u6df1\u5733",
                "\u82cf\u5dde",
                "\u897f\u5b89"
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
        chart_2673e5234e7f49d3abca4b660b2b450f.setOption(option_2673e5234e7f49d3abca4b660b2b450f);
    </script>
                <div id="3f29371aae2a45f69b2178cbbb0cd5f5" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_3f29371aae2a45f69b2178cbbb0cd5f5 = echarts.init(
            document.getElementById('3f29371aae2a45f69b2178cbbb0cd5f5'), 'white', {renderer: 'canvas'});
        var option_3f29371aae2a45f69b2178cbbb0cd5f5 = {
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
                    "name": "\u4e0a\u6d77",
                    "value": [
                        121.473701,
                        31.230416,
                        30.0
                    ]
                },
                {
                    "name": "\u4e1c\u839e",
                    "value": [
                        113.75,
                        23.04,
                        24.0
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
                    "name": "\u5317\u4eac",
                    "value": [
                        116.407526,
                        39.90403,
                        35.0
                    ]
                },
                {
                    "name": "\u5357\u4eac",
                    "value": [
                        118.78,
                        32.04,
                        22.5
                    ]
                },
                {
                    "name": "\u53a6\u95e8",
                    "value": [
                        118.1,
                        24.46,
                        34.0
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
                    "name": "\u5927\u8fde",
                    "value": [
                        121.62,
                        38.92,
                        16.5
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        27.5
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
                    "name": "\u6210\u90fd",
                    "value": [
                        104.06,
                        30.67,
                        22.5
                    ]
                },
                {
                    "name": "\u65e0\u9521",
                    "value": [
                        120.29,
                        31.59,
                        16.0
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
                    "name": "\u6b66\u6c49",
                    "value": [
                        114.31,
                        30.52,
                        22.5
                    ]
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": [
                        117,
                        36.65,
                        12.5
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
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        19.5
                    ]
                },
                {
                    "name": "\u798f\u5dde",
                    "value": [
                        119.3,
                        26.08,
                        14.75
                    ]
                },
                {
                    "name": "\u82cf\u5dde",
                    "value": [
                        120.62,
                        31.32,
                        23.75
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        22.5
                    ]
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        20.0
                    ]
                },
                {
                    "name": "\u91cd\u5e86",
                    "value": [
                        106.551556,
                        29.563009,
                        17.75
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
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        20.0
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
        chart_3f29371aae2a45f69b2178cbbb0cd5f5.setOption(option_3f29371aae2a45f69b2178cbbb0cd5f5);
    </script>
                <div id="555eba165561415db66ddabc287d873c" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_555eba165561415db66ddabc287d873c = echarts.init(
            document.getElementById('555eba165561415db66ddabc287d873c'), 'white', {renderer: 'canvas'});
        var option_555eba165561415db66ddabc287d873c = {
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
                35.0,
                32.5,
                32.5,
                30.0,
                30.0,
                30.0,
                30.0,
                28.75,
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
                    17.5,
                    31.25,
                    37.5,
                    45.0,
                    70.0
                ],
                [
                    12.5,
                    22.75,
                    30.0,
                    39.375,
                    67.5
                ],
                [
                    15.0,
                    27.5,
                    32.5,
                    37.5,
                    55.0
                ],
                [
                    15.0,
                    22.875,
                    30.0,
                    44.375,
                    75.0
                ],
                [
                    12.0,
                    21.375,
                    28.75,
                    33.75,
                    65.0
                ],
                [
                    17.5,
                    30.0,
                    35.0,
                    45.0,
                    80.0
                ],
                [
                    19.5,
                    25.0,
                    30.0,
                    40.0,
                    55.0
                ],
                [
                    12.5,
                    27.0,
                    32.5,
                    40.0,
                    60.0
                ],
                [
                    15.0,
                    25.0,
                    30.0,
                    37.5,
                    55.0
                ],
                [
                    12.5,
                    15.0,
                    22.5,
                    30.0,
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
                "\u4e2d\u5173\u6751",
                "\u671d\u9633\u533a",
                "\u6d77\u6dc0\u533a",
                "\u5357\u5c71\u533a",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u79d1\u6280\u56ed",
                "\u5b9d\u5b89\u533a",
                "\u4f59\u676d\u533a",
                "\u5f20\u6c5f",
                "\u9ad8\u65b0\u533a"
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
                "\u4e2d\u5173\u6751",
                "\u4f59\u676d\u533a",
                "\u5357\u5c71\u533a",
                "\u5b9d\u5b89\u533a",
                "\u5f20\u6c5f",
                "\u671d\u9633\u533a",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u6d77\u6dc0\u533a",
                "\u79d1\u6280\u56ed",
                "\u9ad8\u65b0\u533a"
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
        chart_555eba165561415db66ddabc287d873c.setOption(option_555eba165561415db66ddabc287d873c);
    </script>
                <div id="9e52aa4ae2c344eaa93402170d1559e0" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_9e52aa4ae2c344eaa93402170d1559e0 = echarts.init(
            document.getElementById('9e52aa4ae2c344eaa93402170d1559e0'), 'white', {renderer: 'canvas'});
        var option_9e52aa4ae2c344eaa93402170d1559e0 = {
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
                37.5,
                37.5,
                30.0,
                30.0,
                29.75,
                25.0
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
                    20.0,
                    25.0,
                    35.0,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    12.0,
                    22.5,
                    29.5,
                    37.5,
                    75.0
                ],
                [
                    12.0,
                    22.125,
                    29.5,
                    35.0,
                    60.0
                ],
                [
                    14.0,
                    22.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    19.5,
                    22.5,
                    30.0,
                    40.0,
                    65.0
                ],
                [
                    12.0,
                    21.75,
                    28.5,
                    37.5,
                    55.0
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
                "\u77ed\u89c6\u9891",
                "\u7535\u5546\u5e73\u53f0",
                "\u77ff\u4ea7",
                "\u76f4\u64ad\u5e73\u53f0",
                "\u7535\u5546",
                "\u65b0\u96f6\u552e",
                "IT\u6280\u672f\u670d\u52a1"
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
                "\u6570\u636e\u670d\u52a1",
                "\u667a\u80fd\u786c\u4ef6",
                "\u79d1\u6280\u91d1\u878d",
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
        chart_9e52aa4ae2c344eaa93402170d1559e0.setOption(option_9e52aa4ae2c344eaa93402170d1559e0);
    </script>
                <div id="f94cd51e3f9749f793137ab90c19ac3b" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_f94cd51e3f9749f793137ab90c19ac3b = echarts.init(
            document.getElementById('f94cd51e3f9749f793137ab90c19ac3b'), 'white', {renderer: 'canvas'});
        var option_f94cd51e3f9749f793137ab90c19ac3b = {
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
                32.5,
                32.5,
                30.0,
                30.0,
                30.0,
                27.5,
                27.5
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
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    27.5,
                    37.5,
                    75.0
                ],
                [
                    16.0,
                    27.5,
                    32.5,
                    40.0,
                    80.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    39.625,
                    70.0
                ],
                [
                    12.0,
                    25.75,
                    32.5,
                    40.0,
                    90.0
                ],
                [
                    12.0,
                    23.875,
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
                "\u63a8\u8350\u7b97\u6cd5",
                "\u673a\u5668\u5b66\u4e60",
                "\u6570\u636e\u6316\u6398",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u6df1\u5ea6\u5b66\u4e60",
                "\u56fe\u7247\u8bc6\u522b",
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
                "Python",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "\u56fe\u7247\u8bc6\u522b",
                "\u63a8\u8350\u7b97\u6cd5",
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
        chart_f94cd51e3f9749f793137ab90c19ac3b.setOption(option_f94cd51e3f9749f793137ab90c19ac3b);
    </script>
                <div id="c3430735b542497499adefc87c5f3c91" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_c3430735b542497499adefc87c5f3c91 = echarts.init(
            document.getElementById('c3430735b542497499adefc87c5f3c91'), 'white', {renderer: 'canvas'});
        var option_c3430735b542497499adefc87c5f3c91 = {
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
                35.0,
                35.0,
                30.0,
                30.0,
                22.5,
                20.0,
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
                    20.0,
                    30.0,
                    35.0,
                    45.0,
                    60.0
                ],
                [
                    24.0,
                    33.75,
                    40.0,
                    50.0,
                    55.0
                ],
                [
                    12.5,
                    15.0,
                    22.5,
                    25.0,
                    40.0
                ],
                [
                    12.5,
                    15.0,
                    20.0,
                    24.25,
                    34.5
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    90.0
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    37.5,
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
        chart_c3430735b542497499adefc87c5f3c91.setOption(option_c3430735b542497499adefc87c5f3c91);
    </script>
                <div id="132943f4932d4f4e9113bf5fe42e4280" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_132943f4932d4f4e9113bf5fe42e4280 = echarts.init(
            document.getElementById('132943f4932d4f4e9113bf5fe42e4280'), 'white', {renderer: 'canvas'});
        var option_132943f4932d4f4e9113bf5fe42e4280 = {
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
                55.0,
                40.0,
                32.5,
                30.0,
                25.0,
                22.5,
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
                    21.5,
                    25.0,
                    32.5,
                    60.0
                ],
                [
                    12.5,
                    25.0,
                    32.5,
                    37.5,
                    80.0
                ],
                [
                    12.5,
                    35.0,
                    40.0,
                    52.5,
                    90.0
                ],
                [
                    12.0,
                    24.0,
                    30.0,
                    37.5,
                    67.5
                ],
                [
                    12.5,
                    15.0,
                    20.0,
                    25.0,
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
        chart_132943f4932d4f4e9113bf5fe42e4280.setOption(option_132943f4932d4f4e9113bf5fe42e4280);
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
        <div id="0d121a38cd394fbe824d10955950aa9c" class="chart-container" style="">
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
        <td>算法leader</td>
        <td>北京·学院路</td>
        <td>最右</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>社交平台,内容社区</td>
        <td>D轮及以上</td>
        <td>500-2000人</td>
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
        <td>算法总监</td>
        <td>上海·徐汇区</td>
        <td>Versa</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>工具类产品</td>
        <td>B轮</td>
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
        <td>高级图像算法工程师</td>
        <td>广州·天河区</td>
        <td>艾雷特咨询管理</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>工具类产品,IT技术服务｜咨询,专业服务｜咨询</td>
        <td>未融资</td>
        <td>15-50人</td>
        <td>70k-80k</td>
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
        <td>算法工程师</td>
        <td>北京·通州区</td>
        <td>京东集团</td>
        <td>本科</td>
        <td>经验3-5年</td>
        <td>电商平台</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>50k-100k</td>
    </tr>
    <tr>
        <td>算法leader</td>
        <td>深圳·宝安区</td>
        <td>江行智能</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>智能硬件</td>
        <td>A轮</td>
        <td>50-150人</td>
        <td>60k-90k</td>
    </tr>
    <tr>
        <td>FF2824-高级算法专家/总监</td>
        <td>上海·杨浦区</td>
        <td>哔哩哔哩</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>60k-80k</td>
    </tr>
    <tr>
        <td>智能营销算法工程师/专家</td>
        <td>北京·大兴区</td>
        <td>京东物流</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>物流｜运输</td>
        <td>A轮</td>
        <td>2000人以上</td>
        <td>55k-85k</td>
    </tr>
    <tr>
        <td>高级算法工程师</td>
        <td>杭州·西湖区</td>
        <td>Mai小麦</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>人工智能服务</td>
        <td>A轮</td>
        <td>15-50人</td>
        <td>60k-80k</td>
    </tr>
    <tr>
        <td>广告算法研究员</td>
        <td>北京·中关村</td>
        <td>爱奇艺</td>
        <td>硕士</td>
        <td>经验5-10年</td>
        <td>音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>60k-80k</td>
    </tr>
    <tr>
        <td>音频算法工程师--4087</td>
        <td>北京·中关村</td>
        <td>爱奇艺</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>60k-80k</td>
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
