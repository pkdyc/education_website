<link rel="stylesheet" type="text/css" href="css/home.css">

<div class="home">
    <div class="top-info">    
        <h1 style="color: white; padding-top:160px; font-size: 360%;">
            Learn to build a website 
        </h1>
        <h2 style="color: white; font-size: 200%;">in 3 steps</h2>
    </div>

    <div class="main-nav">
        <div class="btn" onclick="introSub1OnClick()">
            <h3 style="color: white">STEP 1</h3>
            <img src="img/overview.png">
        </div>
        <div class="btn" onclick="backendSub1OnClick()">
            <h3 style="color: white">STEP 2</h3>
            <img src="img/backend.png">
        </div>
        <div class="btn" onclick="frontendSub1OnClick()">
            <h3 style="color: white">STEP 3</h3>
            <img src="img/frontend.png">
        </div>
        <div class="btn" onclick="practiceOnClick()">
            <h3 style="color: white">Practice your HTML5 skills here</h3>
            <img src="img/practice.png">
        </div>
    </div>
    
    <div class="bottom-info">
        <h1 style="color: white; padding-top:160px">
            <p>Share your ideas with others </p>
            <p>in our discussion form</p>
        </h1>
        %if login_status == 'false':
            <h2 style="color: white; padding-top:40px">
                <p>Login to use discussion form</p>
            </h2>
        %else:
            <div style="text-align: center; padding: 20px; margin-right: 30px; margin-left: 42%;">
                <div class="btn-1">
                    <a href="/chatroom" id="discussion-entry"><span>Discussion Form</span></a>
                </div>
            </div>
        %end
    </div>
</div>