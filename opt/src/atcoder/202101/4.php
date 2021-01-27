<?php

$stdin = fgets(STDIN);

$strtrim = rtrim($stdin);

$array = explode(" ", $strtrim);

var_dump($array);

//foreach ($test as $value)
//{
//  echo $value . "\n";
//}


?>
