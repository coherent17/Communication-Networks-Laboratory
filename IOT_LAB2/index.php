<?php
	header("Content-Type:text/html;charset=utf-8");
	$Temperature=$_POST[Temp];
	$SensorID=$_POST[sensor];
	
	echo 'Temperature:'.$Temperature. "\n";
	
	if($SensorID==1){
	$fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/temp.txt','w');
	fwrite($fp,$Temperature);
	fclose($fp);
}
?>
