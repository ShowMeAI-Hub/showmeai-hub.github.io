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
            <button class="tablinks" onclick="showChart(event, 'd6965762178e487eb33de40a0899b660')">薪资</button>
            <button class="tablinks" onclick="showChart(event, '0883e09c72554eae92f572247285b54e')">实习薪资分布</button>
            <button class="tablinks" onclick="showChart(event, '74b88f68f32f4c55a0974024984d9a23')">社招薪资分布</button>
            <button class="tablinks" onclick="showChart(event, 'bdbf76e900634130890380d13d813152')">城市&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'de5924130a324201878e1aa3a67989fb')">薪资地图</button>
            <button class="tablinks" onclick="showChart(event, '6c7d44ef42534846ada01cdb38c7adbc')">区域&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'bbb7e1986e954cdbb8cc1ff0ff52cb0a')">行业&薪资</button>
            <button class="tablinks" onclick="showChart(event, '1ce1126498ec47f88422bcb5154d2e51')">方向关键词&薪资</button>
            <button class="tablinks" onclick="showChart(event, '8585f8778985448e9049083a3c324059')">学历&薪资</button>
            <button class="tablinks" onclick="showChart(event, 'fa4ad8f8f0d54390b8746e231f955efa')">经验&薪资</button>
            <button class="tablinks" onclick="showChart(event, '572e048281a6413fa36876d120379bf0')">top10薪资招聘</button>
    </div>

    <div class="box">
                <div id="d6965762178e487eb33de40a0899b660" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_d6965762178e487eb33de40a0899b660 = echarts.init(
            document.getElementById('d6965762178e487eb33de40a0899b660'), 'white', {renderer: 'canvas'});
            
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
    
        var option_d6965762178e487eb33de40a0899b660 = {
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
                334,
                211,
                205,
                178,
                121,
                120,
                113,
                82,
                78,
                62
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
                    "value": 334
                },
                {
                    "name": "25k-50k",
                    "value": 211
                },
                {
                    "name": "15k-30k",
                    "value": 205
                },
                {
                    "name": "30k-60k",
                    "value": 178
                },
                {
                    "name": "30k-50k",
                    "value": 121
                },
                {
                    "name": "20k-30k",
                    "value": 120
                },
                {
                    "name": "15k-25k",
                    "value": 113
                },
                {
                    "name": "25k-40k",
                    "value": 82
                },
                {
                    "name": "20k-35k",
                    "value": 78
                },
                {
                    "name": "25k-45k",
                    "value": 62
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
                    "value": 334
                },
                {
                    "name": "25k-50k",
                    "value": 211
                },
                {
                    "name": "15k-30k",
                    "value": 205
                },
                {
                    "name": "30k-60k",
                    "value": 178
                },
                {
                    "name": "30k-50k",
                    "value": 121
                },
                {
                    "name": "20k-30k",
                    "value": 120
                },
                {
                    "name": "15k-25k",
                    "value": 113
                },
                {
                    "name": "25k-40k",
                    "value": 82
                },
                {
                    "name": "20k-35k",
                    "value": 78
                },
                {
                    "name": "25k-45k",
                    "value": 62
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
        chart_d6965762178e487eb33de40a0899b660.setOption(option_d6965762178e487eb33de40a0899b660);
    </script>
                <div id="0883e09c72554eae92f572247285b54e" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_0883e09c72554eae92f572247285b54e = echarts.init(
            document.getElementById('0883e09c72554eae92f572247285b54e'), 'white', {renderer: 'canvas'});
            
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
    
        var option_0883e09c72554eae92f572247285b54e = {
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
                    6,
                    11,
                    18,
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
        chart_0883e09c72554eae92f572247285b54e.setOption(option_0883e09c72554eae92f572247285b54e);
    </script>
                <div id="74b88f68f32f4c55a0974024984d9a23" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_74b88f68f32f4c55a0974024984d9a23 = echarts.init(
            document.getElementById('74b88f68f32f4c55a0974024984d9a23'), 'white', {renderer: 'canvas'});
            
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
    
        var option_74b88f68f32f4c55a0974024984d9a23 = {
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
                    25.5,
                    38,
                    54.0,
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
        chart_74b88f68f32f4c55a0974024984d9a23.setOption(option_74b88f68f32f4c55a0974024984d9a23);
    </script>
                <div id="bdbf76e900634130890380d13d813152" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_bdbf76e900634130890380d13d813152 = echarts.init(
            document.getElementById('bdbf76e900634130890380d13d813152'), 'white', {renderer: 'canvas'});
        var option_bdbf76e900634130890380d13d813152 = {
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
                27.0,
                22.5,
                20.0,
                22.5,
                22.5,
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
                    27.5,
                    35.0,
                    40.0,
                    90.0
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    40.0,
                    80.0
                ],
                [
                    12.0,
                    23.0,
                    30.0,
                    37.5,
                    80.0
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
                    20.25,
                    27.0,
                    32.5,
                    75.0
                ],
                [
                    12.5,
                    20.0,
                    22.5,
                    28.125,
                    40.0
                ],
                [
                    12.5,
                    16.0,
                    20.0,
                    24.75,
                    37.5
                ],
                [
                    15.0,
                    20.0,
                    22.5,
                    30.0,
                    45.0
                ],
                [
                    15.0,
                    19.0,
                    22.5,
                    30.0,
                    50.0
                ],
                [
                    17.5,
                    25.0,
                    30.0,
                    37.5,
                    42.5
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
                "\u5357\u4eac",
                "\u4f5b\u5c71",
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
        chart_bdbf76e900634130890380d13d813152.setOption(option_bdbf76e900634130890380d13d813152);
    </script>
                <div id="de5924130a324201878e1aa3a67989fb" class="chart-container" style="width:900px; height:500px;"></div>
    <script>
        var chart_de5924130a324201878e1aa3a67989fb = echarts.init(
            document.getElementById('de5924130a324201878e1aa3a67989fb'), 'white', {renderer: 'canvas'});
            
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
    
        var option_de5924130a324201878e1aa3a67989fb = {
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
                        27.0
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
                        22.5
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
                    "name": "\u957f\u6c99",
                    "value": [
                        113,
                        28.21,
                        20.0
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
                    "name": "\u73e0\u6d77",
                    "value": [
                        113.52,
                        22.3,
                        19.5
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
                    "name": "\u90d1\u5dde",
                    "value": [
                        113.65,
                        34.76,
                        15.0
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
                    "name": "\u9752\u5c9b",
                    "value": [
                        120.33,
                        36.07,
                        17.5
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
                    "name": "\u5609\u5174",
                    "value": [
                        120.76,
                        30.77,
                        14.0
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
                    "name": "\u4e1c\u839e",
                    "value": [
                        113.75,
                        23.04,
                        24.0
                    ]
                },
                {
                    "name": "\u5b81\u6ce2",
                    "value": [
                        121.56,
                        29.86,
                        14.0
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
        chart_de5924130a324201878e1aa3a67989fb.setOption(option_de5924130a324201878e1aa3a67989fb);
    </script>
                <div id="6c7d44ef42534846ada01cdb38c7adbc" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_6c7d44ef42534846ada01cdb38c7adbc = echarts.init(
            document.getElementById('6c7d44ef42534846ada01cdb38c7adbc'), 'white', {renderer: 'canvas'});
        var option_6c7d44ef42534846ada01cdb38c7adbc = {
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
                35.0,
                32.5,
                30.0,
                30.0,
                22.5,
                30.0,
                37.5,
                30.0,
                37.5,
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
                    27.5,
                    35.0,
                    40.0,
                    75.0
                ],
                [
                    13.5,
                    30.0,
                    35.0,
                    45.0,
                    80.0
                ],
                [
                    12.5,
                    27.375,
                    32.5,
                    37.5,
                    65.0
                ],
                [
                    16.0,
                    25.0,
                    30.0,
                    39.0,
                    55.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    38.75,
                    67.5
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.5,
                    20.0,
                    22.5,
                    30.0,
                    40.0
                ],
                [
                    12.0,
                    27.5,
                    37.5,
                    45.0,
                    75.0
                ],
                [
                    15.0,
                    25.0,
                    30.5,
                    45.0,
                    75.0
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    42.5,
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
                "\u6d77\u6dc0\u533a",
                "\u671d\u9633\u533a",
                "\u5357\u5c71\u533a",
                "\u4f59\u676d\u533a",
                "\u6d66\u4e1c\u65b0\u2026",
                "\u9ad8\u65b0\u533a",
                "\u79d1\u6280\u56ed",
                "\u671b\u4eac",
                "\u5b9d\u5b89\u533a",
                "\u4e2d\u5173\u6751",
                "\u897f\u6e56\u533a"
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
                "\u6d66\u4e1c\u65b0\u2026",
                "\u4f59\u676d\u533a",
                "\u79d1\u6280\u56ed",
                "\u9ad8\u65b0\u533a",
                "\u671b\u4eac",
                "\u5f90\u6c47\u533a",
                "\u5b9d\u5b89\u533a"
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
        chart_6c7d44ef42534846ada01cdb38c7adbc.setOption(option_6c7d44ef42534846ada01cdb38c7adbc);
    </script>
                <div id="bbb7e1986e954cdbb8cc1ff0ff52cb0a" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_bbb7e1986e954cdbb8cc1ff0ff52cb0a = echarts.init(
            document.getElementById('bbb7e1986e954cdbb8cc1ff0ff52cb0a'), 'white', {renderer: 'canvas'});
        var option_bbb7e1986e954cdbb8cc1ff0ff52cb0a = {
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
                37.5,
                35.0,
                30.0,
                25.5,
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
                    20.0,
                    25.5,
                    37.5,
                    75.0
                ],
                [
                    12.5,
                    22.5,
                    30.0,
                    37.5,
                    80.0
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
                    80.0
                ],
                [
                    12.0,
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
                    22.5,
                    28.0,
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
                "\u77ed\u89c6\u9891",
                "\u7535\u5546\u5e73\u53f0",
                "\u76f4\u64ad\u5e73\u53f0",
                "\u7269\u8054\u7f51",
                "IT\u6280\u672f\u670d\u52a1",
                "\u786c\u4ef6",
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
        chart_bbb7e1986e954cdbb8cc1ff0ff52cb0a.setOption(option_bbb7e1986e954cdbb8cc1ff0ff52cb0a);
    </script>
                <div id="1ce1126498ec47f88422bcb5154d2e51" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_1ce1126498ec47f88422bcb5154d2e51 = echarts.init(
            document.getElementById('1ce1126498ec47f88422bcb5154d2e51'), 'white', {renderer: 'canvas'});
        var option_1ce1126498ec47f88422bcb5154d2e51 = {
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
                32.5,
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
                    12.0,
                    22.5,
                    30.0,
                    37.5,
                    80.0
                ],
                [
                    12.5,
                    20.0,
                    26.5,
                    35.0,
                    75.0
                ],
                [
                    12.5,
                    27.5,
                    32.5,
                    41.25,
                    85.0
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
                    25.375,
                    32.5,
                    41.875,
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
                "\u63a8\u8350\u7b97\u6cd5",
                "\u6df1\u5ea6\u5b66\u4e60",
                "Python",
                "\u6570\u636e\u6316\u6398",
                "\u4eba\u5de5\u667a\u80fd\u670d\u52a1",
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
        chart_1ce1126498ec47f88422bcb5154d2e51.setOption(option_1ce1126498ec47f88422bcb5154d2e51);
    </script>
                <div id="8585f8778985448e9049083a3c324059" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_8585f8778985448e9049083a3c324059 = echarts.init(
            document.getElementById('8585f8778985448e9049083a3c324059'), 'white', {renderer: 'canvas'});
        var option_8585f8778985448e9049083a3c324059 = {
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
                20.0,
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
                    37.5,
                    40.0,
                    50.0,
                    80.0
                ],
                [
                    14.5,
                    15.0,
                    17.5,
                    22.0,
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
                    12.0,
                    15.0,
                    20.0,
                    23.25,
                    34.5
                ],
                [
                    12.0,
                    22.5,
                    30.0,
                    37.75,
                    90.0
                ],
                [
                    12.0,
                    25.0,
                    30.0,
                    37.5,
                    80.0
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
        chart_8585f8778985448e9049083a3c324059.setOption(option_8585f8778985448e9049083a3c324059);
    </script>
                <div id="fa4ad8f8f0d54390b8746e231f955efa" class="chart-container" style="width:900px; height:900px;"></div>
    <script>
        var chart_fa4ad8f8f0d54390b8746e231f955efa = echarts.init(
            document.getElementById('fa4ad8f8f0d54390b8746e231f955efa'), 'white', {renderer: 'canvas'});
        var option_fa4ad8f8f0d54390b8746e231f955efa = {
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
                47.5,
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
                    80.0
                ],
                [
                    30.0,
                    37.5,
                    47.5,
                    61.25,
                    65.0
                ],
                [
                    13.5,
                    15.0,
                    22.5,
                    22.5,
                    25.0
                ],
                [
                    12.5,
                    25.0,
                    30.0,
                    37.75,
                    80.0
                ],
                [
                    12.5,
                    32.5,
                    40.0,
                    50.0,
                    90.0
                ],
                [
                    12.0,
                    25.0,
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
        chart_fa4ad8f8f0d54390b8746e231f955efa.setOption(option_fa4ad8f8f0d54390b8746e231f955efa);
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
        <div id="572e048281a6413fa36876d120379bf0" class="chart-container" style="">
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
        <td>推荐/广告算法专家</td>
        <td>北京·白石桥</td>
        <td>易车公司</td>
        <td>本科</td>
        <td>经验5-10年</td>
        <td>汽车交易平台</td>
        <td>上市公司</td>
        <td>2000人以上</td>
        <td>70k-100k</td>
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
        <td>算法经理</td>
        <td>上海·虹梅路</td>
        <td>思贤科技</td>
        <td>硕士</td>
        <td>经验3-5年</td>
        <td>数据服务｜咨询,人工智能服务</td>
        <td>B轮</td>
        <td>50-150人</td>
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
        <td>算法leader-直播</td>
        <td>北京·海淀区</td>
        <td>字节跳动</td>
        <td>本科</td>
        <td>经验不限</td>
        <td>内容资讯,短视频</td>
        <td>D轮及以上</td>
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
