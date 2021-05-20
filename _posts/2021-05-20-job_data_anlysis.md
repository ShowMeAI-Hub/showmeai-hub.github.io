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

<h2>（2021-05-20更新）</h2>

<h2>点击按钮查看招聘数据分析详情</h2>
    
<a href="https://showmeai-hub.github.io/2021/05/20/job_data_anlysis.html">
    <button class="button">看薪资</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/20/job_anlysis_company.html">
    <button class="button">看公司</button>
</a>
<a href="https://showmeai-hub.github.io/2021/05/20/job_anlysis_skills.html">
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
            <button class="tablinks" onclick="showChart(event, '5150ba7690424b7298514e10ffe5cefd')">薪资</button>
            <button class="tablinks" onclick="showChart(event, '116039e489fc422eb0b1cbfed316d1dc')">实习薪资分布</button>
            <button class="tablinks" onclick="showChart(event, 'c8a62e3c94e549f882d8f299d6288340')">社招薪资分布</button>
            <button class="tablinks" onclick="showChart(event, '564acd4bf079476d99b509b906ab593a')">城市&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'b83271287b6e46c7ac5e1efe731ebeee')">薪资地图</button>
            <button class="tablinks" onclick="showChart(event, '9dcea8482ddc47f29dd636cd5953bea2')">区域&薪资</button>
            <button class="tablinks" onclick="showChart(event, '2b05002d1f2e403e90d1d380b1370d07')">行业&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'ec887b1618bf4bf086452138365ca361')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'd8b45be3f1a64394bca41f8b5478d76b')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, '912407806e4f4377bd3b98fbe5d9c5f9')">经验&薪资</button>
            <button class="tablinks" onclick="showChart(event, '1844d30c764245378c3aeebb8a968a71')">top10薪资招聘</button>
    </div>

    <div class="box">
                <div id="5150ba7690424b7298514e10ffe5cefd" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_5150ba7690424b7298514e10ffe5cefd = echarts.init(
            document.getElementById('5150ba7690424b7298514e10ffe5cefd'), 'white', {renderer: 'canvas'});
            
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
    
        var option_5150ba7690424b7298514e10ffe5cefd = {
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
                260,
                169,
                168,
                140,
                106,
                94,
                88,
                72,
                66,
                54
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
                    "value": 260
                },
                {
                    "name": "15k-30k",
                    "value": 169
                },
                {
                    "name": "25k-50k",
                    "value": 168
                },
                {
                    "name": "30k-60k",
                    "value": 140
                },
                {
                    "name": "30k-50k",
                    "value": 106
                },
                {
                    "name": "20k-30k",
                    "value": 94
                },
                {
                    "name": "15k-25k",
                    "value": 88
                },
                {
                    "name": "25k-40k",
                    "value": 72
                },
                {
                    "name": "20k-35k",
                    "value": 66
                },
                {
                    "name": "25k-45k",
                    "value": 54
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
                    "value": 260
                },
                {
                    "name": "15k-30k",
                    "value": 169
                },
                {
                    "name": "25k-50k",
                    "value": 168
                },
                {
                    "name": "30k-60k",
                    "value": 140
                },
                {
                    "name": "30k-50k",
                    "value": 106
                },
                {
                    "name": "20k-30k",
                    "value": 94
                },
                {
                    "name": "15k-25k",
                    "value": 88
                },
                {
                    "name": "25k-40k",
                    "value": 72
                },
                {
                    "name": "20k-35k",
                    "value": 66
                },
                {
                    "name": "25k-45k",
                    "value": 54
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
                "15k-30k",
                "25k-50k",
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
                "15k-30k",
                "25k-50k",
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
        chart_5150ba7690424b7298514e10ffe5cefd.setOption(option_5150ba7690424b7298514e10ffe5cefd);
    </script>
                <div id="116039e489fc422eb0b1cbfed316d1dc" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_116039e489fc422eb0b1cbfed316d1dc = echarts.init(
            document.getElementById('116039e489fc422eb0b1cbfed316d1dc'), 'white', {renderer: 'canvas'});
            
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
    
        var option_116039e489fc422eb0b1cbfed316d1dc = {
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
                    4,
                    7,
                    12,
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
                    5.5,
                    10,
                    17.5,
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
                    4.5,
                    5.75,
                    7.75,
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
        chart_116039e489fc422eb0b1cbfed316d1dc.setOption(option_116039e489fc422eb0b1cbfed316d1dc);
    </script>
                <div id="c8a62e3c94e549f882d8f299d6288340" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_c8a62e3c94e549f882d8f299d6288340 = echarts.init(
            document.getElementById('c8a62e3c94e549f882d8f299d6288340'), 'white', {renderer: 'canvas'});
            
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
    
        var option_c8a62e3c94e549f882d8f299d6288340 = {
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
                    15.5,
                    24,
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
                    25.25,
                    37.5,
                    53.75,
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
        chart_c8a62e3c94e549f882d8f299d6288340.setOption(option_c8a62e3c94e549f882d8f299d6288340);
    </script>
                <div id="564acd4bf079476d99b509b906ab593a" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_564acd4bf079476d99b509b906ab593a = echarts.init(
            document.getElementById('564acd4bf079476d99b509b906ab593a'), 'white', {renderer: 'canvas'});
        var option_564acd4bf079476d99b509b906ab593a = {
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
                30.0,
                30.0,
                35.0,
                22.75,
                27.25,
                22.5,
                30.0,
                20.0,
                30.0,
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
                    25.0,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    17.5,
                    26.125,
                    30.0,
                    37.5,
                    42.5
                ],
                [
                    12.5,
                    30.0,
                    35.0,
                    40.0,
                    90.0
                ],
                [
                    15.0,
                    17.125,
                    22.75,
                    35.625,
                    50.0
                ],
                [
                    12.0,
                    20.375,
                    27.25,
                    32.5,
                    75.0
                ],
                [
                    12.5,
                    17.0,
                    22.5,
                    28.75,
                    40.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    38.75,
                    70.0
                ],
                [
                    12.5,
                    16.0,
                    20.0,
                    24.0,
                    37.5
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    15.0,
                    20.0,
                    22.5,
                    31.875,
                    45.0
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
                "\u4f5b\u5c71",
                "\u5317\u4eac",
                "\u5357\u4eac",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u676d\u5dde",
                "\u6b66\u6c49",
                "\u6df1\u5733",
                "\u82cf\u5dde"
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
                "\u4f5b\u5c71",
                "\u5317\u4eac",
                "\u5357\u4eac",
                "\u5e7f\u5dde",
                "\u6210\u90fd",
                "\u676d\u5dde",
                "\u6b66\u6c49",
                "\u6df1\u5733",
                "\u82cf\u5dde"
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
        chart_564acd4bf079476d99b509b906ab593a.setOption(option_564acd4bf079476d99b509b906ab593a);
    </script>
                <div id="b83271287b6e46c7ac5e1efe731ebeee" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_b83271287b6e46c7ac5e1efe731ebeee = echarts.init(
            document.getElementById('b83271287b6e46c7ac5e1efe731ebeee'), 'white', {renderer: 'canvas'});
            
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
    
        var option_b83271287b6e46c7ac5e1efe731ebeee = {
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
                        22.75
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
                        20.5
                    ]
                },
                {
                    "name": "\u5609\u5174",
                    "value": [
                        120.76,
                        30.77,
                        14.0
                    ]
                },
                {
                    "name": "\u5927\u8fde",
                    "value": [
                        121.62,
                        38.92,
                        24.5
                    ]
                },
                {
                    "name": "\u5929\u6d25",
                    "value": [
                        117.200983,
                        39.084158,
                        22.5
                    ]
                },
                {
                    "name": "\u5e7f\u5dde",
                    "value": [
                        113.23,
                        23.16,
                        27.25
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
                        20.0
                    ]
                },
                {
                    "name": "\u6d4e\u5357",
                    "value": [
                        117,
                        36.65,
                        15.75
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
                        22.5
                    ]
                },
                {
                    "name": "\u897f\u5b89",
                    "value": [
                        108.95,
                        34.27,
                        21.25
                    ]
                },
                {
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        16.25
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
                        17.5
                    ]
                },
                {
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        17.5
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
        chart_b83271287b6e46c7ac5e1efe731ebeee.setOption(option_b83271287b6e46c7ac5e1efe731ebeee);
    </script>
                <div id="9dcea8482ddc47f29dd636cd5953bea2" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_9dcea8482ddc47f29dd636cd5953bea2 = echarts.init(
            document.getElementById('9dcea8482ddc47f29dd636cd5953bea2'), 'white', {renderer: 'canvas'});
        var option_9dcea8482ddc47f29dd636cd5953bea2 = {
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
                37.5,
                36.25,
                33.0,
                32.5,
                30.0,
                30.0,
                30.0,
                30.0,
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
                    15.0,
                    30.0,
                    37.5,
                    45.0,
                    70.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    39.375,
                    67.5
                ],
                [
                    12.5,
                    24.375,
                    30.0,
                    37.5,
                    65.0
                ],
                [
                    15.0,
                    25.625,
                    33.0,
                    45.0,
                    75.0
                ],
                [
                    21.5,
                    30.0,
                    37.5,
                    45.0,
                    75.0
                ],
                [
                    15.0,
                    30.0,
                    36.25,
                    45.0,
                    80.0
                ],
                [
                    16.0,
                    25.0,
                    30.0,
                    40.0,
                    55.0
                ],
                [
                    12.5,
                    27.5,
                    32.5,
                    40.0,
                    60.0
                ],
                [
                    12.0,
                    22.75,
                    30.0,
                    37.5,
                    55.0
                ],
                [
                    12.5,
                    20.0,
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
                "\u671b\u4eac",
                "\u4e2d\u5173\u6751",
                "\u671d\u9633\u533a",
                "\u5f90\u6c47\u533a",
                "\u6d77\u6dc0\u533a",
                "\u79d1\u6280\u56ed",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u5357\u5c71\u533a",
                "\u4f59\u676d\u533a",
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
                "\u5f90\u6c47\u533a",
                "\u671b\u4eac",
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
        chart_9dcea8482ddc47f29dd636cd5953bea2.setOption(option_9dcea8482ddc47f29dd636cd5953bea2);
    </script>
                <div id="2b05002d1f2e403e90d1d380b1370d07" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_2b05002d1f2e403e90d1d380b1370d07 = echarts.init(
            document.getElementById('2b05002d1f2e403e90d1d380b1370d07'), 'white', {renderer: 'canvas'});
        var option_2b05002d1f2e403e90d1d380b1370d07 = {
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
                37.5,
                37.5,
                35.0,
                28.25,
                26.0,
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
                    20.0,
                    26.0,
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    35.0,
                    70.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.0,
                    20.0,
                    27.5,
                    35.0,
                    60.0
                ],
                [
                    13.5,
                    22.5,
                    30.0,
                    37.5,
                    75.0
                ],
                [
                    16.5,
                    24.0,
                    30.0,
                    37.5,
                    65.0
                ],
                [
                    12.0,
                    21.5,
                    27.5,
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
                "\u7269\u6d41\u5e73\u53f0",
                "\u7535\u5546\u5e73\u53f0",
                "\u77ed\u89c6\u9891",
                "\u76f4\u64ad\u5e73\u53f0",
                "\u7535\u5546",
                "IT\u6280\u672f\u670d\u52a1",
                "\u77ff\u4ea7"
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
        chart_2b05002d1f2e403e90d1d380b1370d07.setOption(option_2b05002d1f2e403e90d1d380b1370d07);
    </script>
                <div id="ec887b1618bf4bf086452138365ca361" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_ec887b1618bf4bf086452138365ca361 = echarts.init(
            document.getElementById('ec887b1618bf4bf086452138365ca361'), 'white', {renderer: 'canvas'});
        var option_ec887b1618bf4bf086452138365ca361 = {
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
                32.5,
                30.0,
                30.0,
                30.0,
                30.0,
                26.5
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
                    20.5,
                    26.5,
                    34.5,
                    75.0
                ],
                [
                    12.5,
                    27.5,
                    32.5,
                    42.5,
                    80.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    70.0
                ],
                [
                    12.0,
                    25.0,
                    33.75,
                    40.0,
                    90.0
                ],
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
                "\u673a\u5668\u5b66\u4e60",
                "\u63a8\u8350\u7b97\u6cd5",
                "\u6df1\u5ea6\u5b66\u4e60",
                "\u6570\u636e\u6316\u6398",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
                "Python",
                "\u56fe\u7247\u8bc6\u522b"
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
        chart_ec887b1618bf4bf086452138365ca361.setOption(option_ec887b1618bf4bf086452138365ca361);
    </script>
                <div id="d8b45be3f1a64394bca41f8b5478d76b" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_d8b45be3f1a64394bca41f8b5478d76b = echarts.init(
            document.getElementById('d8b45be3f1a64394bca41f8b5478d76b'), 'white', {renderer: 'canvas'});
        var option_d8b45be3f1a64394bca41f8b5478d76b = {
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
                35.0,
                35.0,
                30.0,
                30.0,
                20.75,
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
                    20.0,
                    30.0,
                    35.0,
                    45.0,
                    60.0
                ],
                [
                    24.0,
                    37.5,
                    40.0,
                    50.0,
                    65.0
                ],
                [
                    14.5,
                    15.0,
                    17.0,
                    20.875,
                    25.0
                ],
                [
                    12.0,
                    15.0,
                    20.0,
                    25.0,
                    40.0
                ],
                [
                    12.5,
                    15.0,
                    20.0,
                    22.5,
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
                "\u5e94\u5c4a / \u4e0d\u9650",
                "\u5e94\u5c4a / \u672c\u79d1",
                "\u5e94\u5c4a / \u7855\u58eb"
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
                "\u5927\u4e13",
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
        chart_d8b45be3f1a64394bca41f8b5478d76b.setOption(option_d8b45be3f1a64394bca41f8b5478d76b);
    </script>
                <div id="912407806e4f4377bd3b98fbe5d9c5f9" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_912407806e4f4377bd3b98fbe5d9c5f9 = echarts.init(
            document.getElementById('912407806e4f4377bd3b98fbe5d9c5f9'), 'white', {renderer: 'canvas'});
        var option_912407806e4f4377bd3b98fbe5d9c5f9 = {
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
                55.0,
                40.0,
                30.0,
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
                    20.0,
                    25.0,
                    30.0,
                    60.0
                ],
                [
                    15.0,
                    18.75,
                    22.5,
                    24.375,
                    25.0
                ],
                [
                    12.5,
                    25.0,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.5,
                    35.0,
                    40.0,
                    50.0,
                    90.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.0,
                    15.0,
                    20.0,
                    24.25,
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
        chart_912407806e4f4377bd3b98fbe5d9c5f9.setOption(option_912407806e4f4377bd3b98fbe5d9c5f9);
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
        <div id="1844d30c764245378c3aeebb8a968a71" class="chart-container" style="">
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
        <td>高级算法专家/资深算法专家-信息</td>
        <td>北京·朝阳区</td>
        <td>阿里巴巴-高德</td>
        <td>本科</td>
        <td>经验不限</td>
        <td>工具类产品</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>60k-100k</td>
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
        <td>算法负责人（总监）</td>
        <td>上海·静安区</td>
        <td>逸兴遄飞</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>专业服务｜咨询</td>
        <td>未融资</td>
        <td>50-150人</td>
        <td>70k-90k</td>
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
        <td>算法专家</td>
        <td>北京·望京</td>
        <td>曙兴科技</td>
        <td>本科</td>
        <td>经验3-5年</td>
        <td>移动互联网,电商</td>
        <td>不需要融资</td>
        <td>500-2000人</td>
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
        <td>算法leader</td>
        <td>深圳·新安</td>
        <td>江行智能</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>智能硬件</td>
        <td>A轮</td>
        <td>50-150人</td>
        <td>60k-90k</td>
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
        <td>资深推荐算法专家 - 音乐事业部003</td>
        <td>杭州·长河</td>
        <td>网易</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>内容资讯,游戏,音频｜视频媒体</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>55k-85k</td>
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
