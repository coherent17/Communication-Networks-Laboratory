<?php
	header("Content-Type:text/html;charset=utf-8");
	$SensorID=$_POST[s];
	$month=$_POST[m];
	$date=$_POST[d];

	if($SensorID==3){
		$fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/month.txt','w');
		fwrite($fp,$month);
		fclose($fp);
		$fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/date.txt','w');
		fwrite($fp,$date);
		fclose($fp);
	}
?>
