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
                        <a href="/backend/intro/info">1a. More detail for Backend(Reasons&Components)</a>
                    </li>
                    <li class="nav-li">
                        <a href="/backend/intro/restapi" style="background-color: #111;">1b. An Introduction To REST APIs</a>
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
        <h1>What is REST APIs?</h1>
            <dd>
                <p>REST stands for Representational State Transfer. It is a set of protocols/standards that describe how communication should take place between the computers and other applications across the network.<br>
                To have a clear understanding let’s take the car example again. Suppose you want to drive a car so you know that you have to use accelerator, clutch etc. to drive it. The same way suppose a Web App wants to communicate to a Web Server. So, a Rest API uses GET, POST, PUT, DELETE methods to communicate.<br>
                Therefore, we can conclude that REST is an architectural style for designing network applications. It uses simple HTTP methods to communicate between clients and servers. But it should be noted that HTTP and REST are not same.<br>
                REST API as known to us a state of rules that developers follow when they create their API. One such rules says that we should be able to attain a specification when we link to a specific URL. This URL is a locator which when browsed to generates a request and the specification it gets is called a response.</p>
            </dd>

        <p><img src="img/Backend-main-page.png" alt="Backend Flowchart_2" height="500" width="1500"></p>
        <div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/sql"><span>START WITH SQL</span>
		</div>
	</div>
</div>