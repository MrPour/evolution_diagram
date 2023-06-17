const titleTextSize1 = 60;
const subtitleTextFigureSize1 = 40;
const subtitleTextNormalSize1 = 20;
const titleTextSize2 = 50;
const subtitleTextSize2 = 20;
const spotSize = 15;

let option = {
    title: [{
        text: 'Evolution diagram',
        subtext:'',
        top: '5.3%',
        x: 'center',
        textStyle: {
            color: '#000000',
            fontSize: titleTextSize1
        },
        subtextStyle:{
        rich:
            {
            b:{
                color: '#FF9900',
                fontSize:subtitleTextFigureSize1
            },a:
            {
                    color:  '#000000',
                fontSize:subtitleTextNormalSize1
            }
        }
        }
    },{
        text: '',
        subtext:'',
        left: '20.3%',
        top: '12.3%',
        textStyle: {
            color: '#000000',
            fontSize: titleTextSize2
        },
        subtextStyle:{
            color: '#3642db',
            fontSize: subtitleTextSize2
        }
    }],
    geo: {
        map: 'world',
        show:true,
        top:'20%',
        zoom:1,
        itemStyle:{
            color : "#CCCCCC",
            borderWidth : 0
        }
    },
    color:'#99CC99',
    blendMode:'',
    series: [
        {
            name: 'plant',
            type: 'scatter',
            progressive:200,
            animation:false,
            coordinateSystem: 'geo',
            data: [],
            tooltip: {
                show:true,
                trigger: 'item'
            },
            encode: {
                value: 2
            },
            symbolSize: spotSize,
            itemStyle: {
                color :  (params)=>{
                    return params.data.color
                },
                opacity:0.5
            },
            emphasis: {
                label: {
                    show: true
                }
            }
        }]}

let option2 = {
    title: [{
        text: 'Evolution diagram',
        subtext:'',
        x: 'center',
        top: '5.3%',
        textStyle: {
            color: '#000000',
            fontSize: titleTextSize2
        },
        subtextStyle:{
            color: '#FF9900',
            fontSize: subtitleTextSize2
        }
    },{
        text: '',
        subtext:'',
        left: '3.3%',
        top: '12.3%',
        textStyle: {
            color: '#000000',
            fontSize: 30
        },
        subtextStyle:{
            color: '#3642db',
            fontSize: 20
        }
    }],

    geo: {
        map: 'world',
        show:true,
        roam:false,
        top:'10%',
        zoom:1,
        itemStyle:{
            color : "#CCCCCC",
            borderWidth : 0
        }
    },
    color:'#99CC99',
    blendMode:'',
    legend : {
        orient : 'vertical',
        y : 'bottom',
        x : 'center',
        orient:'horizontal',
        data : ['plant'],
        textStyle : {
            color : '#333333'
        }
    },
    tooltip : {
        trigger : 'item',
        formatter : '{b}'
    },
    series: []
}
