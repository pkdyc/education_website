<head>
<link rel="stylesheet" type="text/css" href="/css/index.css">
<script src="js/redirect.js"></script>
</head>

<p>
<ul class="top-nav">
    <li class="top-nav-li"><a class="active" href="/home" id="home">Home</a></li>
    <li class="top-nav-li"><a href="/about" id="about">About</a></li>
    % if login_status == 'false':
      <li class="top-nav-li"><a href="/loginSQL" id="login">Login</a></li>
      <li class="top-nav-li"><a href="/registerSQL" id="register">Register</a></li>
    % else:
      <li class="top-nav-li">
        <form id="logout" method="post" action="/home">
            <input type="hidden" name="post_id" value="user_logout"/>
            <a class="button" id="logout" onclick="document.getElementById('logout').submit();">Logout</a>
        </form>
      </li>
    % end

    % if user_type == 'admin':
      <li class="top-nav-li"><a href="/admin">Admin Control</a></li>
    % end
</ul>
</p>