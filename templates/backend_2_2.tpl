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
							<a href="/backend/sql/table" style="background-color: #111;">2b. Creating a new SQLite database</a>
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
				<h1>Creating a new SQLite database</h1>
				<h3>A. Firstly, use a cursor to create a person table, which contains 3 columns such as id, name, and age. The code is as follows:</h3> 
				<dd><pre class="prettyprint"><code class=" hljs sql">cur.execute(&#39;<span class="hljs-operator"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> person (id <span class="hljs-keyword">integer</span> <span class="hljs-keyword">primary</span> <span class="hljs-keyword">key</span> ,name <span class="hljs-keyword">varchar</span>(<span class="hljs-number">20</span>),age <span class="hljs-keyword">integer</span>)<span class="hljs-string">&#39;)</span></span></code></pre></dd>
				<p>
					Let us have a look at some example code to create a new SQLite database file with two tables: One with and one without a PRIMARY KEY column (don’t worry, there is more information about PRIMARY KEYs further down in this section).
						<dd><img src="img/sql_table.png" alt="SQL Table"></dd>
				</p>

				<h3>B. Here is a quick overview of all data types that are supported by SQLite 3:</h3>
				<dd>
					INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.<br />
					REAL: An 8-byte floating point value.<br />
					TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).<br />
					BLOB: A blob of data (binary large object) for storing binary data.<br />
					NULL: A NULL value, represents missing data or an empty cell.
				</dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/sql/insert"><span>LEARN INSERT DATA</span>
		</div>

	</div>
</div>