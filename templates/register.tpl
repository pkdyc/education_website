<link rel="stylesheet" type="text/css" href="css/login.css">

<div class="register">
    <div class="login-container">
      <h1>Register</h1>

      <form class="register-box" action="/registerSQL" method="post">
        <p>
          Username:
          <input
            id="username"
            type="text"
            required="required"
            placeholder="Enter your username"
            name="username"
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
          />
        </p>

        %if register_status == 'success':
            <p>Success</p>
        %elif register_status == 'failed':
            <p>Failed : already a user with this username exist</p>
        %else:
            <p>{{register_status}}</p>
        %end

        <button class="register-btn" id="register-submit" type="submit">
        Sign Up
        </button>
        <br />

      </form>
      <br />
      <button class="return-btn" type="submit" onclick="jumpToLogin()">
        Back
      </button>
    </div>
</div>