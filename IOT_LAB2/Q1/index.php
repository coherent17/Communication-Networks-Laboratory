<?php
	header("Content-Type:text/html;charset=utf-8");
	$Temperature=$_POST[T];
	$Humidity=$_POST[H];
	$SensorID=$_POST[s];
	
	echo 'Temperature:'.$Temperature. "\n";
	echo 'Humidity:' .$Humidity. "\n";
	
	if($SensorID==1){
		$fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/temp_1.txt','w');
		fwrite($fp,$Temperature);
		fclose($fp);
		$fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/humi_1.txt','w');
		fwrite($fp,$Humidity);
		fclose($fp);
	}

    if($SensorID==2){
        $fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/temp_2.txt','w');
        fwrite($fp,$Temperature);
        fclose($fp);
        $fp=fopen('/home/pi/Communication-Networks-Laboratory/IOT_LAB2/www-data/humi_2.txt','w');
        fwrite($fp,$Humidity);
        fclose($fp);
    }
?>
