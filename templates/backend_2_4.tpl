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
                            <a href="/backend/sql/query" style="background-color: #111;">2d. Query data in SQLite</a>
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
				<h1>How to Query data?</h1>

                <h3>A. Query all the data just inserted</h3> 
                    <dd>
                        <pre class="prettyprint"><code class=" hljs sql">c.execute(&#39;<span class="hljs-operator"><span class="hljs-keyword">SELECT</span> * <span class="hljs-keyword">FROM</span> person<span class="hljs-string">&#39;)</span></span></code></pre> 
				    </dd>

                <h3>B. To extract query data, the cursor object provides fetchall() and fetchone() methods<br>
                    The fetchall() method gets all the data and returns a two-dimensional list. The fetchone() method gets one of the results and returns a tuple</h3>

				    <dd><img src="img/backend_2_4_p1.png" alt="SQL Picture" height="150" width="800"></dd>

                <h3>C. You have to fetch again to fetch the data again, because the cursor has been</h3>
				    <dd><img src="img/backend_2_4_p2.png" alt="SQL Picture" height="150" width="800"></dd>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
                <a href="/backend/sql/delete"><span>LEARN DELETE DATA</span>
		</div>

	</div>
</div>