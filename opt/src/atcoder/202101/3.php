<?php

$stdin = fgets(STDIN);

$strtrim = rtrim($stdin);

$array = explode(" ", $strtrim);


$R = 0;
$W = 0;
$winner = "";

foreach($array as $value)
{
  if ($value == "RU" and $R == 0)
  {
    $R = 1;
  }
  elseif ($value == "RU" and $R == 1) 
  {
    $winner = "Alice";
    break;
  }
  elseif ($value == "RD" and $R == 0) 
  {
    $winner = "Alice";
    break;
  }
  elseif ($value == "RD" and $R == 1) 
  {
    $R = 0;
  }

  if ($value == "WU" and $W == 0)
  {
    $W = 1;
  }
  elseif ($value == "WU" and $W == 1)
  {
    $winner = "Alice";
    break;
  }
  elseif ($value == "WD" and $W == 0)
  {
    $winner = "Alice";
    break;
  }
  elseif ($value == "WD" and $W == 1)
  {
    $W = 0;
  }
}


if ($winner == "Alice")
{
  print $winner;
}
else
{
  print "Simon\n";
  if ($R == 1 && $W == 1)
  {
    print "UU\n";
  }
  elseif ($R == 1 && $W == 0)
  {
    print "UD\n";
  }
  elseif ($R == 0 && $W == 1)
  {
    print "DU\n";
  }
  elseif ($R == 0 && $W == 0)
  {
    print "DD\n";
  }
}


?>
