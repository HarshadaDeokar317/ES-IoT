<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>WIFI Controlled LED</title>
</head>
       <body>
       <center><b><font size = '20'>Control LED:</b>       
         <form method="get" action="gpio.php">                 
                 <input type="submit" style = "font-size: 16 pt" value="OFF" name="off">
                 <input type="submit" style = "font-size: 16 pt" value="ON" name="on">
                 <input type="submit" style = "font-size: 16 pt" value="BLINK" name="blink">
         </form>
         <?php
         shell_exec("/usr/local/bin/gpio -g mode 33 out");
         if(isset($_GET['off']))
         {
		echo "LED is off";
		shell_exec("/usr/local/bin/gpio -g write 33 0");
         }
	else if(isset($_GET['on']))
	{
		echo "LED is on";
		shell_exec("/usr/local/bin/gpio -g write 33 1");
	}
	else if(isset($_GET['blink']))
	{
		echo "LED is blinking";
		for($x = 0;$x<=4;$x++)
		{
			shell_exec("/usr/local/bin/gpio -g write 33 1");
			sleep(1);
			shell_exec("/usr/local/bin/gpio -g write 33 0");
			sleep(1);
		}
	}
        ?>
   </center></font>
   </body>
 </html>
