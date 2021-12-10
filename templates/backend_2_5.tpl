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
                            <a href="/backend/sql/delete" style="background-color: #111;">2e. Modify and delete data</a>
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
				<h1>How to Modify and delete data?</h1>
                <h3>A. Firstly</h3>
                    <dd><img src="img/backend_2_5_p1.png" alt="SQL Picture" height="150" width="800"></dd>
                
                <h3>B. Query again to modify the data after deletion</h3>
                    <dd><img src="img/backend_2_5_p2.png" alt="SQL Picture" height="150" width="800"></dd>
                    
                <h3>C. Finally</h3>
                    <dd><pre class="prettyprint"><code class=" hljs livecodeserver">con.<span class="hljs-built_in">close</span>()  <span class="hljs-comment"># Close database link</span></code></pre></dd>
                </p>
				<h3>D. Results for SQLite</h3>
					<dd>
							Loop the value of fetchall&gt;&gt;&gt; (1, ‘leon’, 22) <br /> 
							Loop the value of fetchall&gt;&gt;&gt; (2, ‘name2’, 28) <br /> 
							Loop the value of fetchall&gt;&gt;&gt; (3, ‘name3’, 19) <br /> 
							Loop the value of fetchall&gt;&gt;&gt; (4, ‘name4’, 26) <br /> 
							Fetch a piece of data&gt;&gt;&gt; (1, ‘leon’, 22) <br /> 
							Data after cyclic deletion&gt;&gt;&gt; (2, ‘cat’, 28) <br /> 
							Data after cyclic deletion&gt;&gt;&gt; (3, ‘name3’, 19) <br /> 
							Data after cyclic deletion&gt;&gt;&gt; (4, ‘name4’, 26)
					</dd>

                <h3>E. Summary</h3>
					<dd>
						In fact, create a table operation should check whether the table exists, you can use exception handling try...except<br>
						Update, modification and deletion should check the existence of table data, otherwise the program will report an error.<br>
						Python operation database insert statement placeholder problem<br>
						1. Use sqlite3 to connect to the database in Python, and the booth symbol of the insert statement is "?"<br>
						cur.execute("insert into user values(?,?,?)",(1,name,12))<br>
						2. In Python, use pymysql to connect to the mysql database, and the placeholder for the insert statement is "%s"<br>
						cursor.execute("insert into user values(%s, %s, %s)",(1,name,100))
					</dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/bottle"><span>START WITH BOTTLE</span>
		</div>

	</div>
</div>