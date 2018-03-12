<?php
 $res=exec("watson.py /tmp");
  $array=json_decode($res);
  foreach($array as $row)
     echo $row.'<br>';
     
?>
