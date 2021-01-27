<?php

$stdin = fgets(STDIN);

$strtrim = rtrim($stdin);

$arr = str_split($strtrim);
$len = strlen($strtrim);

while (true)
{
  $onemore_flg = 0;
  $cnt = 0;
  $cnt1 = 2;
  while (true)
  {
    $tmp = '';
    if ($arr[$cnt] > $arr[$cnt1])
    {
      $tmp = $arr[$cnt];
      $arr[$cnt] = $arr[$cnt1];
      $arr[$cnt1] = $tmp;
      $onemore_flg = 1;
    }

    if ($cnt1 >= $len-1)
    {
      break;
    }

    $cnt++;
    $cnt1++;
  }

  if ($onemore_flg == 0)
  {
    break;
  }
}

foreach ($arr as $value)
{
  print $value;
}

?>

