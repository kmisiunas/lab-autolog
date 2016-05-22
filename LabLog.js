function LabLogView(Key){


	var TemperatureSeries = [],
		yAxisOptions = [],
		colors = Highcharts.getOptions().colors;
	var HumiditySeries = []
	var PressureSeries = []
	var LightSeries = []
	var VibrationSeries = []
		
	var count = 0
	var dataT = []
	var dataH = []
	var dataCPU_T = []
	var dataLight = []
	var dataPressure = []
	var dataVibration = []
	var dataVibrationPeaks = []
	
	var public_key = Key; //'OGzNYR7mdEFgYOON7g8m';
	
	
/* 	var jsonData = $.ajax({
          url: 'https://data.sparkfun.com/output/' + public_key + '.json',
          //data: {page: 1},
          dataType: 'jsonp',
        }).done(function (results) { */
		
	//Note that the type of request to ThingSpeak determines whether the data is returned reversed or not
	// If there is argument for the amount of data it will return oldest first.
	//https://thingspeak.com/docs/channels#get_feed
	var jsonData = $.ajax({
          url: 'https://api.thingspeak.com/channels/64199/feed.json?days=5&key=95I64JA4ZB53XDTP&start=2015-11-1%2012:00:00',
          //data: {page: 1},
          dataType: 'jsonp',
        }).done(function (results) {
	
		//$.getJSON('https://data.sparkfun.com/output/' + public_key + '.json',	function(results) {

				
/* 			$.each(results, function (i, row) {
				var DateTime = new Date(row.timestamp)
				var d = DateTime.valueOf()
				//console.log(d)
				//dataT[count] = [d,parseFloat(row.temp)]
				dataT.push([d,parseFloat(row.temp)])
				dataH.push([d,parseFloat(row.humidity)])
				dataCPU_T.push([d,parseFloat(row.cpu_temp)])
				dataLight.push([d,parseFloat(row.light)])
				dataPressure.push([d,parseFloat(row.pressure)])
				dataVibration.push([d,parseFloat(row.vibration)])
				dataVibrationPeaks.push([d,parseFloat(row.vibration_peaks)])
				count++
				
          }); */
		  
		  $.each(results.feeds, function (i, row) {
				var DateTime = new Date(row.created_at)
				var d = DateTime.valueOf()
				//console.log(d)
				//dataT[count] = [d,parseFloat(row.temp)]
				dataT.push([d,parseFloat(row.field1)])
				dataH.push([d,parseFloat(row.field2)])
				dataCPU_T.push([d,parseFloat(row.field4)])
				dataLight.push([d,parseFloat(row.field5)])
				dataPressure.push([d,parseFloat(row.field3)])
				dataVibration.push([d,parseFloat(row.field6)])
				dataVibrationPeaks.push([d,parseFloat(row.field7)])
				count++
				
          });

			//Now construct series for highcharts  - note may need to reverse arrays depending on data source			
			TemperatureSeries[0] = {
				name: 'Temp',
				data: dataT  //.reverse()
			};
			TemperatureSeries[1] = {
				name: 'CPU Temperature',
				data: dataCPU_T  //.reverse()
			};
			HumiditySeries[0] = {
				name: 'Humidity',
				data: dataH  //.reverse()
			};

			PressureSeries[0] = {
				name: 'Pressure',
				data: dataPressure  //.reverse()
			};
			LightSeries[0] = {
				name: 'Light',
				data: dataLight  //.reverse()
			};
			VibrationSeries[0] = {
				name: 'Vibration',
				data: dataVibration  //.reverse()
			};
			VibrationSeries[1] = {
				name: 'VibrationPeaks',
				data: dataVibrationPeaks  //.reverse()
			};

			CreateCharts()
		});




	// create the chart when all data is loaded
	function CreateCharts(){
		createChart('Temperature', TemperatureSeries,'Temperature(C)')
		createChart('Pressure', PressureSeries,'Pressure (mB)')
		createChart('Light', LightSeries,'Light (%)')
		createChart('Vibration', VibrationSeries,'Vibration')
		createChart('Humidity', HumiditySeries,'Humidity %')
			}
	
	function createChart(PlotContainer, Series, YAxisName) {
		chart = new Highcharts.StockChart({
		    chart: {
		        renderTo: PlotContainer
		    },

		    rangeSelector: {
		        buttons: [{
		            type: 'day',
		            count: 1,
		            text: '1d'
		        }, {
		            type: 'day',
		            count: 3,
		            text: '3d'
		        }, {
		            type: 'week',
		            count: 1,
		            text: '1w'
		        }, {
		            type: 'month',
		            count: 1,
		            text: '1m'
		        }, {
		            type: 'month',
		            count: 6,
		            text: '6m'
		        }, {
		            type: 'year',
		            count: 1,
		            text: '1y'
		        }, {
		            type: 'all',
		            text: 'All'
		        }],
		        selected: 3
		    },
			legend: {
		            layout: 'vertical',
		            align: 'right',
		            verticalAlign: 'middle',
		            borderWidth: 0,
					enabled: true
		        },	
			xAxis: {       
				ordinal: false
			},
		    yAxis: {
		    		title: {
					text: YAxisName
				}
		    	,
		    	plotLines: [{
		    		value: 0,
		    		width: 2,
		    		color: 'silver'
		    	}]
		    },
		    plotOptions: {
		    	
		    },
		    tooltip: {
		    	//pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
		    	pointInterval: 60,
				valueDecimals: 2,
				dateTimeLabelFormats: '%A, %b %e, %H:%M'
		    },
		    series: Series
		});
	}
	}
