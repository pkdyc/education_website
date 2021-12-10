
<link rel="stylesheet" type="text/css" href="css/login.css">
<div class="login">
    <div class="login-container">
        <h1>Login</h1>
        <div class="login-content">
            <form class="login-box" form action="/loginSQL" method="post">
                <p>
                Username:
                <input
                    id="username"
                    type="text"
                    required="required"
                    placeholder="Enter your username"
                    name="username"
                    class="username_input"
                />
                </p>
                <p>
                Password:
                <input
                    id="password"
                    type="password"
                    required="required"
                    placeholder="Enter your password"
                    name="password"
                    class="password_input"
                />
                </p>

                %if login_attempt == 'failed':
                    <p style="color: red;"><h3>Invalid username or password</h3></p>
                %end
                %if login_attempt == 'invalid_syntax':
                    <p style="color: red;"><h3>invalided input : contains invalid character [.\+?-;=/]</h3></p>
                %end
                <div class="login-box">
                    <button class="login-btn" id="login-submit" type="submit" v-on:click="handleLogin">
                    login
                    </button>
                </div>
            </form>

            <br />
            <h4>OR</h4>
            <button class="register-btn" onclick="jumpToRegister()">sign up</button>
        </div>
    </div>
</div>
