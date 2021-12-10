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
					<a href="/backend/sql" style="background-color: #111;">2. Introduction for SQLite3</a>
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
		<dl>
			<dt>
				<h1>What is SQLite3?</h1>
				<dd>
					<p>
						SQLite is an in-process library that implements a self-sufficient, serverless, zero-configuration, transactional SQL database engine. It is a zero-configuration database, which means that unlike other databases, you do not need to configure it in the system.
					<br>
						Just like other databases, the SQLite engine is not an independent process, and can be statically or dynamically connected according to application requirements. SQLite directly accesses its storage files.
					</p>
					<dd><img src="img/sql.png" alt="SQL"></dd>
				</dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/sql/connect"><span>LEARN MORE SQL</span>
		</div>

	</div>
</div>