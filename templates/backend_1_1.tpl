<link rel="stylesheet" type="text/css" href="css/tutorial.css">

<div class="tutorial-container">
	<div class="nav-div">
        <ul class="nav-list">
            <li class="nav-title">
                <h3>CHAPTER 2 
                <h4>BACKEND
            </li>
            <li class="nav-li">
                <a href="/backend/intro">1. Backend Introduction</a>
                <ul>
                    <li class="nav-li">
                        <a href="/backend/intro/info" style="background-color: #111;">1a. More detail for Backend(Reasons&Components)</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/intro/restapi">1b. An Introduction To REST APIs</a>
                    </li>
                </ul>
            </li>
            <li class="nav-li">
                <a href="/backend/sql">2. Introduction for SQLite3</a>
                <ul>
                    <li class="nav-li">
                        <a href="/backend/sql/connect">2a. Connecting to an SQLite database</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/sql/table">2b. Creating a new SQLite database</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/sql/insert">2c. Insert data in SQLite</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/sql/query">2d. Query data in SQLite</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/sql/delete">2e. Modify and delete data</a>
                    </li>
                </ul>
            </li>
            <li class="nav-li">
					<a href="/backend/bottle">3. Introduction for Bottle</a>
					<ul>
						<li class="nav-li">
							<a href="/backend/bottle/route">3a. The purpose of route()</a>
						</li>
						<li class="nav-li">
							<a href="/backend/bottle/gp">3b. How to use GET and POST</a>
						</li>
					</ul>
				</li>
            <li class="nav-li">
                <a href="/backend/end">4. Summary</a>
            </li>
        </ul>
	</div>
	<div class="content-div">
        <h1>Why does the web need a backend?</h1>
            <dd>
                The answer is same as what the backend does- it is used to hide the processing of any request from the user. The backend includes processing, database and in total the whole machinery of any application. If it gets available to the user the he can easily modify it and see the databases as well. Therefore, the reason for having backend is to have a central processing point for everyone so that user doesn’t need to install any extra application apart from the browser. Also having a backend means you are hiding the machinery of the application which means a user cannot see the databases and sensitive content unless there is a security vulnerability.
            </dd>
        <br>
        <h1>Components of a backend.</h1>
            <dd>
                <p>1. Server- It is the place where backend is stored and run. These are high-powered computers that provides resources which the backend needs i.e. file storage space, processing power, security and encryption, databases and other web services.<br>
                2. Database- It is the brain of any Website that makes it dynamic. If you are searching for anything on a website be it a profile on any social media or any product on E-commerce website it is the role of a database to take the query and fetch the required data to the user.<br>
                3. Middleware- It is any software (Server-side) that facilitates the connection between the frontend and the backend. It acts as a medium that takes requests from the user and provides it to the backend and then facilitate the user with a response given by the backend.<br>
                4. Programming Languages and frameworks- There is a variety of languages available in which the backend can be coded however, the language is chosen based upon the usage because of the difference in their performance, memory usage, compatibility etc.</p>
            </dd>

        <div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
            <a href="/backend/intro/restapi"><span>LEARN REST APIs</span>
		</div>
	</div>
</div>