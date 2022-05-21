### Under the MVT Pattern
### 3rd, create web pages

WORKDIR="/root/coc-lens/backend"
cd $WORKDIR

######################################################################
# 1. Create home page
######################################################################

## template directory 생성
mkdir -p templates

## html code 생성
cat <<EOF | tee templates/home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    This is Home Page
</body>
</html>
EOF


######################################################################
# 2. Create blog pages
######################################################################

## template directory 생성
mkdir -p blog/templates/blog

## html code 생성
cat <<EOF | tee blog/templates/blog/post_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog List</title>
</head>
<body>
    This is Blog List Page
</body>
</html>
EOF

cat <<EOF | tee blog/templates/blog/post_detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Detail</title>
</head>
<body>
    This is Blog Detail Page
</body>
</html>
EOF


######################################################################
# 3. Create EmployeeApp pages
######################################################################

## for EmployeeApp template
mkdir -p EmployeeApp/templates/EmployeeApp

## html code 생성
cat <<EOF | tee EmployeeApp/templates/employee_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee List</title>
</head>
<body>
    This is Employee List Page
</body>
</html>
EOF

cat <<EOF | tee EmployeeApp/templates/employee_detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Detail</title>
</head>
<body>
    This is Employee Detail Page
</body>
</html>
EOF


######################################################################
# 4. Run Django web server
######################################################################

python manage.py runserver


######################################################################
# 5. Test if URLs works
######################################################################

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/blog/post/list/
http://127.0.0.1:8000/employee/list/

http://127.0.0.1:8000/blog/post/1/
http://127.0.0.1:8000/employee/1/
