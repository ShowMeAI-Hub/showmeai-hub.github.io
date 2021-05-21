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
            <button class="tablinks" onclick="showChart(event, '398dfdab72e54d8692e8321dd41aaa1b')">薪资</button>
            <button class="tablinks" onclick="showChart(event, 'c7a6b32693f64b0cb2c1c300613c884a')">实习薪资分布</button>
            <button class="tablinks" onclick="showChart(event, 'ed20f4e1437248308a67d39caf0281ec')">社招薪资分布</button>
            <button class="tablinks" onclick="showChart(event, 'b8d68a5bb5d84055bc724e00ab76475b')">城市&薪资</button>
            <button class="tablinks" onclick="showChart(event, '19f52fa323af4cdd85b708992c1b3219')">薪资地图</button>
            <button class="tablinks" onclick="showChart(event, 'dad17c56569b4d4e9e8bfed73cf64d14')">区域&薪资</button>
            <button class="tablinks" onclick="showChart(event, '2497b033284d4c898d3519d086d17135')">行业&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'ebe863057c2949db936d82c85ff8d1ec')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'a7f301063bb2429d8ee66b2e68e0e9fb')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'ec6355c975614943b407c238e188d655')">经验&薪资</button>
            <button class="tablinks" onclick="showChart(event, '9e78b26bd1314dc38e11103f27c6bafb')">top10薪资招聘</button>
    </div>

    <div class="box">
                <div id="398dfdab72e54d8692e8321dd41aaa1b" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_398dfdab72e54d8692e8321dd41aaa1b = echarts.init(
            document.getElementById('398dfdab72e54d8692e8321dd41aaa1b'), 'white', {renderer: 'canvas'});
            
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
    
        var option_398dfdab72e54d8692e8321dd41aaa1b = {
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
                275,
                178,
                171,
                149,
                110,
                98,
                93,
                74,
                68,
                58
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
                    "value": 275
                },
                {
                    "name": "15k-30k",
                    "value": 178
                },
                {
                    "name": "25k-50k",
                    "value": 171
                },
                {
                    "name": "30k-60k",
                    "value": 149
                },
                {
                    "name": "30k-50k",
                    "value": 110
                },
                {
                    "name": "20k-30k",
                    "value": 98
                },
                {
                    "name": "15k-25k",
                    "value": 93
                },
                {
                    "name": "25k-40k",
                    "value": 74
                },
                {
                    "name": "20k-35k",
                    "value": 68
                },
                {
                    "name": "25k-45k",
                    "value": 58
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
                    "value": 275
                },
                {
                    "name": "15k-30k",
                    "value": 178
                },
                {
                    "name": "25k-50k",
                    "value": 171
                },
                {
                    "name": "30k-60k",
                    "value": 149
                },
                {
                    "name": "30k-50k",
                    "value": 110
                },
                {
                    "name": "20k-30k",
                    "value": 98
                },
                {
                    "name": "15k-25k",
                    "value": 93
                },
                {
                    "name": "25k-40k",
                    "value": 74
                },
                {
                    "name": "20k-35k",
                    "value": 68
                },
                {
                    "name": "25k-45k",
                    "value": 58
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
        chart_398dfdab72e54d8692e8321dd41aaa1b.setOption(option_398dfdab72e54d8692e8321dd41aaa1b);
    </script>
                <div id="c7a6b32693f64b0cb2c1c300613c884a" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_c7a6b32693f64b0cb2c1c300613c884a = echarts.init(
            document.getElementById('c7a6b32693f64b0cb2c1c300613c884a'), 'white', {renderer: 'canvas'});
            
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
    
        var option_c7a6b32693f64b0cb2c1c300613c884a = {
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
                    4.25,
                    7.5,
                    11.5,
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
                    5.75,
                    10.5,
                    18.5,
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
                    5.5,
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
        chart_c7a6b32693f64b0cb2c1c300613c884a.setOption(option_c7a6b32693f64b0cb2c1c300613c884a);
    </script>
                <div id="ed20f4e1437248308a67d39caf0281ec" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_ed20f4e1437248308a67d39caf0281ec = echarts.init(
            document.getElementById('ed20f4e1437248308a67d39caf0281ec'), 'white', {renderer: 'canvas'});
            
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
    
        var option_ed20f4e1437248308a67d39caf0281ec = {
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
        chart_ed20f4e1437248308a67d39caf0281ec.setOption(option_ed20f4e1437248308a67d39caf0281ec);
    </script>
                <div id="b8d68a5bb5d84055bc724e00ab76475b" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_b8d68a5bb5d84055bc724e00ab76475b = echarts.init(
            document.getElementById('b8d68a5bb5d84055bc724e00ab76475b'), 'white', {renderer: 'canvas'});
        var option_b8d68a5bb5d84055bc724e00ab76475b = {
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
                27.0,
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
                    37.75,
                    80.0
                ],
                [
                    17.5,
                    25.0,
                    30.0,
                    37.5,
                    42.5
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
                    17.125,
                    22.75,
                    35.625,
                    50.0
                ],
                [
                    12.0,
                    20.5,
                    27.0,
                    32.5,
                    75.0
                ],
                [
                    12.5,
                    19.0,
                    22.5,
                    27.5,
                    40.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    40.0,
                    70.0
                ],
                [
                    12.5,
                    16.0,
                    20.0,
                    24.25,
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
                    31.25,
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
        chart_b8d68a5bb5d84055bc724e00ab76475b.setOption(option_b8d68a5bb5d84055bc724e00ab76475b);
    </script>
                <div id="19f52fa323af4cdd85b708992c1b3219" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_19f52fa323af4cdd85b708992c1b3219 = echarts.init(
            document.getElementById('19f52fa323af4cdd85b708992c1b3219'), 'white', {renderer: 'canvas'});
            
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
    
        var option_19f52fa323af4cdd85b708992c1b3219 = {
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
                        27.0
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
                        18.0
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
        chart_19f52fa323af4cdd85b708992c1b3219.setOption(option_19f52fa323af4cdd85b708992c1b3219);
    </script>
                <div id="dad17c56569b4d4e9e8bfed73cf64d14" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_dad17c56569b4d4e9e8bfed73cf64d14 = echarts.init(
            document.getElementById('dad17c56569b4d4e9e8bfed73cf64d14'), 'white', {renderer: 'canvas'});
        var option_dad17c56569b4d4e9e8bfed73cf64d14 = {
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
                32.5,
                31.0,
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
                    40.0,
                    67.5
                ],
                [
                    12.5,
                    25.0,
                    30.0,
                    37.5,
                    65.0
                ],
                [
                    15.0,
                    25.0,
                    31.0,
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
                    13.5,
                    30.0,
                    36.25,
                    45.0,
                    80.0
                ],
                [
                    16.0,
                    25.0,
                    30.0,
                    39.375,
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
                "\u4e2d\u5173\u6751",
                "\u671b\u4eac",
                "\u671d\u9633\u533a",
                "\u6d77\u6dc0\u533a",
                "\u5f90\u6c47\u533a",
                "\u79d1\u6280\u56ed",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u4f59\u676d\u533a",
                "\u5357\u5c71\u533a",
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
        chart_dad17c56569b4d4e9e8bfed73cf64d14.setOption(option_dad17c56569b4d4e9e8bfed73cf64d14);
    </script>
                <div id="2497b033284d4c898d3519d086d17135" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_2497b033284d4c898d3519d086d17135 = echarts.init(
            document.getElementById('2497b033284d4c898d3519d086d17135'), 'white', {renderer: 'canvas'});
        var option_2497b033284d4c898d3519d086d17135 = {
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
                27.0,
                26.5,
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
                    27.0,
                    37.5,
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
                    21.0,
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
                "\u7535\u5546\u5e73\u53f0",
                "\u7269\u6d41\u5e73\u53f0",
                "\u77ed\u89c6\u9891",
                "\u76f4\u64ad\u5e73\u53f0",
                "IT\u6280\u672f\u670d\u52a1",
                "\u7535\u5546",
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
        chart_2497b033284d4c898d3519d086d17135.setOption(option_2497b033284d4c898d3519d086d17135);
    </script>
                <div id="ebe863057c2949db936d82c85ff8d1ec" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_ebe863057c2949db936d82c85ff8d1ec = echarts.init(
            document.getElementById('ebe863057c2949db936d82c85ff8d1ec'), 'white', {renderer: 'canvas'});
        var option_ebe863057c2949db936d82c85ff8d1ec = {
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
                34.0,
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
                    20.25,
                    26.5,
                    35.0,
                    75.0
                ],
                [
                    12.5,
                    27.5,
                    34.0,
                    45.0,
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
                    35.0,
                    41.25,
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
        chart_ebe863057c2949db936d82c85ff8d1ec.setOption(option_ebe863057c2949db936d82c85ff8d1ec);
    </script>
                <div id="a7f301063bb2429d8ee66b2e68e0e9fb" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_a7f301063bb2429d8ee66b2e68e0e9fb = echarts.init(
            document.getElementById('a7f301063bb2429d8ee66b2e68e0e9fb'), 'white', {renderer: 'canvas'});
        var option_a7f301063bb2429d8ee66b2e68e0e9fb = {
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
        chart_a7f301063bb2429d8ee66b2e68e0e9fb.setOption(option_a7f301063bb2429d8ee66b2e68e0e9fb);
    </script>
                <div id="ec6355c975614943b407c238e188d655" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_ec6355c975614943b407c238e188d655 = echarts.init(
            document.getElementById('ec6355c975614943b407c238e188d655'), 'white', {renderer: 'canvas'});
        var option_ec6355c975614943b407c238e188d655 = {
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
                    21.0,
                    25.0,
                    30.0,
                    60.0
                ],
                [
                    13.5,
                    16.25,
                    22.5,
                    23.75,
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
                    32.875,
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
                    24.5,
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
        chart_ec6355c975614943b407c238e188d655.setOption(option_ec6355c975614943b407c238e188d655);
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
        <div id="9e78b26bd1314dc38e11103f27c6bafb" class="chart-container" style="">
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
        <td>知识图谱算法工程师/专家</td>
        <td>北京·大兴区</td>
        <td>京东物流</td>
        <td>硕士</td>
        <td>经验5-10年</td>
        <td>物流｜运输</td>
        <td>A轮</td>
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
