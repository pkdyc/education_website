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
							<a href="/backend/sql/connect" style="background-color: #111;">2a. Connecting to an SQLite database</a>
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
				<h1>Connecting to an SQLite database</h1>
				<h3>The sqlite3 that we will be using throughout this tutorial is part of the Python Standard Library and is a nice and easy interface to SQLite databases: There are no server processes involved, no configurations required, and no other obstacles we have to worry about. In general, the only thing that needs to be done before we can perform any operation on a SQLite database via Python’s sqlite3 module, is to open a connection to an SQLite database file:</h3>
				<dd>
					<img src="img/sql_import.png" alt="SQL" height="100" width="800">
					<h5>Code Explain</h5>
					<pre class="prettyprint">Line1: Import module<code class=" hljs java"><span class="hljs-keyword">import</span> sqlite3</code></pre> 
					<pre class="prettyprint">Line2: Establish connection<code class=" hljs tex">conn &#61; sqlite3.connect(sqlite_file)</code></pre> 
					<p>The query to the database needs to use the cursor object, Firstly create a cursor object through cursor().</p>
					<pre class="prettyprint">Line3: Use of cursor objects<code class=" hljs fix"><span class="hljs-attribute">c </span>&#61;<span class="hljs-string"> con.cursor()</span></code></pre>
				</dd>

				<h3>where the database file (sqlite_file) can reside anywhere on our disk, e.g.,</h3>
				<dd><img src="img/sql_file.png" alt="SQL_file"></dd>

				<h3>
					Conveniently, a new database file (.sqlite file) will be created automatically the first time we try to connect to a database. However, we have to be aware that it won’t have a table, yet. In the following section, we will take a look at some example code of how to create a new SQLite database files with tables for storing some data.<br />
					To round up this section about connecting to a SQLite database file, there are two more operations that are worth mentioning. If we are finished with our operations on the database file, we have to close the connection via the .close() method:
				</h3>
				<dd><img src="img/sql_close_1.png" alt="sqL_close_1"></dd>

				<h3>And if we performed any operation on the database other than sending queries, we need to commit those changes via the .commit() method before we close the connection:</h3>
				<dd><img src="img/sql_close_2.png" alt="sql_close_2"></dd>
				
				<h3>
					The connect method returns the con object, which is the database link object, and it provides the following methods: <br /> 
					<dd>.cursor() method to create a cursor object <br> 
						.commit() method to handle transaction commit <br> 
						.rollback() method to handle transaction rollback <br> 
						.close() method to close a database connection</dd>
					</h3> 
				</dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/sql/table"><span>LEARN SQL TABLE</span>
		</div>

	</div>
</div>