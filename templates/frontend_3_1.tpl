<link rel="stylesheet" type="text/css" href="css/tutorial.css">

<div class="tutorial-container">
	<div class="nav-div">
		<ul class="nav-list">
			<li class="nav-title">
				<h3>CHAPTER 3 
				<h4>FRONTEND
			</li>
			<li class="nav-li">
				<a href="/frontend/intro">1. Frontend Introduction</a>
			</li>
			<li class="nav-li">
				<a href="/frontend/html">2. HTML</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/html/element">2a. HTML elements</a>
					</li>
					<li class="nav-li">
						<a href="/frontend/html/structure">2b. HTML structure</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/frontend/css">3. CSS</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/css/syntax" style="background-color: #111;">3a. CSS Syntax</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/frontend/js">4. JavaScript</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/js/guideline">4a. JavaScript Guideline</a>
					</li>
					<li class="nav-li">
						<a href="/frontend/js/extension">4b. JavaScript Extension</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/summary">5. Summary</a>
			</li>
		</ul>
	</div>
	<div class="content-div">
		<h1>CSS Syntax</h1>
		<dl>
			<dt><h3>A simple CSS looks like this:</h3></dt>
			<dd>
				<img src="img/css-syntax.png" alt="CSS Syntax">
			</dd>
			<br>
			<dd>The selector points to the HTML element you want to style.</dd>
			<dd>Property-Value decides the style you want for that element</dd>
			<dd>So in this example, we give the body element a navy blue color.</dd>

			<dt>Here are some CSS examples</dt>
			<dd>
				<img src="img/css-examples.png" alt="CSS Examples">
			</dd>

			<dt><h3>Some common CSS property</h3></dt>

			<dt><h3>How to link a CSS file with a HTML file?</h3></dt>
			<dd>Simply add this line into your HTML file, usually put it inside the header before the body tag</dd>
			<dd>&lt;link rel="stylesheet" type="text/css" href="/path/to/your/css-file"&gt;</dd>

			<dt><h3>Now to can solve our problem in the previous section where we want to place two div side by side in the same row</h3></dt>
			<dd><img src="img/html_layout.png" alt="HTML layout example"></dd>
			<dt><h3>And here's how we do it</h3></dt>

			<dt>First we need to put index section and content section in the same div</dt>
			<dd><img src="img/layout_demo_modified.png" alt="layout_demo_modified"></dd>

			<dt>Then we write CSS to style them</dt>
			<dd><img src="img/css_demo.png" alt="css_demo"></dd>

			<dt>And here's what is looks like</dt>
			<dd><img src="img/output_demo_modified.png" alt="output_demo_modified"></dd>

			<dt>So far we've learnt that HTML builds a structure for the webpage, and CSS styled in into what you want it to be</dt>
			<dt>We notice that with HTML+CSS, we only get static web page</dt>
			<dt>But what if we want to create dynamically updating content, control multimedia, animate images or something that's not static?</dt>
			<dt>Well that's where JavaScript kicks in, now lets find out what is JavaScript and how does it make webpage dynamic</dt>

		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
				<a href="/frontend/js"><span>Learn JavaScript</span></a>
			</div>
		</div>

	</div>
</div>