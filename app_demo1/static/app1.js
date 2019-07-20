	document.load(
	$.ajax({
        		url:"/ajax/",
        		type:"POST",
        		data:{

        			"username":"name1",
        			"password":"pass1"
        		},
        		success:function(data){
        			var dataobj=JSON.parse(data);
                    console.log(dataobj)
        		}


        	}

        		)


			var data = [
			         	{
			         		name : '便利店',
			         		value:[9,12,10,11,16],
			         		color:'#e0b645'
			         	},
			         	{
			         		name : '超市',
			         		value:[63,42,38,21,14],
			         		color:'#7876ba'
			         	},
			         	{
			         		name : '大型超市',
			         		value:[32,19,23,11,7],
			         		color:'#6b8439'
			         	}
			         ];
	        
			var chart = new iChart.ColumnStacked3D({
					render : 'canvasDiv',
					data: data,
					labels:["浙江","江苏","广东","北京","上海"],
					title : {
						text:'连锁零售企业总部(总店)数TOP5',
						color:'#254d70'
					},
					footnote : '数据来源：中华人民共和国国家统计局',
					width : 800,
					height : 400,
					column_width:70,
					background_color : '#ffffff',
					shadow : true,
					shadow_blur : 3,
					shadow_color : '#aaaaaa',
					shadow_offsetx : 1,
					shadow_offsety : 0, 
					sub_option:{
						label:{color:'#f9f9f9',fontsize:12,fontweight:600},
						border : {
							width : 2,
							color : '#ffffff'
						} 
					},
					label:{color:'#254d70',fontsize:12,fontweight:600},
					legend:{
						enable:true,
						background_color : null,
						line_height:25,
						color:'#254d70',
						fontsize:12,
						fontweight:600,
						border : {
							enable : false
						}
					},
					tip:{
						enable :true,
						listeners:{
							//tip:提示框对象、name:数据名称、value:数据值、text:当前文本、i:数据点的索引
							parseText:function(tip,name,value,text,i){
								return name+":"+value+ '个';
							}
						} 
					},
					text_space : 16,//坐标系下方的label距离坐标系的距离。
					zScale:0.5,
					xAngle : 50,
					bottom_scale:1.1, 
					coordinate:{
						width:'74%',
						height:'80%',
						board_deep:10,//背面厚度
						pedestal_height:10,//底座高度
						left_board:false,//取消左侧面板 
						shadow:true,//底座的阴影效果
						grid_color:'#6a6a80',//网格线
						wall_style:[{//坐标系的各个面样式
						color : '#6a6a80'
						},{
						color : '#b2b2d3'
						}, {
						color : '#a6a6cb'
						},{
						color : '#6a6a80'
						},{
						color : '#74749b'
						},{
						color : '#a6a6cb'
						}], 
						axis : {
							color : '#c0d0e0',
							width : 0
						}, 
						scale:[{
							 position:'left',	
							 scale_enable : false,
							 start_scale:0,
							 scale_space:20,
							 end_scale:120,
							 label:{color:'#254d70',fontsize:11,fontweight:600}
						}]
					}
			});

			//利用自定义组件构造左上侧单位
			chart.plugin(new iChart.Custom({
					drawFn:function(){
						//计算位置
						var coo = chart.getCoordinate(),
							x = coo.get('originx'),
							y = coo.get('originy');
						//在左上侧的位置，渲染一个单位的文字
						chart.target.textAlign('end')
						.textBaseline('bottom')
						.textFont('600 12px 微软雅黑')
						.fillText('单位(个)',x+10,y-20,false,'#254d70')
						
					}
			}));
			
			chart.draw();
		)