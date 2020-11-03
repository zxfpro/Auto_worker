wode = 12
app_start_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>%s测试页</title>
    <link rel="stylesheet" href="{wode}/appname/static/appname/css/appname.css">
</head>
<body>
<form action="/%s/appstart" method="post">
    <p>
        标题：<input type="text"name="test1">
        <input type="submit" value="保存">
    </p>
    <textarea name="content" id="50" cols="30" rows="10"></textarea>

</form>
<div>
    {{ test1 }}
    {{ content }}
</div>
<script src="%s/appname/static/appname/js/appname.js"></script>
</body>
</html>

"""
print(app_start_html)