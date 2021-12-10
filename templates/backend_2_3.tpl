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
                            <a href="/backend/sql/insert" style="background-color: #111;">2c. Insert data in SQLite</a>
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
				<h1>How to insert data?</h1>
				<p>
                    <h3>A. Insert two pieces of data into the person table</h3>
                    <dd>
                        <h4>Method 1: directly construct an inserted SQL statement</h4>
                            <pre class="prettyprint"><code class=" hljs haskell"><span class="hljs-typedef"><span class="hljs-keyword">data</span> &#61; &#34;1,&#39;leon&#39;,22&#34;</span></pre></code>
                            <pre class="prettyprint"><code class=" hljs sql">c.execute(&#39;<span class="hljs-operator"><span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> person <span class="hljs-keyword">VALUES</span> (%s)<span class="hljs-string">&#39;%data)</span></span></code></pre> 
                        </dd>
                    
                    <dd>
                        <h4>Method 2: Use the placeholder "?" to avoid SQL injection</h4>
                            <pre class="prettyprint"><code class=" hljs sql">c.execute(&#39;<span class="hljs-operator"><span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> person <span class="hljs-keyword">VALUES</span> (?,?,?)<span class="hljs-string">&#39;,(2,&#39;</span>name2<span class="hljs-string">&#39;,28))</span></span></code></pre> 
                        </dd>

                    <h3>B. You can also use executemany() to execute multiple sql statements. Using executemany() is more efficient than using excute() to execute multiple sql statements in a loop.</h3>
				    <dd>
                        <pre class="prettyprint"><code class=" hljs sql">c.executemany(&#39;<span class="hljs-operator"><span class="hljs-keyword">INSERT</span> <span class="hljs-keyword">INTO</span> person <span class="hljs-keyword">VALUES</span> (?,?,?)<span class="hljs-string">&#39;,[(3,&#39;</span>name3<span class="hljs-string">&#39;,19),(4,&#39;</span>name4<span class="hljs-string">&#39;,26)])</span></span></code></pre> 
                    </dd>

                    <h3>C. These two insert data operations will not take effect immediately, you need to use the database object con to submit the operation:</h3>
				    <dd>
                        <pre class="prettyprint"><code class=" hljs sql">conn.<span class="hljs-operator"><span class="hljs-keyword">commit</span>()</span></code></pre> 
                    </dd>
                </p>
			</dt>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
			<a href="/backend/sql/query"><span>LEARN QUERY DATA</span>
		</div>

	</div>
</div>