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
							<a href="/backend/bottle/route" style="background-color: #111;">3a. The purpose of route()</a>
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
		<dl>
			<dt> <h1>The purpose of route()</h1>
					<dd>
						<h3>route(path, method='GET', callback=None, **options)</h3>
                        The route() decoration combines a piece of code into a URL path. In this case, we link the /hello path to the hello() function. This is called routing (hence the decorator name) and is the most important concept of this framework. You can define as many routes as you need. Whenever the browser requests a URL, it will call the associated function and send the return value back to the browser. (“Bottle Tutorial”,2021)
					</dd>
                    <dd><p><img src="img/bottle_route.png" alt="Bottle_route"></p></dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px; ">
            <div class="btn-1">
                <a href="/backend/bottle/gp"><span>LEARN GET&POST</span></a>
            </div>
        </div>

	</div>
</div>