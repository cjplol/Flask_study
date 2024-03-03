function validateForm(){
    var username=document.getElementById('username').value;
    var password=document.getElementById('password').value;
    console.log("账号为："+username,"密码为："+password)
    if (username.trim() === '' || password.trim() === '') {
                alert('账号和密码不能为空！');
                return false;
            }
    else {
        localStorage.setItem('username',username)
        alert('登录成功！');
        // 这里可能还需要其它操作，比如提交表单
        window.location.href='index.html';
    }

    return true; // 表示表单验证通过
}